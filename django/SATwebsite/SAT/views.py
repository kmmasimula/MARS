from django.shortcuts import render
from django.http import HttpResponse
from .models import Team,User,MBTI,participatoryentity,bellbin,teamattributes,teamRank,teamQuality,teamHours,teamMBTI,teambellbin
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .test import readFromFile,cal,saveToDB
from os.path import join, dirname, realpath
from werkzeug import secure_filename
import math
import numpy as np

# Create your views here.






def errors(request):
	#tr=["['' '' '' '' '' '' '']", "['0' '3' '1' '3' '1' '1' '0']", "['0' '1' '3' '3' '1' '1' '0']", "['1' '0' '1' '3' '1' '3' '0']", "['0' '1' '1' '3' '1' '3' '0']", "['' '' '' '' '' '' '']", "['0' '1' '1' '3' '1' '0' '3']"]
	#ti='2017_02_Rank.csv_1'
	#a=teamRank(teamID=ti,rankmatrix=tr)
	#a.save()


	tr=["['1' '3' '0' '1' '0' '1' '3']", "['0' '3' '0' '1' '1' '1' '3']", "['' '' '' '' '' '' '']", "['1' '3' '0' '1' '0' '1' '3']", "['0' '3' '0' '3' '1' '1' '1']", "['0' '3' '1' '1' '0' '3' '1']", "['1' '3' '0' '3' '0' '1' '1']"]
	ti='2017_02_Rank.csv_2'
	b=teamRank(teamID=ti,rankmatrix=tr)
	b.save()
	tr=["['3' '0' '1' '0' '1' '3']", "['3' '1' '0' '1' '0' '3']", "['0' '1' '1' '0' '3' '3']", "['3' '0' '0' '1' '1' '3']", "['0' '0' '3' '1' '1' '3']", "['1' '0' '1' '0' '3' '3']"]
	ti='2017_02_Rank.csv_3'
	c=teamRank(teamID=ti,rankmatrix=tr)
	c.save()
	tr=["['3' '1' '1' '0' '3' '0' '1']", "['1' '1' '3' '1' '3' '0' '0']", "['1' '1' '1' '3' '3' '0' '0']", "['1' '1' '1' '3' '3' '0' '0']", "['1' '1' '1' '3' '3' '0' '0']", "['1' '0' '1' '0' '3' '1' '3']", "['1' '0' '3' '0' '3' '1' '1']"]
	ti='2017_02_Rank.csv_4'
	d=teamRank(teamID=ti,rankmatrix=tr)
	d.save()
	tr=["['3' '1' '3' '1' '0' '0']", "['' '' '' '' '' '']", "['3' '1' '3' '1' '0' '0']", "['3' '3' '0' '1' '1' '0']", "['' '' '' '' '' '']", "['' '' '' '' '' '']"]
	ti='2017_02_Rank.csv_5'
	e=teamRank(teamID=ti,rankmatrix=tr)
	e.save()
	tr=["['3' '3' '0' '1' '1' '0']", "['3' '3' '1' '0' '1' '0']", "['1' '3' '1' '0' '3' '0']", "['0' '3' '3' '1' '0' '1']", "['3' '3' '0' '1' '1' '0']", "['3' '0' '0' '1' '3' '1']"]
	ti='2017_02_Rank.csv_6'
	f=teamRank(teamID=ti,rankmatrix=tr)
	f.save()

	teams=[]
	mylist=[]
	num1=0
	num2=0
	listJSON2=[]
	data2={}
	data1={}
	zonke=teamRank.objects.all()
	for ma in zonke:
		zonke1=ma
		print(zonke1)
		teams.append(zonke1)

	
	class MyError(Exception):
		def _init_(self,value):
			self.value=value
		def _str_(self):
			return repr(self.value)

	import csv
	def something(array):
		a=1
		bv=False
		while(bv!=True):
			if a**2==len(array):
				return a
			elif a**2>len(array):
				return -1
			a=a+1



	
		
	def checkifcontains(arr,countR):
			#print(len(arr))
			ds=int(math.sqrt(countR))
			for x in range(0,countR):
				if arr[x] not in ('0','1','3',''):
					return False
					
			return True
			#print("Correct")
				

	def checkifsquare(arr):
			#if not arr:
			#	return True
			#m=len(arr)
			#n=len(arr[0])
			if (something(arr)==-1):
				return False
			else:
				return True
	def checkcolumn(arr):
		we=int(math.sqrt(len(arr)))
		#print(we)
		list2=[]
		nparr=np.array(arr)
		#print(nparr)
		try:
			list2=nparr.reshape(we,we)
		except Exception as e:
			raise MyError("Not square")
		#list2=nparr.reshape(we,we)
		arr=list2
		data2={}
		#print(len(arr))
		cnt0=0
		cnt3=0
		#print(listJSON2)
		for i in range(len(arr)):
			cnt=0
			for j in range(len(arr)):
				if(arr[j][i]=='0')or(arr[j][i]==''):
						cnt=cnt+1
				if(arr[j][i]==3):
					cnt=0
					break
				#print("number of 0")
				#print(cnt)
			if(cnt!=0 and cnt/len(arr)>=0.8):	
				print("Result 1:")
				print(json.dumps({"colNum":i}))
				data2={}
				data2['colNum']=i
				listJSON2.append(data2)
			else:
				data2={}
				data2['colNum']=''
				listJSON2.append(data2)
		
		
		for i in range(len(arr)):
			cnt=0
			for j in range(len(arr)):
				if(arr[j][i]==0):
					cnt=0
				if(arr[j][i]=='3' )or(arr[j][i]==''):
					cnt=cnt+1
					break
			if(cnt!=0 and cnt/len(arr)>=0.8):
				print("Result 2:")
				print(json.dumps({"colNum":i}))
				data2['colNumInv']=i
				listJSON2.append(data2)
			else:
				data2['colNumInv']=''
				listJSON2.append(data2)
		#print(listJSON2)
				
				
				#print(data2)

	def flatt(arr):
		finalarr=[]
		print(arr)
		for x in range(len(arr)):
			for p in range(len(arr[x])):
				if arr[x][p] in ('0' ,'1' ,'3','') :
					finalarr.append(arr[x][p])
		return finalarr

	def check2p0(arr):
		numof3=0
		numof1=0
		numof0=0
		we=int(math.sqrt(len(arr)))
		#print(we)
		list2=[]
		nparr=np.array(arr)
		#print(nparr)
		list2=nparr.reshape(we,we)
		arr=list2
		#print(list2)
		if we <5:
			numof0=2
			numof3=numof0
			numof1=we-(numof3+numof3)
			
			numofe=we
		else:
			numof0=math.floor(len(arr) / 3)
			numof1=math.ceil(len(arr)%3)+numof0
			numof3=numof0	
		for i in range(len(arr)):
			cnt1=0
			cnt3=0
			cnt0=0
			cnte=0
			for j in range(len(arr)):
				#print(arr[i][j])
				if(arr[i][j]=='1'):
					cnt1=cnt1+1
				if(arr[i][j]==''):
					cnte=cnte+1
				if(arr[i][j]=='0'):
					cnt0=cnt0+1
				if(arr[i][j]=='3'):
					cnt3=cnt3+1	
			
		if(numof0==cnt0)and(numof1==cnt1)and(numof3==cnt3)or(numofe==cnte)or(cnte==1):
			return True
		else:
			return False
	#end of the functions
	option=1
	if (option == 1):


		#try:
		vivo=[]			
		myarr=[]
		list2=[]
		my2d=[]
		listJSON=[]
		data={}
		apex='static/'
		

		#list2=[['0','1','3','0','0','1','3','0','0'],['1','3','0','0','1','3','0']]
		print("This is flat")
		#for x in range(3):
		#	list2.append(flatt(teams[x]['rank']))
		#print(flatt(teams[0]['rank']))
		#print(list2)
		print('############\n LENGTH')
		print(len(teams))
		for x in range(0,len(teams)):
				list2=flatt(teams[x].rankmatrix)
				print(list2)
				cc=something(list2[x])
				#print(list2[x])
				try:
					checkcolumn(list2[x])
					b=checkifcontains(list2[x],len(list2[x]))
					if not b:

						raise MyError("Contains other numbers")
						#quit()
					a=checkifsquare(list2[x])
					
					if cc==-1:
						raise MyError("Not square")
						#quit()
						
					c=check2p0(list2[x])
					if not c:
						raise MyError("Invalid row balance")
					
					
					
				except Exception as e:
					print("Handling error:"+str(e.args))
					#print(listJSON2[x]['colNum'])
					#db=db.lol.insert
					mylist.append(
       				{
       					'row':'',
       					'File':teams[x].teamID,
       					'ColNum':num1,
       					'ColNumInv':num2,
        				'Message':str(e.args)
        			})
	print(zonke)
	return render(request, 'asd.html',{"myteam":mylist})




def index(request):
	return render(request, 'home.html')
UPLOAD_FOLDER=join(dirname(realpath(__file__)), 'static/uploads/..')
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
		ti=filename+'_'+cc[0]['TeamNr']
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
