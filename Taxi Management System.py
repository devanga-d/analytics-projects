import sys
class Customer:
    def __init__(self, ID, name):
        self._ID = ID
        self._name = name
#The customers name and unique ID has been made a private attribute.

    @property
    def ID(self):
        return self._ID

    @property
    def name(self):
        return self._name
    
#The property method is used to allow the attributes to be read-only.

    def get_discount(self):
        pass

    def display_info(self):
        pass

class BasicCustomer:
    discount_rate = 0.10

    # Constructor
    def __init__(self, booking_made_before):
        self.booking_made_before = booking_made_before

# The above constructor takes the parameter and initializes the instance variable with the provided value. 

    def get_discount(self, distance_fee):
        return self.discount_rate * distance_fee

    def display_info(self):
        print("Booking made before:", self.booking_made_before)
        print("Discount rate:", self.discount_rate)

    @staticmethod
    def update_discount_rate(new_discount_rate):
        BasicCustomer.discount_rate = new_discount_rate
# We use the static method as the discount rate is a class-level attribute.

class EnterpriseCustomer:
    default_rate1 = 0.15  
    default_rate2 = 0.20  
    default_threshold = 100  

class EnterpriseCustomer:
    # Default values for rates and threshold
    def __init__(self, rate1=0.15, rate2=None, threshold=100):
        self.rate1 = rate1
        self.rate2 = rate2 if rate2 is not None else (rate1 + 0.05)
        self.threshold = threshold

# In this code, if a custom rate2 value is provided during object creation, 
# it's used, if not rate2 is calculated as rate1 + 0.05.

    # Getter method
    def get_rate1(self):
        return self.rate1

    def get_rate2(self):
        return self.rate2

    def get_threshold(self):
        return self.threshold

#The getter methods would allow access to the attributes.

#Discount Calcualtion
    def get_discount(self, distance_fee):
        if distance_fee < self.threshold:
            return self.rate1 * distance_fee
        else:
            return self.rate2 * distance_fee
#The get_discount returns the discount rate based on the distance fee
#If the distance_fee is less than the threshold, rate1 is applied, if not rate2 is applied.

    def display_info(self):
        print("Rate 1:", self.rate1)
        print("Rate 2:", self.rate2)
        print("Threshold:", self.threshold)
#The display_info prints out the values of rate1, rate2 and threshold. 

    def set_discount_rates(self, new_rate1, new_rate2):
        self.rate1 = new_rate1
        self.rate2 = new_rate2

#The set_discount_rates allows for updating the discount rates.
    def set_threshold(self, new_threshold):
        self.threshold = new_threshold

#The set_threshold allow for updating the threshold limit. 

class Location:

    def __init__(self, location_id, name):
        self.location_id = location_id
        self.name = name

    def display_info(self):
        print("Location ID:", self.location_id)
        print("Location Name:", self.name)
#The display_info method prints the values of the location_id and name attributes. 

class Rate:
    def __init__(self, rate_id, name, price_per_km):
        self.rate_id = rate_id
        self.name = name
        self.price_per_km = price_per_km

    def display_info(self):
        print("Rate ID:", self.id)
        print("Rate Type:", self.name)
        print("Price per km: $", self.price_per_km)

class Booking:
    def __init__(self, id, departure, destination, distance, rate):
        self.id = id
        self.departure = departure  
        self.destination = destination  
        self.distance = distance  
        self.rate = rate  

    def compute_cost(self):
        distance_fee = self.distance * self.rate.price_per_km

        # Calculate basic fee (minimum fee without discount)
        basic_fee = self.distance * self.rate.price_per_km

        # Calculate discount based on customer type and distance fee
        discount = self.customer.get_discount(distance_fee)

        return distance_fee, basic_fee, discount
    
#Print receipt
def print_receipt(customerName, departure, destinationList, totalDistance, Rate, distance_fee, discount, total_cost):
    print("\n------------------------------------------")
    print("Taxi Receipt")
    print("------------------------------------------")
    print(f"Name:                   {customerName}")
    print(f"Departure:              {departure}")
    print(f"Destination:            {destinationList}")
    print(f"Rate:                   {Rate._price_per_km} (AUD per km)")
    print(f"Total Distance:         {totalDistance} (km)")
    print("------------------------------------------")
    print(f"Basic fee:              {BASIC_FEE} (AUD)")
    print(f"Distance fee:           {distance_fee} (AUD)")
    print(f"Discount:               {discount} (AUD)")
    print("------------------------------------------")
    print(f"Total cost:             {total_cost} (AUD)\n")

# class Records:
#     def __init__(self):
#         self.customers = []
#         self.locations = []
#         self.rates = []

