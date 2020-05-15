
# Define global variables for rent for each type of rental basis

rent_per_hour = int(9)
rent_per_day = int(22)
rent_per_week = int(100)

# Define a class for the car store

class carStore:

    # Initialize the store with number of cars available
    def __init__(self , number_of_cars = 0):
        self.available_cars = number_of_cars

    # Validate the car numbers entered
    def valid_car_count(self,n):
        if n <= 0:
            print("\nPlease enter a valid car number\n")
            return False

        elif n > self.available_cars:
            print("\nThe number of cars that you requested is more than available cars.\n")
            exit()
            return False
        else:
            return True

    # See how many cars are available in store
    def show_number_of_cars(self):
        print("\nThanks for checking upon carRentals. \nCurrently we have {} cars available to rent\n".format(self.available_cars))

    # Rent car on hourly basis
    def rent_hourly(self, required_cars):
        # Check if the number of cars specified is valid
        if self.valid_car_count(required_cars):
            print("\nYou have rented {} Car(s) on hourly basis\n".format(required_cars))
            print("\nYou will be charged ${} per hour for each car.\n".format(rent_per_hour))
            # Update cars count in inventory
            self.available_cars -= required_cars

    # Rent car on daily basis
    def rent_daily(self, required_cars):
        if self.valid_car_count(required_cars):
            print("\nYou have rented {} Car(s) on daily basis\n".format(required_cars))
            print("\nYou will be charged ${} per day for each car.\n".format(rent_per_day))
            # Update cars count in inventory
            self.available_cars -= required_cars

    # Rent car on weekly basis
    def rent_weekly(self, required_cars):
        if self.valid_car_count(required_cars):
            print("\nYou have rented {} Car(s) on weekly basis\n".format(required_cars))
            print("\nYou will be charged ${} per week for each car.\n".format(rent_per_week))
            # Update cars count in inventory
            self.available_cars -= required_cars

    # When the car is returned back
    def return_car(self, customer_details):
        # Fill the inventory
        self.available_cars += customer_details.cars_rented

        # Calculate the bill
        bill = 0
        if customer_details.rentType == 1:
            # Calculate bill amount
            bill = (customer_details.cars_rented * customer_details.rentPeriod * rent_per_hour)
            print("\nYou had rented {} car(s) on hourly basis".format(customer_details.cars_rented))
            print("\nYour bill is {}".format(bill))

        elif customer_details.rentType == 2:
            # Calculate bill amount
            bill = (customer_details.cars_rented * customer_details.rentPeriod * rent_per_day)
            print("\nYou had rented {} car(s) on weekly basis".format(customer_details.cars_rented))
            print("\nYour bill is {}".format(bill))

        elif customer_details.rentType == 3:
            # Calculate bill amount
            bill = (customer_details.cars_rented * customer_details.rentPeriod * rent_per_week)
            print("\nYou had rented {} car(s) on weekly basis".format(customer_details.cars_rented))
            print("\nYour bill is ${}".format(bill))

        customer_details.invoice = bill
        customer_details.car_return()
        return bill



class Customer:

    # Initialize Customer details
    def __init__(self,id = 0):
        # Total number of cars rented by the Customer
        self.cars_rented = 0
        # Type of rental: hourly is 1, daily is 2 and weekly is 3
        self.rentType = 0
        # Amount of time car rented. Hours, days or weeks repectively
        self.rentPeriod = 0
        # Invoice to be paid
        self.invoice = 0

    # Make request to the store and return number of requested cars
    # Takes an object of carStore to update the carStore inventory
    def car_request(self):
        n = int(input("\nEnter the number of cars you wish to rent\n"))

        if n < 1:
            print ("\nPlease enter a valid number of cars you want to rent\n")
            return 0
        else:
            # update the number of cars rented by customer
            self.cars_rented = n
            return n


    # Return car back to the store
    def car_return(self):

        if self.cars_rented and self.rentType and self.rentPeriod:
            return self.cars_rented, self.rentType, self.rentPeriod
        else:
            return 0,0,0
