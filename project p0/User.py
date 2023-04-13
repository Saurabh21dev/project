import mysql.connector as connector
import datetime as date
# dates1 = date.datetime.now()

class DBHelpher :

    dates1 = date.datetime.now()

    Bank_name = "SDBANK "
    def __init__(self):

        self.con = connector.connect(host='localhost',
                                     user='root',
                                     password='sql21',
                                     database='SDbank')
        self.cus_list = []
        self.loggedin = False
    def create(self,name ,phone ,DOB , Address,Balance ,password ):
        query = "insert into customers(name,phone,DOB,Address,Balance,password)values('{}',{},'{}','{}',{},'{}')".format(name,phone,DOB,Address,Balance,password)
        # print(query)
        curr = self.con.cursor()
        curr.execute(query)
        self.con.commit()
        print("Account created  successfully at  " , self.dates1)
        self.cus_list = [name , password]
    def all_customers(self):
        query = "select * from customers"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur :
            print("Account number  : " , row[0])
            print("name  : ", row[1])
            print("phone number  : ", row[2])
            print("DOB  : ", row[3])
            print("Address  : ", row[4])
            print("balance   : ", row[5])
            print()
            print()
    def find_customer(self,account_no):
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
    def delete_customer(self,account_no):
        query = "delete from customers where account_no = {}".format(account_no)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Your Account is deleted Successfully at  " , self.dates1)
        print()
    def update_customer(self,account_no ,newName , newphone, newaddress):
        query = "update customers set name = '{}' , phone = {} , Address = '{}' where account_no = {} ".format(newName,newphone,newaddress,account_no)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Account updated at " , self.dates1)

    def login(self,name , password):
        if name in str(self.cus_list):
            if str(password) in str(self.cus_list):
                self.loggedin = True
        if self.loggedin == True :
            print(f"{name} welcome back ! you loggined in back at ",  self.dates1)
        else :
            print('wrong details ')

    def deposit(self,amount , acc_no):
        q = 'select Balance from customers where account_no = {}'.format(acc_no)
        curr = self.con.cursor()
        curr.execute(q)
        res = curr.fetchone()
        total = int(res[0]) + amount
        query = 'update customers set Balance = {}  where account_no = {}'.format(total , acc_no)
        curr = self.con.cursor()
        curr.execute(query)
        self.con.commit()
        print("Amount deposited "  , " at " , self.dates1)

    def withdrawn(self,amount ,acc_no):
        q = 'select Balance from customers where account_no = {}'.format(acc_no)
        curr = self.con.cursor()
        curr.execute(q)
        res = curr.fetchone()
        total = 0
        trans = True
        if int(res[0]) <= amount:
            print("you dont have sufficient balance ")
            trans = False
        else :
            total = int(res[0]) - amount
            query = 'update customers set Balance = {}  where account_no = {}'.format(total, acc_no)
            curr = self.con.cursor()
            curr.execute(query)
            self.con.commit()
            print("Amount withdrawn  " ,  "at" , self.dates1)
    def deleteAllcustomers(self):
        query = "delete from customers"
        curr = self.con.cursor()
        curr.execute(query)
        self.con.commit()
        print('All customers deleted at ' , self.dates1)


    # def transaction(self):