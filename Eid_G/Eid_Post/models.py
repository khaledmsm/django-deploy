from django.db import models
# Create your models here.

class Name(models.Model):
    massenger_name = models.CharField(max_length=255,null=True,blank=True)
    action_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='Eid_G/images/',blank=True,null=True)

    def __str__(self):
        return str(self.massenger_name)