#The constructor in the records class initializes three empty lists: customers, locations, and rate_types. These lists will store the data read from input files.

    # def read_customers(self, customers):
    #     with open(customers, 'r') as customer_file:
    #         for line in customer_file:
    #             customer_data = line.strip().split(',')
    #             customer_id, name, customer_type = customer_data[:3]
    #             if customer_type == 'B':
    #                 discount_rate = float(customer_data[3])
    #                 customer = BasicCustomer(customer_id, name, discount_rate)
    #             elif customer_type == 'E':
    #                 discount_rate = float(customer_data[3])
    #                 threshold = int(customer_data[4])
    #                 customer = EnterpriseCustomer(customer_id, name, discount_rate, threshold)
    #             else:
    #                 raise ValueError("Invalid customer type")
    #             self.customers.append(customer)
                
class Records:
    def __init__(self):
        self.customers = []
        self.locations = []
        self.rates = []

    def read_customers(self, file_name):
        try:
            with open(file_name, "r") as file:
                for line in file:
                    # Split the line into individual pieces of data
                    customer_id, name, customer_type, *params = line.strip().split(",")
                    
                    # Determine customer type and create appropriate customer object
                    if customer_type == "B":  # Basic Customer
                        customer = BasicCustomer(customer_id, name)
                    elif customer_type == "E":  # Enterprise Customer
                        discount_rate, threshold = map(int, params)
                        customer = EnterpriseCustomer(customer_id, name, discount_rate, threshold)
                    else:
                        # Handle unknown customer types or raise an error as needed
                        pass
                    
                    # Add the customer object to the customers list
                    self.customers.append(customer)
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
        except Exception as e:
            print(f"An error occurred while reading customers: {e}")

    def read_locations(self, file_name):
        try:
            with open(file_name, "r") as file:
                for line in file:
                    location_id, name = line.strip().split(",")
                    location = Location(location_id, name)
                    self.locations.append(location)
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
        except Exception as e:
            print(f"An error occurred while reading locations: {e}")

    def read_rates(self, file_name):
        try:
            with open(file_name, "r") as file:
                for line in file:
                    rate_id, name, price_per_km = line.strip().split(",")
                    rate = Rate(rate_id, name, float(price_per_km))
                    self.rates.append(rate)
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
        except Exception as e:
            print(f"An error occurred while reading rates: {e}")

    def find_customer(self, search_value):
        for customer in self.customers:
            if search_value in (customer.ID, customer.name):
                return customer
        return None

    def find_location(self, search_value):
        for location in self.locations:
            if search_value in (location.location_id, location.name):
                return location
        return None

    def find_rate(self, search_value):
        for rate in self.rates:
            if search_value in (rate.rate_id, rate.name):
                return rate
        return None

    def list_customers(self):
        for customer in self.customers:
            print(f"Customer ID: {customer.ID}, Name: {customer.name}, Type: {customer.customer_type}, Discount: {customer.discount_rate*100}%")

    def list_locations(self):
        for location in self.locations:
            print(f"Location ID: {location.location_id}, Name: {location.name}")

    def list_rates(self):
        for rate in self.rates:
            print(f"Rate ID: {rate.rate_id}, Name: {rate.name}, Price per km: ${rate.price_per_km}")


#For each line in the file, it splits the line based on commas, creating a list customer_data containing customer ID, name, customer type, and rate type.
#A dictionary customer is created for each customer, where keys represent different attributes (customer ID, name, customer type, and rate type).
#The created customer dictionary is appended to the customers list.

#     def read_locations(self, locations):
#         with open(locations, 'r') as location_file:
#             for line in location_file:
#                 location_id, name = line.strip().split(',')
#                 location = Location(location_id, name)
#                 self.locations.append(location)

#     def read_rates(self, rates):
#         with open(rates, 'r') as rates_file:
#             for line in rates_file:
#                 rate_id, name, price_per_km = line.strip().split(',')
#                 rate = Rate(rate_id, name, float(price_per_km))
#                 self.rates.append(rate)

# #The same process is repeated for the other files

#     def find_customer(self, ID):
#         for customer in self.id:
#             if id in (customer.ID):
#                 return customer
#         return None

# # This method searches for a customer ID in the list of customers (self.customers) based on the given search_value. The search_value is the customer ID.
# #It iterates through the list of customers and checks if the search_value matches either the customer's ID.
# #If a match is found, the method returns the corresponding customer object.
# ###CHECK THIS########

#     def find_location(self, location):
#         for location in self.locations:
#             if location in (location.location_id, location.name):
#                 return location
#         return None

#     def find_rate(self, rates):
#         for rate in self.rates:
#             if rates in (rate.rate_id, rate.name):
#                 return rate
#         return None

# #Same process is repeated for the other classes.

