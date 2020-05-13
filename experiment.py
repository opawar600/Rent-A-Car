from cars import carStore, Customer
import pymysql

def find_next_custid():

    connection = pymysql.connect(host = "localhost",user = "root", password = "root1234", db = "rentacar", cursorclass = pymysql.cursors.DictCursor)
    sqlQuery = "select count(*) from Customer"
    try:
        with connection.cursor() as cursor:
            csid = cursor.execute(sqlQuery)
            print(csid)
            connection.commit()

    finally:
        connection.close()
    print(csid)
    return csid


def main():
    store = carStore(100)

    print ("Welcome to Rent-A-Car! \nWe have {} Cars available to rent".format(store.available_cars))
    rentorreturn = int(input("I would like to: \n(1)Rent a car \n(2)Return back rented car?"))

    if rentorreturn == 1:
        cust_id = find_next_custid()
        print(cust_id)
        cust = Customer(int(cust_id))
        # Ask customer how would he like to rent a car
        choice = int(input("I want to rent the car on\n(1) Hourly Basis\n(2) Daily Basis\n(3) Weekly Basis"))

        if choice == 1:
            # Update customer rental Type
            cust.rentType = 1 # Type 1 is hourly Basis

            # How much time would the customer rent the car? Update rental time in hours.
            n = cust.car_request()

            if n != 0:
                store.rent_hourly(n)
                hours = int(input("\nHow many hours would you like to rent the car?\n"))
                cust.rentPeriod = hours
                # Add customer details to
                cust.add_customer_to_database()

        elif choice == 2:
            # Update customer rental Type
            cust.rentType = 2 # Type 1 is hourly Basis

            # How much time would the customer rent the car? Update rental time in hours.
            n = cust.car_request()

            if n != 0:
                store.rent_daily(n)
                days = int(input("\nHow many days would you like to rent the car?\n"))
                cust.rentPeriod = days
                # Add customer details to
                cust.add_customer_to_database()

        elif choice == 3:
            # Update customer rental Type
            cust.rentType = 3 # Type 1 is hourly Basis

            # How much time would the customer rent the car? Update rental time in hours.
            n = cust.car_request()

            if n != 0:
                store.rent_daily(n)
                weeks = int(input("\nHow many weeks would you like to rent the car?\n"))
                cust.rentPeriod = weeks
                # Add customer details to
                cust.add_customer_to_database()

        else:
            print("\nEnter valid request. \nPlease enter your request in form of the number")



if __name__ == '__main__':
    main()
