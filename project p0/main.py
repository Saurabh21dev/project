from User import DBHelpher
from Admin import Admin

def main() :
      print()
      print("  WELCOME TO  ", DBHelpher.Bank_name)
      helpher = DBHelpher()
      admin = Admin()
      print()
      inp = input("please enter admin or user  ")

      if inp == 'user' :
       while True :

          print()
          print("Enter 1 to create an new account ")
          print("Enter 2 to display your account details  ")
          print("Enter 3 to delete your accountad  ")
          print("Enter 4 to update  your account  ")
          print("Enter 5 to deposit to an account  ")
          print("Enter 6 to withdrawn from   an  account ")
          print("Enter 7 to complete an transactions ")
          print()

          try :
              choice = int(input())
              if choice == 1:

                  name = input('please enter your name : ')
                  while True :
                    phone = int(input('enter your phone number : '))
                    if len(str(phone)) > 10 or len(str(phone)) < 10 :
                      print("Invalid phone number ! please enter 10 digit only ")
                    else :
                        break
                  DOB = input('please enter you date of birth ')
                  Address = input('enter your address : ')
                  while True :
                     opening_bal = int(input("please enter your opening balance : "))
                     if opening_bal <= 0 :
                         print('opening balance cant be zero ')
                     else :
                         break

                  while True :
                    password = input('please enter password ')
                    if len(str(password)) <= 5 or len(str(password)) >= 18 :
                        print("Enter passwword greater than 5 and less than 18 char ")
                    else : break

                  helpher.create(name,phone,DOB,Address,opening_bal,password)

              elif choice == 2 :
                  while True :
                    cus = int(input("please enter your account number to fetch your  information : "))
                    if cus == None:
                         print('Wrong Account number ! check again')
                    else :
                        helpher.find_customer(cus)
                        break
                    # helpher.find_customer(cus)

              elif choice == 3 :
                  cus = int(input("please enter an account number to delete your account : "))
                  helpher.delete_customer(cus)

              elif choice == 4 :
                  cid = int(input("please enter account number to update your details "))
                  newname = input("please enter new name ")

                  while True :
                    newphone = int(input('enter your phone number : '))
                    if len(str(newphone)) > 10 or len(str(newphone)) < 10 :
                      print("Invalid phone number ! please enter 10 digit only ")
                    else : break
                  newaddress = input("enter new address : ")
                  helpher.update_customer(cid,newname,newphone,newaddress)

              elif choice == 5 :
                  acc_no = int(input("please enter your account number to deposit "))
                  amt = int(input('please enter amount you want to deposit '))
                  helpher.deposit(amt , acc_no)

              elif choice == 6 :
                  acc_no = int(input("please enter your account number to withdrawn "))
                  amt = int(input('please enter amount you want to withdrawn '))
                  helpher.withdrawn(amt,acc_no)

              # elif choice == 8 :
              #     helpher.deleteAllcustomers()

              elif choice == 7 :
                  print('Thank you for using SDBANK  ! Welcome back ')
                  break
              else :
                  print("Invalid input ! try again  ")
          except Exception as e :
              print(e)
              print('Invalid details ! Try again ')

      elif inp == 'admin' :
       while True:
          username = input('please enter username : ')
          password = input('pleasse enter password')
          if username != admin.admin and password != admin.password:
              print("please enter correct credentials ")
              break
          else :

           while True :
             print()
             print("Enter 1 to display  all customers  ")
             print("Enter 2 to display a specific customer  ")
             print("Enter 3 to delete an  account ")
             print("Enter 4 to update  an  account ")
             print("Enter 5 to delete all customers ")
             print("Enter 6 to complete an transactions ")
             print()
             try :
                choice = int(input('please enter your choice'))

                if choice == 1:
                   admin.showall_customers()
                elif choice == 2 :
                   inp = int(input("please enter account number to fetch customer details : "))
                   admin.find_customer(inp)
                elif choice == 3 :
                   inp = int(input("please enter account number to delete customer  : "))
                   admin.delete_customer(inp)
                elif choice == 4 :
                   cid = int(input("please enter account number to update your details "))
                   newname = input("please enter new name ")

                   while True :
                      newphone = int(input('enter your phone number : '))
                      if len(str(newphone)) > 10 or len(str(newphone)) < 10:
                        print("Invalid phone number ! please enter 10 digit only ")
                      else:
                         break
                   newaddress = input("enter new address : ")
                   admin.update_customer(cid,newname,newphone,newaddress)
                elif choice == 5:
                   admin.deleteAllcustomers()
                elif choice == 6 :
                   print("Thank you admin ! see you soon ")
                   break
                else :
                   print("Invalid input ! try again ")
             except Exception as e :
               print(e)
               print("invalid details ! try again ")

















if __name__ == "__main__" :
    main()