# 1. Get all items that belong to Groceries
Items.objects.fillter(Groceries)
# 2. Get the one list named Groceries
List.objects.get(Groceries)
# 3. Check whether any item named eggs exists
Item.objects.exists(eggs)
# 4. Get all items named eggs
Item.objects.filter(eggs)