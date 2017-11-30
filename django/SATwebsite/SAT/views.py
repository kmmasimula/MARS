from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
#from .test import readFromFile
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
		#myobject=readFromFile(uploaded_file_url)
		return render(request, 'home.html')
	else :
		return render(request,'upload.html')

@csrf_protect
def fileupload(request):
	
	if (request.method =='POST'):
		return render(request, 'home.html')

	return render(request, 'home.html')
	
def readFromFile(fname):
	#fname="2017_02Fixed.csv"
	print("This is the filename "+fname)
	#client = MongoClient()
	#db = client['mytest']
	#coll=db['mytable']

	myarr=[]
	my2d=[]
	myfinal=[]
	#jsonObj={"Rank":[],"Hours":[],"Quality":[]}
	
	strJ="";
	useless=""
	longestcol=0
	longestrow=0
	numTeams=0;
	members=[]
	banzo=[]
	k=0
	#myHeaders=["UserID","TeamID",1,2,3]
	with open(fname,"rb") as csvfile:
			isKopp=False
			lineArray=[]
			lineNum=1
			for row in csv.reader(csvfile, delimiter=';'):
				if not row[0] and not row[1] :
					lineArray.append(lineNum)
					if isKopp:
						banzo.append(myarr)
						myarr=[]

					members.append(row[2:])
					isKopp=True
					#print("This is the first: "+str(row[2]))
				elif row[0]:
					lineArray.append(lineNum) 
					myarr.append(row)
				lineNum=lineNum+1

			banzo.append(myarr)
			#print("This is banzo")
			#printneat(banzo[1],"")

			for x in range(len(members)):
				members[x]=bunch(members[x])
			#members=getTeam(members)
			tmp=0
			for x in range(0,len(members)):
				jsonObj={}
				jsonObj['membersCol']=members[x]
				jsonObj['matrix']=banzo[x]
				jsonObj['linenumber']=lineArray[tmp:tmp+len(banzo[x])+1]
				myfinal.append(jsonObj)
				tmp=tmp+len(banzo[x])+1

			
			
			

	return myfinal