#     def list_customers(self):
#         for customer in self.customers:
#             print(f"Customer ID: {customer.ID}, Name: {customer.name}, Type: {customer.customer_type}, Discount: {customer.discount_rate*100}%")
    
# This method prints information about all customers stored in self.customers.
# It iterates through the list of customers and prints their ID, name, customer type, and discount rate (converted from decimal to percentage).
    # def list_locations(self):
    #     for location in self.locations:
    #         print(f"Location ID: {location.location_id}, Name: {location.name}")

    # def list_rates(self):
    #     for rate in self.rates:
    #         print(f"Rate ID: {rate.rate_id}, Name: {rate.name}, Price per km: ${rate.price_per_km}")

# class Operations:
#     def __init__(self):
#         # Initialize data collections and read data from files if available
#         self.records = Records()  # Assuming you have a Records class to manage customer, location, and rate data
#         self.records.read_customers("customers.txt")
#         self.records.read_locations("locations.txt")
#         self.records.read_rate_types("rates.txt")

#     def display_menu(self):
#         while True:
#             print("\nMenu:")
#             print("1. Book a trip")
#             print("2. Display existing customers")
#             print("3. Display existing locations")
#             print("4. Display existing rate types")
#             print("5. Exit")
#             choice = input("Enter your choice: ")

#             if choice == "1":
#                 self.book_trip()
#             elif choice == "2":
#                 self.records.list_customers()
#             elif choice == "3":
#                 self.records.list_locations()
#             elif choice == "4":
#                 self.records.list_rates()
#             elif choice == "5":
#                 print("Exiting the program. Goodbye!")
#                 break
#             else:
#                 print("Invalid choice. Please try again.")

#     def book_trip(self):
#         # Assume you have methods to handle booking functionality and creating Booking objects
#         # Get customer, location, rate type, and distance inputs from the user
#         # Create a Booking object and calculate costs
#         # Display the receipt as specified in the requirements
#         # Add the customer data if it's a new customer

#         # Example code (assuming Booking and Customer classes are defined)
#         customer_name = input("Enter customer name: ")
#         location_name = input("Enter departure location: ")
#         rate_type_name = input("Enter rate type: ")
#         distance = float(input("Enter distance (in km): "))

#         customer = self.records.find_customer(customer_name)
#         location = self.records.find_location(location_name)
#         rate_type = self.records.find_rate(rate_type_name)

#         if customer is None:
#             print("Customer not found. Please add customer information.")
#             # Get additional customer information and create a new Customer object
#             # customer = Customer(...)
#             # Add customer to records: self.records.customers.append(customer)

#         if location is None or rate_type is None:
#             print("Invalid location or rate type. Please check your input.")
#             return

#         # Calculate costs, create a Booking object, and display the receipt
#         # booking = Booking(customer, location, rate_type, distance)
#         # booking.calculate_costs()
#         # booking.display_receipt()

#         print("Booking completed!")

# # Assuming Records, Customer, Location, Rate, and Booking classes are defined
# # Initialize and run the menu
# operations = Operations()
# operations.display_menu()

class Operations:
    
    
    # def __init__(self):
    #     # Initialize data collections and read data from files if available
    #     self.records = Records()  # Assuming you have a Records class to manage customer, location, and rate data
    #     self.records.read_customers("customers.txt")
    #     self.records.read_locations("locations.txt")
    #     self.records.read_rate_types("rates.txt")

    def display_menu(self):
        while True:
            print("\nMenu:")
            print("1. Book a trip")
            print("2. Display existing customers")
            print("3. Display existing locations")
            print("4. Display existing rate types")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.book_trip()
            elif choice == "2":
                self.records.list_customers()
            elif choice == "3":
                self.records.list_locations()
            elif choice == "4":
                self.records.list_rates()
            elif choice == "5":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def book_trip(self):
        customer_name = input("Enter customer name: ")
        location_name = input("Enter departure location: ")
        rate_type_name = input("Enter rate type: ")
        distance = float(input("Enter distance (in km): "))

        customer = self.records.find_customer(customer_name)
        location = self.records.find_location(location_name)
        rate_type = self.records.find_rate(rate_type_name)

        if customer is None:
            print("Customer not found. Please add customer information.")
            # Get additional customer information and create a new Customer object
            # customer = Customer(...)  # Create the appropriate customer object based on user input
            # Add customer to records: self.records.customers.append(customer)

        if location is None or rate_type is None:
            print("Invalid location or rate type. Please check your input.")
            return

        # Calculate costs, create a Booking object, and display the receipt
        # booking = Booking(customer, location, rate_type, distance)
        # booking.calculate_costs()
        # booking.display_receipt()

        print("Booking completed!")


