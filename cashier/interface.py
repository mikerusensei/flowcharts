from customer import Customer
from product import Product
from cart import Cart

import os
import time

class Interface:

    @staticmethod
    def show_menu():
        running = True

        while running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Welcome to Store\n")
            print("What can I help to you?\n")
            print("[1] Buy\n[2] Return\n[3] Exit")

            choice = input("\nEnter your choice: ")
            
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                print("Exiting Program...")
                time.sleep(1)
                running = False
            else:
                print("ERROR: Invlid input. Press [Enter] to continue.")
                input()
    
    @staticmethod
    def show_buy_window():
        running = True

        while running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Select products you want to buy\n")
            

if __name__ == "__main__":
    Interface.show_menu()