# Rent-A-Car

### Object Oriented Approach

In this project, we develop a python based project implementing object oriented programming and integrate it with MySQL Relational Database System. We develop a Car Rental System where a customer can rent a car from a car store on three different basis.

* Hourly:  ($9/hr)
* Daily:   ($22/day)
* Weekly:  ($100/week)

### Classes
There are two classes in this system.
* CarStore
> Here we maintain our inventory records and number of cars available to rent. Store can rent car on hourly, daily and weekly basis. The number of cars that a customer requests must be less than available cars in the store. Also, store has to issue a bill to the customer when the rented car is returned back.
* Customer
> Customer can request a car for rent from the store. He can rent a car on all three basis listed above. For the simplicity of the system, one customer can rent cars on only one basis at a time. Customers get a bill from the store for the rented cars.

### Files
* cars.py
Has all the functions related to carStore and Customer.
* main.py
Main python file built on top of cars.py to give the user access to the Car Rental System.

### Python
2.7.16.
Execute

> python main.py


or

> python3 main.py

This is approach to understand how OOP concepts work. But once we terminate the program, all the data is lost.
Hence to store the data somewhere, we also implemented the same concept different approach.

Refer to MySQL folder to see the same problem implemented using MySQL Database.


