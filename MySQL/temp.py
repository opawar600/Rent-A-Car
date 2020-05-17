import pymysql.cursors

# Execute any sql query and return results
def query_from_database(query):
    connection = pymysql.connect(host = "localhost",user = "root", password = "root1234", db = "rentacar", cursorclass = pymysql.cursors.DictCursor)

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
    number = []

    for i in result:
        carType.append(i["carType"])
        number.append(i["available_cars"])

    print(list(zip(carType,number)))

# Fucntion to generate customer id
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
            rent_hourly(cust_id, number_of_cars,carType)
        elif rentType == 2:
            rent_daily(cust_id, number_of_cars,carType)
        else:
            rent_weekly(cust_id, number_of_cars,carType)

# Rent Hourly
def rent_hourly(cust_id, number_of_cars,carType):
    hours = int(input("\nHow many hours would you like to rent the car?\n"))

    query = ("insert into Customer(cust_id,car_rented,carTypeid,rentType,rentPeriod) values ({},{},{},1,{})".format(cust_id,number_of_cars,carType,hours))
    query_from_database(query)

    query_store = ("update carStore set available_cars = available_cars - {}, cars_rented = cars_rented + {} where car_id = {}".format(number_of_cars,number_of_cars,carType))
    query_from_database(query_store)

# Rent daily
def rent_daily(cust_id, number_of_cars,carType):
    days = int(input("\nHow many days would you like to rent the car?\n"))

    query = ("insert into Customer(cust_id,car_rented,carTypeid,rentType,rentPeriod) values ({},{},{},2,{})".format(cust_id,number_of_cars,carType,days))
    query_from_database(query)

    query_store = ("update carStore set available_cars = available_cars - {}, cars_rented = cars_rented + {} where car_id = {}".format(number_of_cars,number_of_cars,carType))
    query_from_database(query_store)

# Rent Weekly
def rent_weekly(cust_id, number_of_cars,carType):
    weeks = int(input("\nHow many weeks would you like to rent the car?\n"))

    query = ("insert into Customer(cust_id,car_rented,carTypeid,rentType,rentPeriod) values ({},{},{},3,{})".format(cust_id,number_of_cars,carType,weeks))
    query_from_database(query)

    query_store = ("update carStore set available_cars = available_cars - {}, cars_rented = cars_rented + {} where car_id = {}".format(number_of_cars,number_of_cars,carType))
    query_from_database(query_store)


# Car return back
def
# Calculate Bill amount