from django.db import models
from vhaanmain.models import statelists
from uuid import uuid4

# Create your models here.
class admin_list(models.Model):
    admin_name = models.CharField(max_length = 80,default="default")
    admin_password = models.CharField(max_length = 80,default="default")
    auth_token = models.CharField(max_length=280,default = uuid4,editable = False)
    
    def __str__(self):
        return self.admin_name
    
class stateAssign_admin_custom(models.Model):
    admin_name = models.ForeignKey(admin_list,on_delete= models.CASCADE,null = True)
    state_name = models.ForeignKey(statelists,on_delete= models.CASCADE,null = True)