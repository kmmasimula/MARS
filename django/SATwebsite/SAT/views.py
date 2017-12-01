from django.shortcuts import render
from django.http import HttpResponse
from .models import Team,teamRank,teamQuality,teamHours
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .test import readFromFile,cal,saveToDB

# Create your views here.

def index(request):
	return render(request, 'home.html')

@csrf_protect
def upload(request):
	if (request.method =='POST'):
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		print("this is the url "+uploaded_file_url)
		#uploaded_file_url=".."+uploaded_file_url
		cc=[]
		myobject=readFromFile(uploaded_file_url)
		for x in range(0,len(myobject)):
				thegame=cal(myobject[x]['matrix'],x+1)
				#thegame=f1.bunch()
				#print(thegame)
				cc.append(saveToDB(thegame,filename))

		
		print(cc[0]['TeamNr'])
		
		for p in range(len(cc)):
			ti=filename+"_"+cc[p]['TeamNr']
			tr=cc[p]['rank']
			tq=cc[p]['quality']
			th=cc[p]['hours']
			a=teamRank(teamID=ti,rankmatrix=tr)
			b=teamQuality(teamID=ti,qualitymatrix=tq)
			c=teamHours(teamID=ti,hoursmatrix=th)
			a.save()
			b.save()
			c.save()
		
		return render(request, 'view.html',{"data":cc})
	else :
		return render(request,'upload.html')

@csrf_protect
def fileupload(request):
	
	if (request.method =='POST'):
		return render(request, 'home.html')

	return render(request, 'home.html')
	
def view(request):
	mydata={}#Marks.objects.all()
	return render(request, 'view.html',{"data":mydata})
