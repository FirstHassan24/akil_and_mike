from django.db import models

# Create your models here.
from django.db import models

#trello list such as todo or in progress
class List(models.Model):
    name = models.TextField(max_length=30)

#cards in a list, such as "make migrations" in the "TO DO" List
class Item(models.Model):
    list= models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.TextField(max_length=200,)
    description = models.TextField(null=True)
    pass

#TODO: