# Rent-A-Car

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
* experiment.py
This file is built on top of main.py to connect database to our code. In the database, we need a customer table which has customer id(cust_id), cars_rented, rentType, rentPeriod and invoice. 
We use *MySQL* server as a database management system. 
To connect MySQL to python script, we use *pymsql* 

### Python
2.7.16. 
Execute

> python main.py

> python experiment.py

or

> python3 main.py

> python experiment.py

### MySQL
8.0.20 

> use database_name

> create table Customer (cust_id INT, cars_rented INT, rentType INT, rentPeriod INT, invoice INT)

### PyMySQL

> pip install pymysql

OR

> pip3 install pymysql

[References](https://medium.com/@gurupratap.matharu/object-oriented-programming-project-in-python-for-your-github-portfolio-d34feaf1332c)
