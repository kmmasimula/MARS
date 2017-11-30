from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import array
import math
import numpy as np
from collections import Counter
import csv
import sys
import pymongo
#from pymongo import Connection
from pprint import pprint

mylongest=0

def printneat(somelist,strs):
	#print("")
	#print(strs)
	for x in range(0,len(somelist)):
		print(somelist[x])

def saveToDB(jj,fn):
	#connection = pymongo.Connection("mongodb://localhost", safe = True) 

	#db = connection.m101
	#people = db.team
	person = {'name':'vreda pieterse', 'role':'president'}
	rr=np.array(jj)
	data = {}
	
	rank=[]
	hours=[]
	qualityarr=[]
	members=[]
	numrows=rr.shape[0]
	isrank=False
	ishour=False
	isquality=False
	countrank=0
	counthour=0
	countquality=0
	count=0
	incr=0;
	for x in range(0,numrows):
		members.append(rr[x][0])
		isrank=True
		count=2
		countrank=0
		counthour=0
		countquality=0
		while True:
			if isrank:
				#print("The count is :"+str(count)+" "+rr[x][count])
				if rr[x][count]=="":
					count=count+1
					countrank=countrank+1
					if countrank==numrows:
						rank.append(str(rr[x][count-numrows:count]))
						ishour=True
						isrank=False
						
				else:
					rank.append(str(rr[x][count:count+numrows]))
					count=count+numrows
					ishour=True
					isrank=False
					
			
			elif ishour :
				if rr[x][count]=="":
					count=count+1
					counthour=counthour+1
					if counthour==numrows:
						hours.append(str(rr[x][count-numrows:count]))	
						ishour=False
						isquality=True
					
						
				else:
					hours.append(str(rr[x][count:count+numrows]))
					count=count+numrows
					isquality=True
					ishour=False
			
			elif isquality:
				if rr[x][count-1]=="":
					count=count+1
					countquality=countquality+1
					if countquality==numrows:
						qualityarr.append(str(rr[x][count-numrows:count]))
						isquality=False
						break
				else:
					qualityarr.append(str(rr[x][count:count+numrows]))
					isquality=False
					#count=2
					break
			


	
	data['identifier']=fn
	data['TeamNr']=rr[0][1]
	data['TeamMembers']=members
	data['rank'] = rank
	data['hours']=hours
	data['quality']=qualityarr
	#people.insert(data)

	print("created objects saving to database")
	return data

def bunch(arr):
	temp=[]
	for x in range(len(arr)):
		if arr[x]:
			temp.append(arr[x])
	return temp

def getTeam(arr):
	temp=[]
	for x in range(0,len(arr)):
		item=arr[x][0]
		for p in range(1,len(arr[x])):
			#print(item)
			if arr[x][p]==item:
				#print("yippppie")
				#print(arr[x][0:p])
				temp.append(arr[x][0:p])
				break
	return temp

def getTeam2(arr):
	temp=[]
	for p in range(1,len(arr)):
		item=arr[0]
		if arr[p]==item:
			temp=arr[0:p]
			break
	return temp

def readFromFile(fname):
	fname="C:/Work/app/django/SATwebsite/media/2017_02Fixed.csv"
	print("This is the filename "+fname)

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
	with open(fname,"rt") as csvfile:
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

def checkErrors(obj):
	print("***************** Checking errors************")
	print(obj[3]['linenumber'])
	#print(obj[0]['matrix'])
	print("")
	
	for x in range(len(obj)):
		mat=obj[x]['matrix']
		#print("We are printing first col")
		col=getCol(mat)
		if len(obj[x]['membersCol'])%len(col)!=0:
			raise Exception("The number of members in row  do not match with col [team "+str(mat[0][1])+"]")

		if checkPattern(obj[x]['membersCol'])!="-1":
			raise Exception("The pattern of team members does not match [team "+str(mat[0][1])+"],line number "+str(obj[x]['linenumber'][0]))
		
		if checkSame(obj[x]['membersCol'],col)!="-1":
			nn=int(checkSame(obj[x]['membersCol'],col))
			raise Exception("Mismatch of team members [team "+str(mat[0][1])+"],line number "+str(obj[x]['linenumber'][nn]))
			
		#print(mat)
		if checkTeamNumber(mat)!="-1":
			nn=int(checkTeamNumber(mat))
			raise Exception("The pattern of team Numbers does not match [team "+str(mat[0][1])+"],line number "+str(obj[x]['linenumber'][nn]))
	
		if checkInvalid(mat)!=-1:
			nn=checkInvalid(mat)+1
			raise Exception("Invalid characters in matrix [team "+str(mat[0][1])+"],line number "+str(obj[x]['linenumber'][nn]))
	
	#raise Exception("Team number do not match ")
def checkInvalid(l1):
	for x in range(len(l1)):
		for p in range(len(l1[x])):
			
			if not l1[x][p]=="" :
				#print(l1[x][p])
				if "," in str(l1[x][p]):
					return x
				if str(l1[x][p]).isdigit()==False:
					return x
	return -1	
	"""
	if l1[4][2].isdigit()==True:
		print("It is number")
	if l1[4][2]=="":
		print("It is a space")
	print(l1[4][2])
	"""
def checkSame(l1,l2):
	i=0
	#print("This is l1 length: "+str(len(l1)))
	for x in range(len(l1)):
		if l1[x]!=l2[i]:
			return str(i+1)
		i=i+1
		if i==len(l2):
			i=0
	return "-1"
def checkPattern(l):
	actual=getTeam2(l)
	#print("Check pattern ")
	#mm="-1"
	if checkSame(l,actual)!="-1":
		return checkSame(l,actual)
	return "-1"
def checkTeamNumber(l):
	teamNumbers=[]
	pp=[]
	tt=""
	num=l[0][1]
	for x in range(len(l)):
		teamNumbers.append(l[x][1])
		pp.append(num)

	if checkSame(teamNumbers,pp)!="-1":
		return checkSame(teamNumbers,pp)
	return "-1"
def getCol(arr):
	ll=[]
	for x in range(len(arr)):
		ll.append(arr[x][0])
	return ll

def numRows(js):
	#print(js)
	rr=np.array(js)
	numr=rr.shape[0]
	option=str(js[0][1])
	count=1
	for x in range(0,numr):
		if str(option)!=str(js[x][1]):
			count=count+1
			option=str(js[x][1])
	return count

def cal(js,option):
	#print(mylongest)
	jsonObj=[]
	for x in range(0,len(js)):
		if str(option)==str(js[x][1]):
			jsonObj.append(js[x])
	return jsonObj

print('starting banzo server...')



'''
while True:
	option = int(input("Welcome , What would you like to do ? \n 1.View matrix\n2.save to database\n3.exit\n"))
	if option==3:
		break
	elif option==2:
		saveToDB(jj)
		
	else :
		option2 = str(input("Please enter the team number \n"))
		jj=readFromFile(option2,"2017_01.csv")
'''
#httpd.serve_forever()

#run()