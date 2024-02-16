from cart import Cart
from customer import Customer
from cashier import Cashier
from product import Product

if __name__ == "__main__":
    customer = Customer(
        "Buy",
        Cart([
            Product("Goya", 20.00, "02/20/2024"),
            Product("Toblerone", 100.00, "03/03/2024"),
            ])
    )
    cashier = Cashier("Mark")

    cashier.is_closing_time(customer)