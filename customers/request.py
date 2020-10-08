CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct"
    },
    {
      "id": 2,
      "name": "Billy Bob",
      "address": "123 Main St."
    },
    {
      "id": 3,
      "name": "Tammy Thunder",
      "address": "123 Greenview Dr."
    },
    {
      "id": 4,
      "name": "Larry Loser",
      "address": "700 Harrison ln."
    },
    {
      "email": "becca@becca.com",
      "password": "me",
      "name": "Rebecca Parker",
      "id": 5
    },
    {
      "email": "r@r.com",
      "password": "me",
      "name": "Rebecca Parker",
      "id": 6
    }
]


def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    
    requested_customer = None

    for customer in CUSTOMERS:
        
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):

    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer


def delete_customer(id):
    customer_index = -1

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)