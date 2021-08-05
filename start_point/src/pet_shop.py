# WRITE YOUR FUNCTIONS HERE

# 1. Get pet shop name
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# 2. Get total cash 
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# 3. Add or remove cash
def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

# 4. Get pets_sold
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# 5. Increase pets_sold
def increase_pets_sold(pet_shop, new_pets_sold):
    pet_shop["admin"]["pets_sold"] += new_pets_sold


