import datetime

class Cashier:
    def __init__(self, name) -> None:
        self.name = name
        self.closing_time = "22:00:00"
        self.opening_time = "08:00:00"
        self.scanned_items = []

    def is_closing_time(self, customer):
        current_time = datetime.datetime.now()
        #formatted_time = "00:00:00"
        formatted_time = current_time.strftime("%H:%M:%S")

        if formatted_time >= self.closing_time or formatted_time < self.opening_time:
            print("Sorry we're closed!")
        else:
            self.receive_customer(customer)

    def receive_customer(self, customer):
        if customer.business == "Buy":
            self.scan_cart(customer.cart)

    def scan_cart(self, cart):
        current_date = datetime.datetime.now()
        formatted_date = current_date.strftime("%m/%d/%Y")

        for item in cart.items:
            item_expiration = item.expiration
            if item_expiration <= formatted_date:
                del item
                print("Item Removed")

            else:
                self.scanned_items.append({"Product Name": item.name, "Price": item.price})
                print(self.scanned_items)
                print("Not Expired")
