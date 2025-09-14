from django.db import models
import re
from datetime import datetime
# Create your models here.

class ShowManage(models.Manager):
    def validaterShow(self,postData):
        error={}
        
        r_date = postData.get('r_date', '')
        
        
        if postData['title']:
            if len(postData['title'])<2:
                error['len_title']='The title should be at least 3 letters'
        else:
             error['null_title']='You must enter a title' 
             
        if postData['network'] :
            if len(postData['network'])<2:
                error['len_network']='The network should be at least 3 letters'
        else:
             error['null_network']='You must enter a network' 
             

        if len(postData['desc'])<10:
                error['len_description']='The description should be at least 3 letters'
 
             
        if  r_date :
            rejex = re.compile(r'^\d{2}-\d{2}-\d{4}$')
            if(not rejex.match(r_date)):
                error['format_r_date']='The release date format is incorrect' 
            else:
                date_obj = datetime.strptime(r_date, "%m-%d-%Y").date()
                if date_obj > datetime.today().date():
                    error['future_date']='The release date must be in the past'
        else:    
            error['null_r_date']='You must enter a release date' 
             
                         
        return error



class Show(models.Model):
    title=models.CharField( max_length=50)
    network=models.CharField( max_length=50)
    release_date = models.DateField()
    description=models.TextField(default="Hello World")
    objects = ShowManage()
    created_at = models.DateTimeField(  auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"