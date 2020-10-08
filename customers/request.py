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