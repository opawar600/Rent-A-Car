# Define a class for the car store

class carStore:

    # Initialize the store with number of cars available
    def __init__(self , number_of_cars = 0):
        self.available_cars = number_of_cars

    # See how many cars are available in store
    def show_number_of_cars(self):
        print("Thanks for checking upon carRentals. \nCurrently we have {} cars available to rent".format(self.available_cars))

    # Rent car on hourly basis
    def rent_hourly(self, required_cars):
        # Check if the number of cars specified is valid
        if required_cars <= 0:
            print("Please enter a valid car number")
        elif required_cars > self.available_cars:
            print("The number of cars that you requested is more than available cars.")
        else:
            print("You have rented {} Car(s) on hourly basis".format(required_cars))
            print("You will be charged $25 per hour for each car.")
            self.available_cars -= required_cars

    # Rent car on daily basis
    #def rent_daily(self, required_cars)

    # Rent car on weekly basis
    #def rent_weekly(self, required_cars)

    # When the car is returned back
    #def return_car(self, car_rent_details)


#class Customer:

    # Initialize Customer details
    #def __init(self)

    # Make request to the store
    #def car_request(self)

    # Return car back to the store
    #def car_return(self)

store = carStore(100)
store.show_number_of_cars()
n = input("Enter number of cars that you want to rent")
store.rent_hourly(n)
store.show_number_of_cars()
