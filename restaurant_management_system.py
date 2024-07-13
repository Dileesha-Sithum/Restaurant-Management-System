class MenuItem:
    def __init__(self):
        # Initialize the menu items and their prices
        self.menu_items = {
            "House Cured Bourbon Gravadlax": 9.99, 
            "Bloc de pate": 14.99, 
            "village market testing plate": 7.99, 
            "White's Out seafood cocktail": 14.99, 
            "Essex camembert souffle": 9.99,
            "Beef": 45.99, 
            "Steak Diane": 49.99, 
            "Lobster": 49.99, 
            "Rack of Welsh lamb": 24.99, 
            "pan fried cod loin": 24.99, 
            "Charred cauliflower steak": 29.99,
            "poached alice pears": 8.99, 
            "Apricot & brandy macaroon": 7.99, 
            "Floating island": 7.99, 
            "Dark chocolate & strawberry cheesecake": 8.99, 
            "Macadamia blondie & chocolate brownie": 5.99,
            "Coffee & biscuits": 5.99,
            "Wine": 8, 
            "Water": 1, 
            "Soda": 2
        }
        # Initialize the popularity of each menu item to zero
        self.menu_popularity = {item: 0 for item in self.menu_items.keys()}

    def display_menu_items(self):
        # Display the menu items and their prices
        for item, price in self.menu_items.items():
            print(f"{item}: ${price:.2f}")


