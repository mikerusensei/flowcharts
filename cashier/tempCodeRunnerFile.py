from cart import Cart
from customer import Customer
from cashier import Cashier

if __name__ == "__main__":
    customer = Customer("Jomari",
                        "Buy",
                        Cart([{"Product Name": "toothpaste", "Expiration": "2/20/2024"},
                              {"Product Name": "shampoo", "Expiration": "2/14/2024"}
                              ]
                              ))
    cashier = Cashier("Mark")

    cashier.receive_customer(customer)
