from django.db import models

class Petition(models.Model):
    petitionurl=models.CharField(max_length=150,default="http://localhost:8000")
    petitionstartdate=models.DateField()
    petitiontitle=models.CharField(max_length=100)
    petitionbackstory=models.TextField()
    petitionsubtitle=models.CharField(max_length=255)
    petitioncountyes=models.IntegerField(default=0)
    petitioncountno=models.IntegerField(default=0)
    petitionwhy=models.TextField()
    petitionprooflink=models.TextField()
    petitionlocation=models.TextField()
    petitionthreshold=models.IntegerField()
    petitionstatus=models.BooleanField(default=True)
    petitioncountview=models.IntegerField(default=0)
    petitiontotalengagement=models.IntegerField(default=0)
   # def __str__(self):
    #    return self.petitiontitle
