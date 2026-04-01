# 1. Create one List called "Groceries"
Groceries= List.objects.create(name="Groceries")
# 2. Create two Items linked to that list
Item.objects.create(
    #what confuses me here is how does this experession connect to 
    list="Groceries",
    title="eggs"
    description="buy a dozen eggs"
)
# 3. Get the one exact Groceries list

# 4. Check whether any Item named "Eggs" exists