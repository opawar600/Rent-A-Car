# Define a class for the car store

class carStore:

    # Initialize the store with number of cars available
    def __init__(self , number_of_cars = 0):
        self.available_cars = number_of_cars

    def valid_car_count(self,n):
        if n <= 0:
            print("Please enter a valid car number")
            return False

        elif n > self.available_cars:
            print("The number of cars that you requested is more than available cars.")
            return False
        else:
            return True

    # See how many cars are available in store
    def show_number_of_cars(self):
        print("Thanks for checking upon carRentals. \nCurrently we have {} cars available to rent".format(self.available_cars))

    # Rent car on hourly basis
    def rent_hourly(self, required_cars):
        # Check if the number of cars specified is valid
        if self.valid_car_count(required_cars):
            print("You have rented {} Car(s) on hourly basis".format(required_cars))
            print("You will be charged $9 per hour for each car.")
            self.available_cars -= required_cars

    # Rent car on daily basis
    def rent_daily(self, required_cars):
        if self.valid_car_count(required_cars):
            print("You have rented {} Car(s) on daily basis".format(required_cars))
            print("You will be charged $22 per day for each car.")
            self.available_cars -= required_cars

    # Rent car on weekly basis
    def rent_weekly(self, required_cars):
        if self.valid_car_count(required_cars):
            print("You have rented {} Car(s) on weekly basis".format(required_cars))
            print("You will be charged $100 per week for each car.")
            self.available_cars -= required_cars

    # When the car is returned back
    #def return_car(self, car_rent_details)


class Customer:

    # Initialize Customer details
    def __init__(self):
        # Total number of cars rented by the Customer
        self.cars_rented = 0
        # Type of rental: hourly is 1, daily is 2 and weekly is 3
        self.rentType = 0
        # Amount of time car rented. Hours, days or weeks repectively
        self.rentPeriod = 0
        # Invoice to be paid
        self.invoice = 0

    # Make request to the store
    def car_request(self):
        n = int(input("Enter the number of cars you wish to rent"))

        if n < 1:
            print ("Please enter a valid number of cars you want to rent")
        else:
            self.cars_rented = n
            print("Thank you! You will get {} Car(s) as per your request".format(n))



    # Return car back to the store
    def car_return(self):

        if self.cars_rented and self.rentType and self.rentPeriod:
            return self.cars_rented, self.rentType, self.rentPeriod
        else:
            return 0,0,0
