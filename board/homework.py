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
    #TODO:2.2 Create 3 Lists  named "To Do", "In Progress", and "Done"?
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


