# Import functions from helper file
from helper import *

# Main
def main():

    print("""
    **************************************************
    Welcome to Rent-A-Car! How can we help?
    **************************************************
    1. Rent a car
    2. Return an already rented car
    3. Exit
    **************************************************
    """)
    flag = 1

    while flag == 1:
        case = int(input("Enter your request\n"))

        if case != 1 and case !=2 and case!=3:
            print("The input is not valid. Please enter 1 or 2")

        elif case == 1:
            cust_id = generate_cust_id() + 1
            print("\nWe have following cars available for rent")
            print("\n(Id, Name, Number of Cars Available)")
            show_available_cars()
            carType = int(input("\nEnter the Id of car that you wish to rent\n"))

            rentType = int(input("""
            How would you like to rent the car?
            1. Hourly Basis
            2. Daily Basis
            3. Weekly Basis\n"""))

            number_of_cars = int(input("""
            How many Cars do you want to rent?\n"""))

            rent_car(cust_id,number_of_cars, carType, rentType)
            show_id = generate_cust_id()
            print("""
            =============================================
            Thanks for using our services
            =============================================
            You have rented {} Car(s)
            Please remember {} as your Customer_id
            Provide this id when you return the car back.
            =============================================
            """.format(number_of_cars,show_id))

            flag = 0

        elif case == 2:
            return_car()
            flag = 0

        else:
            exit()

if __name__ == '__main__':
    main()
