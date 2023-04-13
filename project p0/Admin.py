import mysql.connector as connector
import datetime as date
class Admin :

    dates1 = date.datetime.now()
    admin = 'ADMIN'
    password = 'admin12'
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     user='root',
                                     password='sql21',
                                     database='SDbank')

    def showall_customers(self):
            query = "select * from customers"
            cur = self.con.cursor()
            cur.execute(query)
            for row in cur:
                print("Account number  : ", row[0])
                print("name  : ", row[1])
                print("phone number  : ", row[2])
                print("DOB  : ", row[3])
                print("Address  : ", row[4])
                print("balance   : ", row[5])
                print()
                print()

    def find_customer(self, account_no):
            query = "select * from customers where account_no='{}'".format(account_no)

            cur = self.con.cursor()

            cur.execute(query)
            for row in cur:
                print("Account number  : ", row[0])
                print("name  : ", row[1])
                print("phone number  : ", row[2])
                print("DOB  : ", row[3])
                print("Address  : ", row[4])
                print(" balance   : ", row[5])
                print()
                print()

    def delete_customer(self, account_no):
            query = "delete from customers where account_no = {}".format(account_no)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("Customer Deleted successfully at  ", self.dates1)
            print()

    def update_customer(self, account_no, newName, newphone, newaddress):
            query = "update customers set name = '{}' , phone = {} , Address = '{}' where account_no = {} ".format(
                newName, newphone, newaddress, account_no)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("Customer updated at ", self.dates1)

    def deleteAllcustomers(self):
            query = "delete from customers"
            curr = self.con.cursor()
            curr.execute(query)
            self.con.commit()
            print('All customers deleted at ', self.dates1)