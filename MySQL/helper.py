import pymysql.cursors

# Helper functions to perform various operations on carStore database and Customer database.

# Execute any sql query and return results
def query_from_database(query):
    # Make sure you include password here.
    connection = pymysql.connect(host = "localhost",user = "root", password = "*******", db = "rentacar", cursorclass = pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            connection.commit()

    finally:
        connection.close()

    return result

# Function to get number of available cars.
def show_available_cars():

    result = query_from_database("select * from carStore")

    carType = []
    carid = []
    number = []

    for i in result:
        carType.append(i["carType"])
        carid.append(i["car_id"])
        number.append(i["available_cars"])

    output = list(zip(carid,carType,number))

    for op in output:
        print(op)

# Function to generate customer id
def generate_cust_id():
    result = list(query_from_database("select count(*) from Customer"))
    return result[0]["count(*)"]

# Validate number of cars requested
def valid_car_count(n,carType):
    if n <= 0:
        print("\nPlease enter a valid car number\n")
        return False

    else:
        query = str("select available_cars from carStore where car_id = ")+ str(carType)
        result = list(query_from_database(query))[0]["available_cars"]

        if n>result:
            print("\nThe number of cars that you requested is more than available cars.\n")
            return False

        else:
            return True

# Rent Car on any basis
def rent_car(cust_id,number_of_cars, carType, rentType):
    if valid_car_count(number_of_cars, carType):
        if rentType == 1:
            rent_hourly(cust_id,number_of_cars,carType)
        elif rentType == 2:
            rent_daily(cust_id,number_of_cars,carType)
        else:
            rent_weekly(cust_id,number_of_cars,carType)

# Rent Hourly
def rent_hourly(cust_id,number_of_cars,carType):
    hours = int(input("\nHow many hours would you like to rent the car?\n"))

    query = ("insert into Customer(cust_id,car_rented,carTypeid,rentType,rentPeriod) values ({},{},{},1,{})".format(cust_id,number_of_cars,carType,hours))
    query_from_database(query)

    query_store = ("update carStore set available_cars = available_cars - {}, cars_rented = cars_rented + {} where car_id = {}".format(number_of_cars,number_of_cars,carType))
    query_from_database(query_store)

# Rent daily
def rent_daily(cust_id,number_of_cars,carType):
    days = int(input("\nHow many days would you like to rent the car?\n"))

    query = ("insert into Customer(cust_id,car_rented,carTypeid,rentType,rentPeriod) values ({},{},{},2,{})".format(cust_id,number_of_cars,carType,days))
    query_from_database(query)

    query_store = ("update carStore set available_cars = available_cars - {}, cars_rented = cars_rented + {} where car_id = {}".format(number_of_cars,number_of_cars,carType))
    query_from_database(query_store)

# Rent Weekly
def rent_weekly(cust_id,number_of_cars,carType):
    weeks = int(input("\nHow many weeks would you like to rent the car?\n"))

    query = ("insert into Customer(cust_id,car_rented,carTypeid,rentType,rentPeriod) values ({},{},{},3,{})".format(cust_id,number_of_cars,carType,weeks))
    query_from_database(query)

    query_store = ("update carStore set available_cars = available_cars - {}, cars_rented = cars_rented + {} where car_id = {}".format(number_of_cars,number_of_cars,carType))
    query_from_database(query_store)

# Function to find carPrice based on rentType
def find_car_price(price,rentType):
    if rentType == 1:
        return (((price/3)-2), "hourly" , "hours")

    elif rentType == 3:
        return ((price * 3), "weekly" , "weeks")

    else:
        return (price,"daily", "days")


# Car return back and calculate bill
def return_car():
    bill = 0

    cstid = int(input("\nEnter your unique Customer id\n"))

    validate = ("select invoice from Customer where cust_id = {}".format(cstid))
    validater = query_from_database(validate)

    if validater[0]["invoice"] != None:
        print ("\nCustomer Already Exists and Bill is already paid. Please enter active Customer id.")
        return_car()

    else:
        query = ("select * from Customer where cust_id = {}".format(cstid))
        result = query_from_database(query)

        query_store = ("select carPrice from carStore where car_id = {}".format(result[0]["carTypeid"]))
        argument = query_from_database(query_store)

        car_price,rentTypeName, noun = find_car_price(argument[0]["carPrice"],result[0]["rentType"])

        bill = car_price * result[0]["rentPeriod"] * result[0]["car_rented"]

        #Add bill to customer entry
        update_customer = ("update Customer set invoice = {} where cust_id = {}".format(bill,cstid))
        query_from_database(update_customer)

        # Replinish inventory
        update_store = ("update carStore set available_cars = available_cars + {} , cars_rented = cars_rented - {} where car_id = {}".format(result[0]["car_rented"],result[0]["car_rented"],result[0]["carTypeid"]))
        query_from_database(update_store)

        print ("""
        =============================================
        Thanks a lot for using our services
        You rented {} cars on {} basis for {} {}
        =============================================
        The total bill is $ {}
        """.format(result[0]["car_rented"],rentTypeName,result[0]["rentPeriod"],noun,bill))
