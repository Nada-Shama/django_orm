from django.db import models

# Create your models here.
class Dojo(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=2)
    desc=models.TextField(default='old_dojo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"
    
class Ninja(models.Model):
    f_name=models.CharField(max_length=255)
    l_name=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    dojo = models.ForeignKey(Dojo,related_name='ninjas',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.f_name} {self.l_name}"