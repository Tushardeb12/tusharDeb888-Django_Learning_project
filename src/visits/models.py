from django.db import models

# Create your models here.
class Pagevisit(models.Model):
    # db table
    # id -> primary key -> autofield -> 1, 2, 3, ...
    path = models.TextField(null = True) #col1
    time_stamp = models.DateTimeField(auto_now_add=True)    #col 2