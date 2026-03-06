#TODO:1. For convenience, start by writing code that loops over all of your items and deletes them, then loops over all of your lists and deletes them. You can then run this code in order from the start and get the same result each time:
#1. catches all the rows in each model
#2. evaluate each row one by one
#3 delete each value as you loop through them:
#for some reason 
items = Item.objects.all()
lists = List.objects.all()
for item in items:
    item.delete()