# 1. Get all items that belong to Groceries
Item.objects.filter(list= Groceries)
# 2. Get the one list named Groceries
List.objects.get(name="Groceries")
# 3. Check whether any item named eggs exists
Item.objects.filter(name="eggs").exists()
# 4. Get all items named eggs
Item.objects.filter(name="eggs")