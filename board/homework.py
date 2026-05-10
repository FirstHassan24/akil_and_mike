from board.models import *
#TODO:1. For convenience, start by writing code that loops over all of your items and deletes them, then loops over all of your lists and deletes them. You can then run this code in order from the start and get the same result each time:
#1. catches all the rows in each model
#2. evaluate each row one by one
#3 delete each value as you loop through them:
def run():
    #print("hello am i showing up in the terminal?")
    for item in Item.objects.all():
        item.delete()
    for list in List.objects.all():
        list.delete()
    # print(List.objects.all())
    # print(Item.objects.all())
    #TODO:2.2 Create 3 Lists  named "To Do", "In Progress", and "Done" in the list model?
    todo=List(name="To DO")
    todo.save()
    progress=List(name="In Progress")
    progress.save()
    done=List(name="Done")
    done.save()
    print(List.objects.all())
    print(Item.objects.all())
    for list in List.objects.all():
        print(list.name)
    #TODO:3.in "Done", create three items: "Eat breakfast", "Eat lunch", and "Shower". Do this by finding the List by filtering on its name (consider using .get) and storing it in a variable,
    # then using the list's `item_set` relation. Remember: if you use the item_set relation, you don't have to pass a list argument when creating or filtering on an item, as they are already related to a specific list.
    #create the list that i will be storing the data into:
    done = List.objects.get(name="Done")
    #using the item_set method create and store breakfast inside done list
    done.item_set.create(title="Eat breakfast")
    #
    done.item_set.create(title="Eat lunch",description="what are you eating in the afternoon?")
    done.item_set.create(title="Shower")

    #TODO:4. Find "Shower" by its name and delete it. Bonus: Google (or read the doc) how to do a case-insensitive filter and find it by searching for "shower" (lowercase).
    Item.objects.get(title__iexact="shower").delete()

    #TODO: 5.1.Write code that finds all items that start with "Eat" and 2.updates each of them to say "Make" . In other words, "Eat Breakfast" becomes "Make Breakfast", etc. Note that while you've seen how to search for a substring anywhere in the value, you'll have to Google (or read the doc) to learn how to search only the start of a string. Note that whenever I say "find" I mean using the Django ORM, not with python if statements. You'll need loops, but no if statements in this assignment.
    eat = Item.objects.filter(title__startswith="Eat")
    make = eat.get(title="Eat breakfast")
   
    #TODOL:5.2:mentor:good job doing it individually now set it up so it loops over the queryset and auto changes "Eat" to "Make".
    for item in eat:
      item.title=item.title.replace("eat","make")
      item.save()


