#TODO:1. For convenience, start by writing code that loops over all of your items and deletes them, then loops over all of your lists and deletes them. You can then run this code in order from the start and get the same result each time:
#1. in the shell import the models,
#2. loop over the first model
from .models import Item,List
#store all the values from the model in a variable:
items = Item.objects.all()
lists = List.objects.all()
for item in items:
    #store  each item:
    delete=items.objects.filter(item)
    #save it to the database:
    delete.save()
    #delete each item you saved:
    delete.delete()
