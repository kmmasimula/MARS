__author__='mLab'


import os
import math
import numpy as np
from flask import Flask,flash , render_template,url_for ,request,redirect
from bson.objectid import ObjectId
from data import Articles
import pymongo
from flask_pymongo import PyMongo 
import json
import test as f1


#connection = pymongo.MongoClient("ds121726.mlab.com", 21726)
#db = connection["satellite"]

passs="banzo"
usee="mybd"

MONGODB_URI='mongodb://'+usee+':'+passs+'@ds121726.mlab.com:21726/satellite'
client=pymongo.MongoClient(MONGODB_URI)

db=client.get_default_database()
myvr=db['team']
myvr.insert({"name":"banele"})

APP_ROOT =os.path.dirname(os.path.abspath(__file__))
app=Flask(__name__)

'''app.config['MONGO_DBNAME']='satellite'
app.config['MONGO_URI']='mongodb://test:test@ds121726.mlab.com:21726/satellite'

mongo=PyMongo(app)'''

Articles=Articles()
cc=[]

@app.route('/uploadpage')
def uploadpage():
	return render_template('upload.html')

@app.route('/objectpage')
def objectpage():
	return render_template('objects.html')

@app.route('/upload',methods=['POST'])
def upload():

	try:
		#cc=[]
		target =os.path.join(APP_ROOT,'myuploads')
		print("This is the target "+target)

		if not os.path.isdir(target):
			os.mkdir(target)
		
		for sfile in request.files.getlist("file"):
			print(sfile)
			filename=sfile.filename
			destination="/".join([target,filename])
			
			sfile.save(destination)
			
			myobject=f1.readFromFile(filename)
			f1.checkErrors(myobject)
			#cc=[]
			for x in range(0,len(myobject)):
				thegame=f1.cal(myobject[x]['matrix'],x+1)
				#thegame=f1.bunch()
				#print(thegame)
				cc.append(f1.saveToDB(thegame,filename))
			flash('You have uplodaed the file','success')
	except ValueError:
		flash('Invalid characters in matrix','danger')
		return render_template("home.html")
	except Exception as e:
		flash(str(e),'danger')
		return render_template("home.html")

	return render_template("objects.html",myteam=cc[0])

@app.route('/edit/<string:id>',methods=['GET','POST'])
def edit(id):
	try:
		#print("my id is "+id)
		machine=db.team.find_one({"_id":ObjectId(id)})
		print("hello "+str(machine['TeamNr']))
		#for mach in machine:
			
		
	except Exception as e:
		return str(e)
	return redirect(url_for('home'))

@app.route('/delete/<string:id>',methods=['GET','POST'])
def delete(id):
	try:
		#print("my id is "+id)
		machine=db.team.remove({"_id":ObjectId(id)})
		flash('Object is deleted ','success')
		#for mach in machine:
			
		
	except Exception as e:
		return str(e)
	return redirect(url_for('articles'))

@app.route('/getmachine',methods=['GET','POST'])
def getMatchine():
	try:
		results=""
		if request.method=='POST' and request.form['mysearch']:
			results=request.form['mysearch']
			machine=db.team.find({"TeamNr":str(results)})
		elif request.method=='POST' and request.form['deleteAll']:
			start=request.form['deleteAll']=='drop'
			if start:
				machine=db.team.drop()
				flash('The whole table has been deleted ','success')
				return redirect(url_for('home'))
		else:
			machine=db.team.find()

		teams=[]
		for mach in machine:
			teamlist={
			'teamM':str(mach['TeamMembers']),
			'teamno':str(mach['TeamNr']),
			'id':str(mach['identifier']),
			'hour':str(mach['hours']),
			'rank':str(mach['rank']),
			'quality':str(mach['quality']),
			'myid':mach['_id']
			}
			teams.append(teamlist)
	except Exception as e:
		return str(e)
	return render_template('articles.html',myteam=teams)

@app.route('/mypersist',methods=['GET','POST'])
def mypersist():
	try:
		if len(cc)!=0:
			return redirect(url_for('persistpage'))
		
		results=""
		
		
		
	except Exception as e:
		return str(e)
	return render_template('home.html')

@app.route('/replace',methods=['GET','POST'])
def replace():
	if request.method=='POST' :
		#persist to db
		print("hello replace")
		start=request.form['myreplace']=='replace'
		if start:
			for x in range(len(cc)):
				db.team.update(cc[x],cc[x],upsert=True)
			flash('The objects have been replaced successfully ','success')
			return render_template('home.html')
		else :
			flash('The objects have droped','success')
			return render_template('home.html')
		
	return render_template('replacing.html',myteam=cc)

@app.route('/')
def index():
	cc=[]
	return render_template('home.html',)

@app.route('/home',methods=['GET','POST'])
def home():
	cc=[]
	#if request.method=='GET':
	#	start=request.form['cancel']=='ignore'
	#	if start:
	#		flash("Objects have been ignored","success")
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/errors')
def errors():
	machine=db.team.find()
	mylist=[]
	teams=[]
	for mach in machine:
		teamlist={
		'teamM':str(mach['TeamMembers']),
		'teamno':str(mach['TeamNr']),
		'id':str(mach['identifier']),
		'hour':str(mach['hours']),
		'rank':str(mach['rank']),
		'quality':str(mach['quality']),
		'myid':mach['_id']
		}
		teams.append(teamlist)

	print(teams[0]['id'])
	#these are the functions
	num1=0
	num2=0
	listJSON2=[]
	data2={}
	data1={}

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
		#arr=arr.toList()
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
		for x in range(0,len(teams)):
				list2=flatt(teams[x]['rank'])
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
       					'row':teams[x]['teamno'],
       					'File':teams[x]['id'],
       					'ColNum':num1,
       					'ColNumInv':num2,
        				'Message':str(e.args)
        			})
	return render_template('asd.html',myteam=mylist)

@app.route('/persistpage',methods=['GET','POST'])
def persistpage():
	if request.method=='POST' and request.form['mypersist']:
		#persist to db
		print("hello persist")
		print(cc[0])
		for x in range(len(cc)):
			if db.team.find(cc[x]).count()>0:
				flash('The objects already in the database ','danger')
				return redirect(url_for('replace'))
			db.team.update(cc[x],cc[x],upsert=True)
		flash('The objects have been persisted successfully ','success')
		return render_template('home.html')


	return render_template('persist.html',myteam=cc)

@app.route('/articles')
def articles():
	return render_template('articles.html',articles=Articles)

if __name__ == "__main__":
    app.secret_key='secret123'
    app.run(debug=True)

