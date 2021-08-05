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

# 6. Stock count 
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# 7. Get pets by breed
def get_pets_by_breed(pet_shop, dog_breed):
    pet_breeds = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == dog_breed:
            pet_breeds.append(pet)
    return pet_breeds

# 9. Find pet by name 

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

# 11. Remove pet by name 
def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

# 12. Add pet to stock 
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

# 13. Get customers cash
def get_customer_cash(customers):
        return customers["cash"]

# 14. Remove customer cash 
def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

# 15. Get customers pet count
def get_customer_pet_count(customer):
    return len(customer["pets"])

# 15. Add pet to customer
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

# Optional Tasks







