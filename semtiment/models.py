from django.db import models

# Create your models here.
class ResultsModel(models.Model):
    semtiment = models.CharField(max_length=4096,null=True)
    view = models.CharField(max_length=4096,null = True)
    sentence = models.TextField(max_length=9999,null = True)

    
