from django.shortcuts import render
from django.http import HttpResponse
from .models import Team,teamRank
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
		ti=filename+cc[0]['TeamNr']
		tr=cc[0]['rank']
		a=teamRank(teamID=ti,rankmatrix=tr)
		a.save()
		#for x in range(5):
		#	a=Marks(teamnumber=cc[x]['TeamNr'],teamMembers=cc[x]['TeamMembers'],identifier=cc[x]['identifier'],rank=cc[x]['rank'],quality=cc[x]['quality'],hours=cc[x]['hours'])
		#	a.save()
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
