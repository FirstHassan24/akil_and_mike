# ========= DJANGO ORM TRAINING =========

# MODELS MENTAL MAP
# List = parent
# Item = child
# Item has a ForeignKey to List

# -------------------------------
# 1. CREATE A PARENT
# -------------------------------

# groceries = List.objects.create(name="Groceries")

# Question:
# What does groceries hold?
# A single List object

# -------------------------------
# 2. CREATE CHILDREN
# -------------------------------

# Item.objects.create(
#     list=groceries,
#     title="Eggs",
#     description="Buy a dozen"
# )

# Item.objects.create(
#     list=groceries,
#     title="Milk",
#     description="2 percent"
# )

# Question:
# Why do we pass list=groceries?
# Because each Item must point to its parent List

# -------------------------------
# 3. GET ONE EXACT OBJECT
# -------------------------------

# groceries = List.objects.get(name="Groceries")

# Question:
# What does .get() return?
# One exact object

# Failure cases:
# - no match
# - more than one match

# -------------------------------
# 4. GET MANY MATCHES
# -------------------------------

# items = Item.objects.filter(list=groceries)

# Question:
# What does .filter() return?
# A QuerySet of matching objects

# -------------------------------
# 5. YES / NO CHECK
# -------------------------------

# has_eggs = Item.objects.filter(title="Eggs").exists()

# Question:
# What does .exists() return?
# A boolean

# -------------------------------
# 6. LAZY VS FETCH
# -------------------------------

# qs = Item.objects.filter(title="Eggs")   # lazy
# list(qs)                                 # fetches
# qs.exists()                              # fetches

# Question:
# Which lines are lazy and which fetch?

# -------------------------------
# 7. CHILD TO PARENT
# -------------------------------

# egg = Item.objects.get(title="Eggs")

# Question:
# If I already have egg, how do I think about its list?
# "This child belongs to one parent"

# -------------------------------
# 8. PARENT TO CHILDREN
# -------------------------------

# groceries = List.objects.get(name="Groceries")

# Question:
# If I already have groceries, what should I expect back
# when asking for its items?
# A QuerySet of Item objects