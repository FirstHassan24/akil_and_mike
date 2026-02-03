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

#TODO:Configure a new django app, set up the models, migrate the database, and test your models in the shell for the following app:Model organizations and their employees. An employee can only work for one organization at a time. This modeling should be basically identical to what we did with Trello!
#1.DRAW an erd of the employee and the organization
#2.set up the models(link the foreign key:)
# 3.migrate the models
# 4.test the model in the shell 
#  5. YOUR DONE
