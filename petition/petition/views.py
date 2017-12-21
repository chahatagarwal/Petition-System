from django.http import JsonResponse
from django.core import serializers
from petition.models import Petition
import json

def petition(request,task_id=None):
    petitionurl="http://localhost:8000"+request.path
    if request.method=="GET":
        obj=[]
        #obj=serializers.serialize("json",Petition.objects.all())           
        obj=list(Petition.objects.values())
        for i in obj:
            i["petitionurl"]=petitionurl
            
        return JsonResponse({"Petition":obj},status=200)  
    elif request.method=="POST":
        data=json.loads(request.body)
        obj=Petition.objects.create(petitionstartdate=data["petitionstartdate"],
            petitiontitle=data["petitiontitle"],petitionbackstory=data["petitionbackstory"],
            petitionsubtitle=data["petitionsubtitle"],petitionwhy=data["petitionwhy"],
            petitionprooflink=data["petitionprooflink"],petitionlocation=data["petitionlocation"],
            petitionthreshold=data["petitionthreshold"])
        obj.save()
        if obj:
            return JsonResponse({"success":True},status=200)
        else:
            return JsonResponse({"failed":False},status=400)            

def petitiondisplay(request,task_id=None):
    if request.method=="GET":
        id=task_id
        petitionurl="http://localhost:8000"+request.path
        if id:
            obj=Petition.objects.get(id=id)
            obj.petitioncountview += 1
            obj.petitiontotalengagement = obj.petitioncountyes + obj.petitioncountno        
            if obj.petitioncountyes > obj.petitionthreshold:
                obj.petitionstatus=False
            obj.save()            
            if obj.petitionstatus:
                obj1=[]         
                obj1=list(Petition.objects.filter(id=id).values())
                for i in obj1:
                    i["petitionurl"]=petitionurl
                #obj=serializers.serialize("json",[obj])  
                return JsonResponse({"Petition":obj1},status=200)
            else:
                return JsonResponse({"failed":False},status=400)

def petitionyes(request,task_id=None):
    if request.method=="POST":
            id=task_id
            petitionurl="http://localhost:8000"+request.path
            if id:
                obj=Petition.objects.get(id=id)
                obj.petitioncountyes += 1
                obj.save()
                return JsonResponse({"success":True},status=200)

def petitionno(request,task_id=None):
    if request.method=="POST":
            id=task_id
            petitionurl="http://localhost:8000"+request.path
            if id:
                obj=Petition.objects.get(id=id)
                obj.petitioncountno += 1
                obj.save()
                return JsonResponse({"success":True},status=200)
