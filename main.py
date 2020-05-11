from cars import carStore, Customer

def main():
    store = carStore(100)
    cust = Customer()

    while True:
        print("""
        *************************************************
        1. Show available number of cars in store
        2. Rent a Car on daily basis for $9/hr
        *************************************************
        """)

        choice = int(input("How would you like to use our services"))

        if choice == 1:
            store.show_number_of_cars()

        elif choice == 2:
            # Update the rental type as 1: hourly
            cust.rentType = 1

            # How much time would the customer rent the car? Update rental time in hours.
            hours = int(input("How many hours would you like to rent the car?"))
            cust.rentPeriod = hours



if __name__ == '__main__':
    main()
