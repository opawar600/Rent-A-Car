from cars import carStore, Customer

def main():
    store = carStore(100)
    cust = Customer()

    while True:
        print("""
        *************************************************
        1. Show available number of cars in store
        2. Rent a Car on hourly basis for $9/hr
        3. Rent a Car on daily basis for $22/day
        4. Rent a Car on weekly basis for $100/week
        5. Return a rented Car back.
        6. Exit
        *************************************************
        """)

        choice = int(input("\nHow would you like to use our services\n"))

        if choice == 1:
            store.show_number_of_cars()


        elif choice == 2:
            # Update the rental type as 1: hourly
            cust.rentType = 1
            #print("Rent type of customer is {}".format(cust.rentType))

            # How much time would the customer rent the car? Update rental time in hours.
            n = cust.car_request()
            if n != 0:
                store.rent_hourly(n)
                hours = int(input("\nHow many hours would you like to rent the car?\n"))
                #cust.cars_rented = n
                cust.rentPeriod = hours



        elif choice == 3:
            # Update the rental type as 2: daily
            cust.rentType = 2
            #print("Rent type of customer is {}".format(cust.rentType))

            # How many days would the customer rent the car? Update rental time in days.
            n = cust.car_request()
            if n != 0:
                store.rent_daily(n)
                days = int(input("\nHow many days would you like to rent the car?\n"))
                #cust.cars.rented = n
                cust.rentPeriod = days


        elif choice == 4:
            # Update the rental type as 3: weekly
            cust.rentType = 3
            #print("Rent type of customer is {}".format(cust.rentType))

            # How many weeks would the customer rent the car? Update rental time in days.
            n = cust.car_request()
            if n != 0:
                store.rent_weekly(n)
                weeks = int(input("\nHow many weeks would you like to rent the car?\n"))
                #cust.cars.rented = n
                cust.rentPeriod = weeks


        elif choice == 5:
            # Refill the store inventory and calculate bill
            store.return_car(cust)

        else:
            print("\nThanks for your visit\n")
            exit()






if __name__ == '__main__':
    main()