class Restaurant:
    def __init__(self):
        # Initialize the tables for early and late sessions
        self.earlysession_tables = {i: {
            "status": "Free",
            "Session": "",
            "Customer Name": "",
            "Number of Diners": 0,
            "orders": {},
            "cost": 0
        } for i in range(1, 6)}
        self.latesession_tables = {i: {
            "status": "Free",
            "Session": "",
            "Customer Name": "",
            "Number of Diners": 0,
            "orders": {},
            "cost": 0
        } for i in range(1, 6)}
        # Initialize lists to track booked tables
        self.earlysession_booked_tables = []
        self.latesession_booked_tables = []
        # Initialize other variables for orders, income, tips, and menu
        self.priority_orders = []
        self.total_income = 0
        self.table_costs = {}
        self.total_amount_tips = 0
        self.menu = MenuItem()

    def order_manager(self):
        print("1. Early Session")
        print("2. Late Session")

        try:
            Session = int(input("Enter Session: "))
            if Session in [1, 2]:
                customer = input("Enter Customer Name: ")
                diners_count = int(input("Enter Number of Diners: "))
                if 1 <= diners_count <= 8:
                    if Session == 1:
                        self.place_order_for_session(self.earlysession_tables, self.earlysession_booked_tables, "Early Session", customer, diners_count)
                    elif Session == 2:
                        self.place_order_for_session(self.latesession_tables, self.latesession_booked_tables, "Late Session", customer, diners_count)
                else:
                    print("Diners up to a maximum of eight allowed for a table")
            else:
                print("INVALID SESSION")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # ... (other methods in the Restaurant class with comments)
    def place_order_for_session(self, session_tables, booked_tables, session_name, customer, diners_count):
        try:
            self.order_fee = 0
            table_number = int(input("Table Number: "))
            if 1 <= table_number <= 6:
                if table_number not in booked_tables:
                    table = session_tables[table_number]
                    self.order_fee, tips = self.process_order(table, table_number, session_name)
                    self.complete_payment(table, booked_tables, customer, diners_count, table_number, session_name, self.order_fee, tips)
                else:
                    print(f"TABLE {table_number} ALREADY BOOKED FOR {session_name}")
            else:
                print("WRONG TABLE NUMBER")
        except ValueError:
            print("INVALID INPUT. PLEASE ENTER THE VALID NUMBER.")

    def process_order(self, table, table_number, session_name):
        order_items = {}
        order_fee = 0
        beverage_items = ["Coffee & biscuits", "Wine", "Water", "Soda"]

        print(f"Enter Order Items for {session_name} :")
        print("MENU :")
        self.menu.display_menu_items()
        while True:
            order_item = input("Enter Item or (Enter 'done' to finish): ")
            if order_item == "done":
                break

            if order_item in self.menu.menu_items:
                quantity = int(input("Quantity: "))
                order_items[order_item] = quantity

                if order_item in ["Lobster", "Steak Diane"]:
                    self.priority_orders.append(order_item)

                order_fee += self.menu.menu_items[order_item] * quantity
                self.total_income += order_fee
                self.menu.menu_popularity[order_item] += 1
                self.table_costs[table_number] = order_fee

                if order_item in beverage_items:
                    self.handle_beverage_order(table, table_number, order_item, quantity)
            else:
                print("INVALID ITEM. PLEASE SELECT FROM THE MENU.")

        table["orders"].update(order_items)
        return order_fee, 0.05 * order_fee

    def handle_beverage_order(self, table_number, table, order_item, quantity):
        cost = self.menu.menu_items[order_item] * quantity
        table["orders"][order_item] = quantity
        table["cost"] += cost
        self.total_income += cost
        self.table_costs[table_number] = self.table_costs.get(table_number, 0) + cost

    def complete_payment(self, table, booked_tables, customer, diners_count, table_number, session_name, order_fee, tips):
        print("Select Payment Method")
        print ("1. Credit/Debit Card") 
        print ("2. Cash")
        pay_method = int(input("Enter Payment Method: "))
        if pay_method == 1:
            order_fee += order_fee * 0.1
        elif pay_method != 1 or 2:
            print("WRONG PAYMENT METHOD")

        print(f"TABLE BOOKED SUCCESSFULLY FOR {session_name}, TOTAL COST: ${order_fee}")
        table["status"] = "Booked"
        table["Session"] = session_name
        table["Customer Name"] = customer
        table["Number of Diners"] = diners_count
        table["cost"] = order_fee

        self.total_amount_tips += tips
        booked_tables.append(table_number)

    def calculate_income(self):
        print(f"TOTAL INCOME: ${self.total_income:.2f}")
        print(f"TOTAL TIPS COLLECTED FROM TODAY: ${self.total_amount_tips:.2f}")

    def table_status(self):
        print("Early Session Tables 6pm - 8pm")
        self.display_tables_status(self.earlysession_tables)

        print("Late Session Tables 8pm - 10pm")
        self.display_tables_status(self.latesession_tables)

        max_table = max(self.table_costs, key=self.table_costs.get)
        print(f"TABLE {max_table} HAS THE HIGHEST COST: ${self.table_costs[max_table]:.2f}")

    def display_tables_status(self, tables):
        for i in range(1, 6):
            print(f"Table {i}", tables[i])

    def popularity_items(self):
        popularity = sorted(self.menu.menu_popularity.items(), key=lambda x: x[1], reverse=True)
        for item, count in popularity:
            print(f"{item}: {count} orders")

    def beverages(self):
        
        print("1. Early Session") 
        print("2. Late Session")
        session = int(input("Session: "))

        try:
            if session == 1:
                self.handle_beverages_for_session(self.earlysession_tables, "Early Session")
            elif session == 2:
                self.handle_beverages_for_session(self.latesession_tables, "Late Session")
            else:
                print("INVALID SESSION")
        except ValueError:
            print("INVALID INPUT. PLESASE ENTER A VALID NUMBER")

    def handle_beverages_for_session(self, session_tables, session_name):
        print(f"{session_name} Booked Tables: {self.earlysession_booked_tables}")
        table_num = int(input("Table Number: "))

        if table_num in self.earlysession_booked_tables:
            beverage_items = ["Coffee & biscuits", "Wine", "Water", "Soda"]
            for i in (beverage_items):
                print(i)
            item = input("Enter Item or (Enter 'done' to finish): ")
            while item != "done":
                if item in ["Coffee & biscuits", "Wine", "Water", "Soda"]:
                    quantity = int(input("Quantity: "))
                    cost = self.menu.menu_items[item] * quantity
                    session_tables[table_num]["orders"][item] = quantity
                    session_tables[table_num]["cost"] += cost
                    self.total_income += cost
                    self.table_costs[table_num] = self.table_costs.get(table_num, 0) + cost
                    self.menu.menu_popularity[item] += 1
                    print("BEVERAGES ADDED SUCCESSFULLY")
                    item = input("Enter Item or ('done' to finish): ")
                else:
                    print("ITEM NOT ADDED !!!")
                    break
        else:
            print("TABLE IS NOT BOOKRD YET")

    def run(self):
        # Main loop for the restaurant management system
        while True:
            print("OPTIONS: ")
            options = [
                " BOOKING YOUR TABLE",
                " TABLES STATUS / COSTS",
                " TOTAL INCOME / TIPS",
                " MENU POPULARITY ITEMS",
                " BEVERAGES",
                " EXIT"
            ]

            for i, option in enumerate(options):
                print(f"{i + 1}. {option}")

            option = input("Select Your Option               : ")
            try:
                if option == "1":
                    self.order_manager()
                elif option == "2":
                    print("TABLE STATUS / TABLE COSTS ")
                    self.table_status()
                elif option == "3":
                    print(" TOTAL INCOME / TOTAL AMOUNT OF TIPS")
                    self.calculate_income()
                elif option == "4":
                    print("MENU POPULARITY ITEMS")
                    self.popularity_items()
                elif option == "5":
                    print("ALCOHOLIC /NON-ALCOHOLIC BEVERAGES")
                    self.beverages()
                elif option == "6":
                    exit()
                else:
                    print("INVALID OPTION")
            except Exception as e:
                print(f"AN ERROR OCCURED: {str(e)}")

if __name__ == "__main__":
    # Create a Restaurant instance and start the program
    restaurant = Restaurant()
    restaurant.run()
