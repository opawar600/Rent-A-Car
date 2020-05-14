from cars import carStore, Customer
import pymysql

def find_next_custid():

    connection = pymysql.connect(host = "localhost",user = "root", password = "root1234", db = "rentacar", cursorclass = pymysql.cursors.DictCursor)
    sqlQuery = "select count(*) from Customer"
    try:
        with connection.cursor() as cursor:
            cursor.execute(sqlQuery)
            csid = (cursor.fetchone())
    finally:
        connection.close()

    return csid["count(*)"]

# Function to generate bill and add the details to dataset. Takes cust_id for which the bill is to be Calculated and carStore object.
def generate_invoice(custid,store_temp):
    connection = pymysql.connect(host = "localhost",user = "root", password = "root1234", db = "rentacar", cursorclass = pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sqlQuery = "select * from Customer where cust_id = %s"
            cursor.execute(sqlQuery,(int(custid)))
            obj = (cursor.fetchone())

            cust_temp = Customer(100) # Create a temporary object to use functions from cars.py
            cust_temp.rentType = obj["rentType"]
            cust_temp.rentPeriod = obj["rentPeriod"]
            cust_temp.cars_rented = obj["cars_rented"]

            bill = store_temp.return_car(cust_temp)

            sqlQuery2 = "update Customer set invoice = %s where cust_id = %s"
            cursor.execute(sqlQuery2,(int(bill),int(custid)))
            connection.commit()
    finally:
        connection.close()

def main():
    store = carStore(100)

    print ("Welcome to Rent-A-Car! \nWe have {} Cars available to rent".format(store.available_cars))
    rentorreturn = int(input("I would like to: \n(1)Rent a car \n(2)Return back rented car?"))

    if rentorreturn == 1:
        cust_id = find_next_custid()
        #print(cust_id)
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


    elif rentorreturn == 2:
        print("\nThanks for using our service.")
        bill_for_cust = int(input("\nEnter the id provided to you when you rented the car"))
        generate_invoice(bill_for_cust,store)




if __name__ == '__main__':
    main()
