
from datetime import datetime 
from datetime import date
cid=date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

import sqlite3
import hashlib


# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the 'users' table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')
conn.commit()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup():
    global name
    print("\n\n===================================================================")
    print("                   S I G N U P                                       ")
    print("====================================================================")
    print("\nKindly fill in the following details")

    while True:
        name = input("\nEnter name : ")
        if len(name) != 0:
            break
    
    phone = input("\nEnter your phone number: ")
    while len(phone) != 10 or not phone.isdigit():
        print("Enter valid phone number")
        phone = input("Enter your phone number: ")
    print("Phone number verified")

    email = input("\nEnter email id: ")
    while not ("@" in email and ".com" in email and email == email.lower() and len(email) <= 20):
        print("Invalid email-id")
        email = input("\nEnter email id: ")
    print("Email id verified")

    password = input("Enter password: ")
    hashed_password = hash_password(password)

    # Insert the user details into the database
    try:
        cursor.execute("INSERT INTO users (name, phone, email, password) VALUES (?, ?, ?, ?)", 
                       (name, phone, email, hashed_password))
        conn.commit()
        print("Signup successful!")
    except sqlite3.IntegrityError:
        print("This email is already registered!")
    while True:
                    ppl=int(input("Enter the number of guests per room:"))
                    if ppl>5:
                        print("Only a maximum of 5 guests can stay in a room")
                        continue
                        
                    if ppl<1:
                        print("Atleast one guest ahould accomadate a room:")
                        continue
                    else:
                        print('Thanks for filling the details')
                        break
   

def loginUser():
    global name
    print("\n\n===================================================================")
    print("                   L O G I N                                         ")
    print("====================================================================")
    
    email = input("\nEnter your email id: ")
    password = input("Enter your password: ")
    hashed_password = hash_password(password)

    # Validate the credentials
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, hashed_password))
    user = cursor.fetchone()
    
    if user:
        name = user[0]
        print("Login successful!")

    else:
        print("Invalid email or password.")
        main_menu()
    while True:
                    ppl=int(input("Enter the number of guests per room:"))
                    if ppl>5:
                        print("Only a maximum of 5 guests can stay in a room")
                        continue
                        
                    if ppl<1:
                        print("Atleast one guest ahould accomadate a room:")
                        continue
                    else:
                        print('Thanks for filling the details')
                        break


print("")
print("OoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoO")
print("")
print('''                           PEARL VALLEY RESORTS - MALDIVES
                                             WELCOMES YOU
       ''')
print("OoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoO")

def captcha():
                import random
                global c
                c = 0
                print("Human verification\n")
                while True:
                    y=random.randrange(100000,900000)
                    print(y)
                    z=int(input("Enter the given number:"))
                    if z==y:
                        c=True
                        print("Verified !")
                        break
                    elif z!=y:
                        print("You have entered the wrong pin,try again!")
                        c+=1
                        if c==2:
                            c=False
                            print("Your verification failed")
                            break
                        
def main_menu():
    
    global loginFlag
    while True:
           print("=============MAIN MENU=============")     
           print("|---------------------------------|")
           print("|S.no|      Option                |")
           print("|----|----------------------------|")
           print("| 1  |     Admin                  |")
           print("| 2  |     Customer               |")
           print("| 3  |     Exit                   |")
           print("|=================================|")
           c=input("Enter your choice : ")
           print()
           if c=='3':
               break
           if c=='1':

                global uname
                email = "ilakiya@gmail.com"
                mobile = "912345678"
                uname=input("Enter username : ")
                pwd=input("Enter password : ")
                if uname=="ilakiya" and pwd=="raghavi":
                    print("Logged in Successfully")
                    print('\n')
                    print("Welcome Admin")
                    login=True
                    
                    while True:
                            print("1. View user details")
                            print("2. Logout")
                            choice = int(input(" Enter your choice:"))
                            
                            if choice==1:
                
                                print("Username: " + uname)
                                print("Mobile  : " + mobile)
                                print("Email   : " + email)
                            if choice==2:
                                break
                else:
                    print("Invalid Credentials!")
                    main_menu()
           
           if c=='2':
            isNewUser = int(input("1.Login\n2.SignUp\nEnter your choice: "))
            if isNewUser == 2:
               captcha()
               signup()
            elif isNewUser == 1:
               loginFlag = True
               loginUser()
            else:
               print("Invalid choice")
               main_menu()
            
            

            def pool():
                 ask=input('1-Gym\n2-Swimming pool\nWhat would you like to choose: ')

                 if ask == "1":
                   print("============GYM TIMINGS===========")     
                   print("|--------------------------------|")
                   print("|S.no      Days        Timings(pm)")
                   print("|----|---------------------------|")
                   print("| 1  |     Monday      |3:00-8:00|")
                   print("| 2  |     Tuesday     |3:00-8:00|")
                   print("| 3  |     Wednesday   |3:00-8:00|")
                   print("| 4  |     Thursday    |3:00-8:00|")
                   print("| 5  |     Friday      |3:00-8:00|")
                   print("| 6  |     Saturday    |3:00-8:00|")
                   print("| 7  |     Sunday      |3:00-8:00|")
                   print("|================================|")
                   print("1-Monday,2-Tuesday,3-Wednesday,4-Thursday,5-Friday,6-Saturday,7-Sunday")
                   cg1 = int(input("Enter the day you will be entering the gym:"))
                   print("Thank you we will make sure to keep your trainer ready")
                   while True:
                      if cg1 == 1 or cg1 == 2 or cg1==3 or cg1==4 or cg1==5 or cg1==6 or cg1 ==7:
                           print("Thank you")
                           break
                      else:
                           print("Invalid choice")
                           cg1 = int(input("Enter the day you will be entering the gym:"))
                           continue
                    
                     
                 if ask == "2":
                   print("============POOL TIMINGS===========")     
                   print("|---------------------------------|")
                   print("|S.no      Days        Timings(pm) ")
                   print("|----|----------------------------|")
                   print("| 1  |     Monday      |7:00-11:00|")
                   print("| 2  |     Tuesday     |7:00-11:00|")
                   print("| 3  |     Wednesday   |7:00-11:00|")
                   print("| 4  |     Thursday    |7:00-11:00|")
                   print("| 5  |     Friday      |7:00-11:00|")
                   print("| 6  |     Saturday    |7:00-12:00|")
                   print("| 7  |     Sunday      |7:00-12:00|")
                   print("|=================================|")
                   print("1-Monday,2-Tuesday,3-Wednesday,4-Thursday,5-Friday,6-Saturday,7-Sunday")
                   cg = int(input("Enter the day you will be entering the pool:"))
                   while True:
                       if cg == 1 or cg == 2 or cg==3 or cg==4 or cg==5 or cg==6 or cg ==7:
                           print("Thank you")
                           print("Thank you we will make sure to keep your trainer ready")
                           break
                       else:
                           print("Invalid choice")
                           day = int(input("Enter the day you will be entering the gym:"))
                           continue

               
           
            print("")
            print("|----------------------------------------------------------------------------------------|")
            print("|                      <<< PEARL VALLEY RESORTS - MALDIVES >>>                           |")
            print("|________________________________________________________________________________________|")
            print("| ROOM TYPE    SIZE(m)    NO. OF VISITORS   PRICE PER DAY(Rs)   BALCONY          (Rs)    |")
            print("|----------------------------------------------------------------------------------------|")
            print("| Standard     10x10           2-3               2000           Unavailable      300     |")
            print("|                                                                                        |")                                                                                                               
            print("| Deluxe       20x10           2-3               3500           Available        300     |")
            print("|                                                                                        |")                                                                                                               
            print("| SuperDeluxe  20.5x19.5       2-3               4500           Available        300     |")
            print("|                                                                                        |")                                                                                                               
            print("| Suite       (22x10)+(23x10)  4-5               6000           Available        300     |")
            print("|........................................................................................|")
            print("|________________________________________________________________________________________|")



            def rooms():
                 global finalprice
                 global price
                 global room
                 global check_in
                 global check_out
                 global days
                 
                 
                 print("\n1 - STANDARD    2 - DELUXE   3 - SUPER DELUXE   4 - SUITE")
                 print("\n[type 1 for a STANDARD room, 2 for DELUXE, 3 for SUPERDELUXE and 4 for SUITE]")
                 
                 while True:
                   room=k=int(input("\nEnter your choice :[1,2,3,4] "))
                   if room==1 or room==2 or room==3 or room==4:
                     bed=input("\nDo you need extra bed?[Yes/No]? ")
                     break
                   elif room>4 or room<1:
                       print("Invalid input enter again")
                       continue
                 if bed=='yes' or bed=='YES' or bed=='Yes' or bed=='NO' or bed=='No' or bed=='no' or bed=='Y' or bed=='N' or bed=='n':
                         print("\n----------------------Instructions to input date-----------------------")
                         print("* Enter valid check in and check out date")
                         print("* The check out date should atleast be one day ahead of check in date")
                         print("------------------------------------------------------------------------")

                 date=["0","1","2","3","4","5","6","7","8","9","/"] 
                 check_in = input("Enter check-in date (YYYY-MM-DD): ")
                 check_out = input("Enter check-out date (YYYY-MM-DD): ")


               
                 try:
                     # Convert input strings to datetime objects
                     check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
                     check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
                     
                     # Validate that check-in date is earlier than check-out date
                     if check_in_date < check_out_date:
                           pass
                     else:
                           print("Check-in date must be earlier than check-out date. Please try again.")
                           rooms()
                 except ValueError:
                       print("Invalid date format. Please use numbers for year, month, and day.")     
                       rooms()     


                 try:
               
                     check_in_parts = [int(part) for part in check_in.split('-')]
                     check_out_parts = [int(part) for part in check_out.split('-')]
                     if abs(len(check_in_parts)) == 3 and abs(len(check_out_parts)) == 3:
                        check_in_year, check_in_month, check_in_day = check_in_parts
                        check_out_year, check_out_month, check_out_day = check_out_parts
                        days = (check_out_year - check_in_year) * 365 + (check_out_month - check_in_month) * 30 + (check_out_day - check_in_day)
                        print("Number of days:", days)
                        if days<=0:
                           print("Invalid date")
                                                  
                        else:
                           days=days+0 
                     else:
                        print("Invalid date format. Please use YYYY-MM-DD.")
                 except ValueError:
                       print("Invalid date format. Please use numbers for year, month, and day.")
                 if room==1:
                     price=2000
                     k="Standard"
                 if room==2:
                     price=3500
                     k="Deluxe"
                 if room==3:
                     price=4500
                     k="Super Deluxe"
                 if room==4:
                     price=6000
                     k="Suite"
                 finalprice=price*days
                 if bed=="YES" or bed=="Yes" or bed=="yes" or bed=="Y" or bed=="y":
                       finalprice=finalprice+(300*days)
                   
                 if room==1:
                    print("|----------------------------------------------------|")
                    print("|           S T A N D A R D   R O O M                |")
                    print("|----------------------------------------------------|")
                    print("| Air conditioned room                               |")            
                    print("| 1 queen sized bed                                  |")
                    print("| 1X1 (m) work table with lamp                       |")   
                    print("| 2X1 (m) closet with hangers                        |")
                    print("| mini refrigirator [free drinks]                    |") 
                    print("| glass shower room [ warm water available ]         |")
                    print("| electric kettle                                    |")
                    print("| basic shower products                              |")
                    print("| mini firstaid kit                                  |")
                    print("| dustbins                                           |")
                    print("| water dispenser                                    |")
                    print("| lockers available                                  |")
                    print("| towels and bathrobes[2]                            |")
                    print("| Free room service                                  |")
                    print("| Free WiFi                                          |")
                    print("| full access to other facilities                    |")
                    print("| VIEW- Ocean view                                   |")
                    print("|----------------------------------------------------|")
                 if room==2:
                    print("|----------------------------------------------------|")
                    print("|              D E L U X E   R O O M                 |")
                    print("|----------------------------------------------------|")
                    print("| Air conditioned room                               |")
                    print("| balcony available                                  |")
                    print("| 1 king sized bed                                   |")
                    print("| 1X1 (m) work table with lamp                       |")   
                    print("| 2X1 (m) closet with hangers                        |")
                    print("| mini refrigerator [free drinks]                    |") 
                    print("| shower head with bath tub[ warm water available ]  |")
                    print("| electric kettle                                    |")
                    print("| basic shower products                              |")
                    print("| mini firstaid kit                                  |")
                    print("| dustbins                                           |")
                    print("| water dispenser                                    |")
                    print("| lockers available                                  |")
                    print("| towels and bathrobes[2]                            |")
                    print("| Free room service                                  |")
                    print("| Free WiFi                                          |")
                    print("| full access to other facilities                    |")
                    print("| VIEW- Ocean view                                   |")
                    print("|----------------------------------------------------|")
                 if  room==3:
                    print("|----------------------------------------------------|")
                    print("|         S U P E R   D E L U X E   R O O M          |")
                    print("|----------------------------------------------------|")
                    print("| Air conditioned room                               |")
                    print("| balcony available                                  |")
                    print("| 1 king sized bed                                   |")
                    print("| couch and tea table                                |")
                    print("| 1X1 (m) work table with lamp                       |")   
                    print("| 2X1 (m) closet with hangers                        |")
                    print("| mini refrigerator [free drinks]                    |") 
                    print("| glass shower room with curtains                    |")
                    print("| bath tub [ warm water available ]                  |")
                    print("| electric kettle                                    |")
                    print("| basic shower products                              |")
                    print("| mini firstaid kit                                  |")
                    print("| dustbins                                           |")
                    print("| water dispenser                                    |")
                    print("| lockers available                                  |")
                    print("| towels and bathrobes[2]                            |")
                    print("| Free room service                                  |")
                    print("| Free WiFi                                          |")
                    print("| full access to other facilities                    |")
                    print("| VIEW- Ocean view                                   |")
                    print("|----------------------------------------------------|")
                 if  room==4:
                    print("|----------------------------------------------------|")
                    print("|               S U I T E   R O O M                  |")
                    print("|----------------------------------------------------|")
                    print("| suite room is a combo of two rooms                 |")
                    print("| Air conditioned room                               |")            
                    print("| 2 X 1 queen sized bed                              |")
                    print("| 2 X 1X1 (m) work table with lamp                   |")   
                    print("| 2 X 2X1 (m) closet with hangers                    |")
                    print("| 2 X mini refrigerator [free drinks]                |") 
                    print("| 2 X glass shower room [ warm water available ]     |")
                    print("| 2 X electric kettle                                |")
                    print("| 2 X basic shower products                          |")
                    print("| 2 X mini firstaid kit                              |")
                    print("| 2 X dustbins                                       |")
                    print("| 2 X water dispenser                                |")
                    print("| 2 X lockers available                              |")
                    print("| 2 X towels and bathrobes[2]                        |")
                    print("| Free room service                                  |")
                    print("| Free WiFi                                          |")
                    print("| full access to other facilities                    |")
                    print("| VIEW- Ocean view                                   |")
                    print("|----------------------------------------------------|")
                    
                #bill
                   
                 print("\n\n\t-------------------------------------------------------------------")
                 print("\t            BILLING FOR PEARL VALLEY RESORTS - MALDIVES                ")
                 print("\t_______________________________________________________________________")
                 print("\t                                                                       ")
                 print("\t\t  NAME                          : ",uname)
                 print("\t\t  ROOM TYPE                     : ",room)
                 print("\t\t  Check-in Date                 : ",check_in)    
                 print("\t\t  Check-out Date                : ",check_out)
                 print("\t\t  No. of Stays                  : ",days,"days")
                 if bed=="Yes" or  bed=="YES"or bed=="Y" or bed=="y" or bed=="yes":
                  print("\t\t  Price of BED per day          :",days*300)
                 print("\t\t  TOTAL AMOUNT                  : ",finalprice,"Rs")
                 print("\t_______________________________________________________________________")
                 print("\t-----------------------------------------------------------------------")
            rooms()

            #1spa
            def spa():
                 global hairrate
                 global service
                 print("|==========================================================================================|")
                 print("|                                                                                          |")
                 print("|                                   BELLEZA SPA                                            |")
                 print("|                                                                                          |")
                 print("|==========================================================================================|")
                 menu=input("Would you like to see the menu ?[yes/no]")
                 if menu == "no" or menu == "n":
                     print("You have chosen to exit,Thank you")
                 if menu == "yes" or menu == "y":
                     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                     print('''\t1.Hair services \n\t2.Beauty services\n\t3.Massage\n\t4.Facials''')
                     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                     service=int(input("Enter your choice:"))
                     if service ==1:
                        print('''\t\t\t-------------------------------------------------------------------
                                 |      |                 Menu                           |  cost   |
                                 -------------------------------------------------------------------
                                 |  1.  |          Hair colouring                        |  500    |
                                 |  2.  |          Hair extensions                       |  550    |
                                 |  3.  |          Texture                               |  400    |
                                 |  4.  |          Blow dry                              |  100    |
                                 |  5.  |          Women's hair cut                      |  450    |
                                 |  6.  |          Men's hair cut                        |  350    |
                                 |  7.  |          Bread trim                            |  200    |
                                 |------|------------------------------------------------|---------|''')
                        print("Thank you for choosing belleza!, you can proceed")

                        h=int(input("enter your choice:"))


                        if h==1:
                           hairrate=500
                        elif h==2:
                           hairrate=550
                        elif h==3:
                           hairrate=400
                        elif h==4:
                           hairrate=100
                        elif h==5:
                           hairrate=450
                        elif h==6:
                           hairrate=350
                        elif h==7:
                           hairrate=200
                        print("your bill at hair",hairrate)
                        
                     if service ==2:
                       print("-"*120)
                       print('''-------------------------------------------------------------------
                                 |      |                Menu                            |  cost   |
                                 -------------------------------------------------------------------
                                 |  1.  |          Custom                                |  550    |
                                 |  2.  |          Deluxe scalp                          |  590    |
                                 |  3.  |          Exfoliating foot                      |  200    |
                                 |  4.  |          Paraffin treatment                    |  150    |
                                 |  5.  |          Warm oil scalp                        |  300    |
                                 |  6.  |          Reflexology                           |  600    |
                                 |  7.  |          Agave nectar                          |  200    |
                                 -----------------------------------------------------------------''')
                       print("Thank you for choosing belleza!, you can proceed")

                       h1=int(input("Enter your choice:"))
                       if h1==1:
                           hairrate=550
                       elif h1==2:
                           hairrate=590
                       elif h1==3:
                           hairrate=200
                       elif h1==4:
                           hairrate=150
                       elif h1==5:
                           hairrate=300
                       elif h1==6:
                           hairrate=600
                       elif h1==7:
                           hairrate=200
                       print("your bill at beauty",hairrate)

                       print("total bill",hairrate)

                       
                     if service ==3:
                       print('''-------------------------------------------------------------------
                                 |      |               Menu                             |  cost   |
                                 -------------------------------------------------------------------
                                 |  1.  |          Full body                             |  650    |
                                 |  2.  |          Foot massage                          |  200    |
                                 |  3.  |          Neck massage                          |  150    |
                                 |  4.  |          Swedish massage                       |  600    |
                                 |  5.  |          Back massage                          |  300    |
                                 |  6.  |          Deep tissue massage                   |  600    |
                                 -----------------------------------------------------------------''')
                       print("Thank you for choosing belleza!, you can proceed")

                       s=int(input("enter your choice:"))
                       if s==1:
                           hairrate=650
                       elif s==2:
                           hairrate=200
                       elif s==3:
                           hairrate=150
                       elif s==4:
                           hairrate=600
                       elif s==5:
                           hairrate=300
                       elif s==6:
                           hairrate=600
                       
                       print("your bill at beauty",hairrate)

                       
                     if service ==4:
                       print('''-------------------------------------------------------------------
                                 |      |                Menu                           |  cost   |
                                 -------------------------------------------------------------------
                                 |  1.  |          Basic                                |  750    |
                                 |  2.  |          Deep cleansing                       |  890    |
                                 |  3.  |          Organic                              |  600    |
                                 |  4.  |          Renew                                |  550    |
                                 |  5.  |          Palm Springs peel                    |  600    |
                                 |  6.  |          Natural hydration                    |  700    |
                                 -----------------------------------------------------------------''')
                       print("Thank you for choosing belleza!, you can proceed")
                       p=int(input("enter your choice:"))
                       if p==1:
                           hairrate=750
                       elif p==2:
                           hairrate=890
                       elif p==3:
                           hairrate=600
                       elif p==4:
                           hairrate=550
                       elif p==5:
                           hairrate=600
                       elif p==6:
                           hairrate=700
                     print("________________________________________________")
                     print("                                                ")
                     print("                S P A   B I L L                 ")
                     print("________________________________________________")
                     print("                                                ")
                     print("    Bill for your appointment : ",hairrate,"INR")
                     print("    Total amount              : ",hairrate,"INR")
                     print("________________________________________________")
            #2Florist
            def florist():
                  print("|==========================================================================================|")
                  print("|                                                                                          |")
                  print("|                              ✿ CORAL FLORIST ✿                                          |")                    
                  print("|                                                                                          |")
                  print("|==========================================================================================|")
                  print("Welcome to CORAL")
                  m=input("Would you like to see our menu[yes/no]: ")
                  if m=="yes" or m=="y":
                    print("|====================================|")      
                    print("|            CORAL MENU              |")
                    print("|------------------------------------|")
                    print("|S.no|        Flowers                |")
                    print("|---- -------------------------------|")
                    print("| 1  |        Roses                  |")
                    print("| 2  |        Lilies                 |")
                    print("| 3  |        Dahilas                |")
                    print("| 4  |        Orchids                |")
                    print("| 5  |        Tulips                 |")
                    print("| 6  |        Iris                   |")
                    print("|====================================|")
               
                    ''' 
                     cursor.execute('create table if not exists florist(sno int, Flowers varchar(50)')
                     cursor.execute('insert into florist values(1,"Roses",)')
                     cursor.execute('insert into florist values(2,"Lilies",')
                     cursor.execute('insert into florist values(3,"Dahilas",')
                     cursor.execute('insert into florist values(4,"Orchids",')
                     cursor.execute('insert into florist values(5,"Tulips",')
                     cursor.execute('insert into florist values(6,"Iris",')
                     cursor.execute("select * from florist")
                     print("sno\t\t Florist\t\t")
                     for i in cursor:
                        print(i[0],"\t",i[1],"\t\t")

                     mycon.commit()
                     mycon.close()
                     print('')
                     '''
                    
                    print("1-Roses,2-Lilies,3-Dahilas,4-Orchids,5-Orchids,5-Tulips,6-Iris")
                    c2=int(input("Enter which flower would you like :"))
                    c3=[1,2,3,4,5,6]
                    while True:
                       if c2 in c3:
                           print("Good choice! We will make sure to deliver it as soon as possible")
                           break
                       if c2 not in c3:
                           print("Invalid choice")
                           c2=int(input("Enter your choice"))
                           continue
                    ask1=input("\nWould you like to add a customised message to your bouquet?")
                    if ask1=='YES' or ask1=='Yes' or ask1=='yes' or ask1=='Y' or ask1=='y':
                        print('please enter your message [ word limit = 50 words ]')
                        mesg=input("\nEnter your message to be printed...")
                        if len(mesg)>50:
                            print("Please enter your mesaage in less than 50 words")
                            mesg=input("\nEnter your message to be printed:)")
                            print('this message will be printed along with your bouquet;)')
                            print('_______________________________________________________________________________________________')
                            print('                                                                                               ')
                            print('  ',mesg,'                                                                                     ')     
                            print('                                                                                               ')
                            print('_______________________________________________________________________________________________')  
                        if len(mesg)<=50:
                            print('this message will be printed along with your bouquet;)')
                            print('_______________________________________________________________________________________________')
                            print('                                                                                               ')
                            print('  ',mesg,'                                                                                     ')     
                            print('                                                                                               ')
                            print('_______________________________________________________________________________________________')
                    if ask1=='NO' or ask1=='No' or ask1=='no' or ask1=='N' or ask1=='n':
                      print("")
                        
            #4rules and regulation
            def rr():
                     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                     print("                           RULES AND REGULATIONS                                         ")
                     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                     print("1.No pets are allowed inside the premises")
                     print("2.Harrassment or improper behaviour of anyone will be dealt accordingly")
                     print("3.Please close the door whenever you stay inside your room")
                     print("4.Ensure that your properties are safe,the management will not be responsible for lost itmes")
                     print("5.Cancellation must be done atleast 2 days prior")
                     print("6.Please enusre that you check in and checkout at proper dates")
                     print("7.Terms and conditions applied")
                     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            #5Discount on festive seasons
            def discount():
                global birthday
                birthday=input("Enter your birthday in the format(YYYY-MM-DD)")
                if birthday == check_in:
                    print("Happy birthday! You will get 5% discount on the booking hall price")
                else:
                    print("Sorry,there are no discounts at the moment")
                     
               #6Food menu
            def food():
             global rate
             global quantity
             global c
             while True:
              print("|==========================FOOD MENU=============================|")
              print("Choose your cuisine from below:")
              print("1.Indian cuisine")
              print("2.Mexican cuisine")
              print("3.Chinese cuisine")
              print("4.Maldivian cuisine")
              print("|================================================================|")
              a=int(input("Enter your choice: "))
              while True:
                  if a ==1:
                       print("|=====================================================================|")
                       print("|                           INDIAN FOOD MENU                          |")       
                       print("|=====================================================================|")
                       print("|1. Appetizers                                                        |")
                       print("|2. Tandoori delicacies                                               |")                                                                                                                                                                                                             
                       print("|3. Curry                                                             |")      
                       print("|4. Beverage                                                          |")                                                                                                                                                                                                             
                       print("|5. Side dish                                                         |")                     
                       print("|6. Desserts                                                          |")                                                                                                                                                    
                       print("|7. Vegetarian                                                        |")     
                       print("|=====================================================================|")
                       c=int(input("Enter your choice"))
                       if c == 1:
                           print("|=====================================================================|")
                           print("|                           INDIAN FOOD MENU                          |")       
                           print("|=====================================================================|")
                           print("|S.no                        Dish                             Cost    |")                                                  
                           print("| 1.                      chicken biriyani                     220    |")                                                                                                                                                                                                            
                           print("| 2.                      Samosas Vegetable                    240    |")      
                           print("| 3.                      Samosas meat                         260    |")                                                                                                                                                                                                             
                           print("| 4.                      Vegetable pakoras                    260    |")                     
                           print("| 5.                      paneer pakora                        300    |")                                                                                                                                                    
                           print("| 6.                      fish pakora                          315    |")     
                           print("| 7.                      chaat papdi                          320    |")
                           print("|=====================================================================|")
                           o=int(input("Enter your order:"))
                           if o ==1:
                              rate=220
                           elif o==2:
                              rate=240
                           elif o==3:
                              rate=260
                           elif o==4:
                              rate=260
                           elif o==5:
                              rate=300
                           elif o==6:
                              rate=315
                           elif o==7:
                              rate=320
                           quantity=int(input("Enter quantity : "))
                           more=input("Would you like to see more?")
                           if more=="Yes" or more=="yes" or more=="y":
                               continue
                           else:
                               break
                        
                           
                       if c == 2:
                           print("|=====================================================================|")
                           print("|                           INDIAN FOOD MENU                          |")       
                           print("|=====================================================================|")
                           print("|S.no                        Dish                             Cost    |")                                                  
                           print("| 1.                      Chicken tandoori                    460     |")                                                                                                                                                                                                            
                           print("| 2.                      Chicken tikka                       480     |")      
                           print("| 3.                      Seekh kebab                         390     |")                                                                                                                                                                                                             
                           print("| 4.                      Masala chicken makhani              410     |")                     
                           print("| 5.                      Butter chicken makhani              450     |")                                                                                                                                                    
                           print("|=====================================================================|")
                           o=int(input("Enter your order:"))
                           if o==1:
                              rate=460
                           elif o==2:
                              rate=480
                           elif o==3:
                              rate=390
                           elif o==4:
                              rate=410
                           elif o==5:
                              rate=450
                           quantity=int(input("Enter quantity : "))
                           more=input("Would you like to see more?")
                           if more=="Yes" or more=="yes" or more=="y":
                               continue
                           else:
                               break
                          
                                  
                       if c == 3:
                           print("|=====================================================================|")
                           print("|                           INDIAN FOOD MENU                          |")       
                           print("|=====================================================================|")
                           print("|S.no                        Dish                             Cost    |")                                                  
                           print("| 1.                      Shai korma muglai                   520     |")                                                                                                                                                                                                            
                           print("| 2.                      Bhuna gosht                         450     |")      
                           print("| 3.                      Rogan josh kashmiri                 390     |")                                                                                                                                                                                                             
                           print("| 4.                      Deewani handi                       780     |")                     
                           print("| 5.                      vindaloo goan                       560     |")                                                                                                                                                    
                           print("|=====================================================================|")
                           if o==1:
                              rate=520
                           elif o==2:
                              rate=450
                           elif o==3:
                              rate=390
                           elif o==4:
                              rate=780
                           elif o==5:
                              rate=560
                           quantity=int(input("Enter quantity : "))
                           more=input("Would you like to see more?")
                           if more=="Yes" or more=="yes" or more=="y":
                               continue
                           else:
                               break
                         
                           
                       if c == 4:
                           print("|=====================================================================|")
                           print("|                           INDIAN FOOD MENU                          |")       
                           print("|=====================================================================|")
                           print("|S.no                        Dish                             Cost    |")                                                  
                           print("| 1.                      Mojito                              190     |")                                                                                                                                                                                                            
                           print("| 2.                      Milkshake                           260     |")      
                           print("| 3.                      Coffee                              140     |")                                                                                                                                                                                                             
                           print("| 4.                      Fresh juice                         220     |")                     
                           print("| 5.                      Soft drinks                         125     |")                                                                                                                                                    
                           print("|=====================================================================|")
                           o=int(input("Enter your order:"))

                           if o==1:
                              rate=190
                           elif o==2:
                              rate=260
                           elif o==3:
                              rate=140
                           elif o==4:
                              rate=220
                           elif o==5:
                              rate=125
                           quantity=int(input("Enter quantity : "))
                           more=input("Would you like to see more?")
                           if more=="Yes" or more=="yes" or more=="y":
                               continue
                           else:
                               break
                          
                       if c == 5:
                           print("|=====================================================================|")
                           print("|                           INDIAN FOOD MENU                          |")       
                           print("|=====================================================================|")
                           print("|S.no                        Dish                             Cost    |")                                                  
                           print("| 1.                      Dahi raita                          110     |")                                                                                                                                                                                                            
                           print("| 2.                      Mango chutney                       110     |")      
                           print("| 3.                      Pickles                              90     |")                                                                                                                                                                                                             
                           print("| 4.                      Onions                               90     |")                     
                           print("| 5.                      Green peppers                        90     |")                                                                                                                                                    
                           print("|=====================================================================|")
                           o=int(input("Enter your order"))
                           if o==1:
                              rate=110
                           elif o==2:
                              rate=110
                           elif o==3:
                              rate=90
                           elif o==4:
                              rate=90
                           elif o==5:
                              rate=90
                           quantity=int(input("Enter quantity : "))
                           more=input("Would you like to see more?")
                           if more=="Yes" or more=="yes" or more=="y":
                               continue
                           else:
                               break
                           
                       if c == 6:
                           print("|=====================================================================|")
                           print("|                           INDIAN FOOD MENU                          |")       
                           print("|=====================================================================|")
                           print("|S.no                        Dish                             Cost    |")                                                  
                           print("| 1.                      Gulab jamoon                        120     |")                                                                                                                                                                                                            
                           print("| 2.                      moose cake                          280     |")      
                           print("| 3.                      Icecream                            260     |")                                                                                                                                                                                                             
                           print("| 4.                      Brownie                             340     |")                     
                           print("| 5.                      lava cake                           340     |")                                                                                                                                                    
                           print("| 6.                      cookies                             280     |")    
                           print("|=====================================================================|")
                           o=int(input("Enter your order:"))
                           if o==1:
                              rate=120
                           elif o==2:
                              rate=280
                           elif o==3:
                              rate=260
                           elif o==4:
                              rate=340
                           elif o==5:
                              rate=340
                           elif o==6:
                              rate=280
                           quantity=int(input("Enter quantity : "))
                           more=input("Would you like to see more?")
                           if more=="Yes" or more=="yes" or more=="y":
                               continue
                           else:
                               break
                           
                       if c == 7:
                           print("|=====================================================================|")
                           print("|                           INDIAN FOOD MENU                          |")       
                           print("|=====================================================================|")
                           print("|S.no                        Dish                             Cost    |")                                                  
                           print("| 1.                      Mutter paneer                       420     |")                                                                                                                                                                                                            
                           print("| 2.                      Eggplant bhartha                    390     |")      
                           print("| 3.                      aloo gobi                           390     |")                                                                                                                                                                                                             
                           print("| 4.                      channa chandi chowk                 410     |")                     
                           print("| 5.                      shai paneer                         460     |")                                                                                                                                                     
                           print("| 6.                      daal makhani                        380     |")    
                           print("|=====================================================================|")
                           
                           o=int(input("Enter your order:"))
                           if o==1:
                              rate=420
                           elif o==2:
                              rate=390
                           elif o==3:
                              rate=390
                           elif o==4:
                              rate=410
                           elif o==5:
                              rate=460
                           elif o==6:
                              rate=380
                           quantity=int(input("Enter quantity : "))
                           more=input("Would you like to see more?")
                           if more=="Yes" or more=="yes" or more=="y":
                               continue
                           else:
                               break
                  print("________________________________________________")
                  print("                                                ")
                  print("             F O O D   B I L L                  ")
                  print("________________________________________________")
                  print("                                                ")
                  print("     Bill for your cuisine : ",rate*quantity,"INR")
                  print("     Total amount          : ",rate*quantity,"INR")
                  print("________________________________________________")
                  if a == 2:
                       print("|=====================================================================|")
                       print("|                           MEXICAN FOOD MENU                         |")       
                       print("|=====================================================================|")
                       print("|1.                          Tacos                                    |")
                       print("|2.                        Quesadillas                                |")                                                                                                                                                                                                             
                       print("|3.                        Texicana fries                             |")      
                       print("|4.                        Sides                                      |")                                                                                                                                                                                                             
                       print("|5.                        Drinks                                     |")                     
                       print("|=====================================================================|")
                       e=int(input("Enter your choice[in numbers only]"))
                       if e == 1:
                            print("|=====================================================================|")
                            print("|                          MEXICAN FOOD MENU                          |")       
                            print("|=====================================================================|")
                            print("|S.no                        Dish                             Cost    |")
                            print("|1.                     Chicken fresca                        410     |")
                            print("|2.                     Passtor de puerco                     490     |")                                                                                                                                                                                                             
                            print("|3.                     Carne asada                           390     |")      
                            print("|4.                     Pulled pork BBQ                       520     |")                                                                                                                                                                                                             
                            print("|5.                     Veggie                                360     |")
                            print("|=====================================================================|")
                            o=int(input("Enter your order:"))
                            if o ==1:
                               rate=410
                            elif o==2:
                               rate=490
                            elif o==3:
                               rate=390
                            elif o==4:
                               rate=520
                            elif o==5:
                               rate=360
                            quantity=int(input("Enter quantity : "))
                            more=input("Would you like to see more?")
                            if more=="Yes" or more=="yes" or more=="y":
                               continue
                            else:
                               break
                           
                       if e == 2:
                            print("|=====================================================================|")
                            print("|                          MEXICAN FOOD MENU                          |")       
                            print("|=====================================================================|")
                            print("|S.no                        Dish                             Cost    |")
                            print("|1.                         Cheese Tacos                      390     |")
                            print("|2.                         Veggie Tacos                      380     |")                                                                                                                                                                                                             
                            print("|3.                         Pastor Tacos                      420     |")      
                            print("|4.                         Chicken Tacos                     410     |")                                                                                                                                                                                                             
                            print("|5.                         Steak Tacos                       435     |")                     
                            print("|6.                         BBQ Tacos                         440     |")                                                                                                                                            
                            print("|=====================================================================|")
                            o=int(input("Enter your order:"))
                            if o ==1:
                              rate=390
                            elif o==2:
                              rate=380
                            elif o==3:
                              rate=420
                            elif o==4:
                              rate=410
                            elif o==5:
                              rate=435
                            elif o==6:
                              rate=440
                            quantity=int(input("Enter quantity : "))
                            more=input("Would you like to see more?")
                            if more=="Yes" or more=="yes" or more=="y":
                               continue
                            else:
                               break
                       if e == 3:
                            print("|=====================================================================|")
                            print("|                          MEXICAN FOOD MENU                          |")       
                            print("|=====================================================================|")
                            print("|S.no                        Dish                             Cost    |")
                            print("|1. Veggie                                                    300     |")
                            print("|2. Chicken                                                   400     |")                                                                                                                                                                                                             
                            print("|3. Steak                                                     450     |")                                                                                                                                                                                                                                                                           
                            print("|4. Pastor                                                    350     |")                     
                            print("|5. BBQ                                                       600     |")                                                                                                                                                    
                            print("|=====================================================================|")
                            o=int(input("Enter your order:"))
                            if o ==1:
                               rate=300
                            elif o==2:
                               rate=400
                            elif o==3:
                               rate=450
                            elif o==4:
                               rate=350
                            elif o==5:
                               rate=600
                            quantity=int(input("Enter quantity : "))
                            more=input("Would you like to see more?")
                            if more=="Yes" or more=="yes" or more=="y":
                               continue
                            else:
                               break
                           
                       if e == 4:
                            print("|=====================================================================|")
                            print("|                          MEXICAN FOOD MENU                          |")       
                            print("|=====================================================================|")
                            print("|S.no                        Dish                             Cost    |")
                            print("|1. Lime fries                                                310     |")
                            print("|2. Chips and salsa                                           340     |")                                                                                                                                                                                                             
                            print("|3. Chips and guacamole                                       200     |")                                                                                                                                                                                                                                                                               
                            print("|4. Cheese dip and chips                                      400     |")                     
                            print("|5. Chilli fries                                              320     |")                                                                                                                                                    
                            print("|=====================================================================|")
                            o=int(input("Enter your order:"))
                            if o==1:
                              rate=310
                            elif o==2:
                              rate=340
                            elif o==3:
                              rate=200
                            elif o==4:
                              rate=400
                            elif o==5:
                              rate=320
                            quantity=int(input("Enter quantity : "))
                            more=input("Would you like to see more?")
                            if more=="Yes" or more=="yes" or more=="y":
                               continue
                            else:
                               break
                            
                       if e == 5:
                            print("|=====================================================================|")
                            print("|                          MEXICAN FOOD MENU                          |")       
                            print("|=====================================================================|")
                            print("|S.no                        Dish                             Cost    |")
                            print("|1. Bottled water                                             100     |")
                            print("|2. Soft drinks                                               200     |")                                                                                                                                                                                                             
                            print("|3. Mexican coke                                              320     |")                                                                                                                                                                                                                                                                               
                            print("|4. Mexican fanta                                             320     |")                     
                            print("|5. sushi puppie                                              350     |")                                                                                                                                                    
                            print("|=====================================================================|")
                            o=int(input("Enter your order:"))
                            if o==1:
                              rate=100
                            elif o==2:
                              rate=200
                            elif o==3:
                              rate=320
                            elif o==4:
                              rate=320
                            elif o==5:
                              rate=350
                            quantity=int(input("Enter quantity : "))
                            more=input("Would you like to see more?")
                            if more=="Yes" or more=="yes" or more=="y":
                               continue
                            else:
                               break
                            
                  print("________________________________________________")
                  print("                                                ")
                  print("             F O O D   B I L L                  ")
                  print("________________________________________________")
                  print("                                                ")
                  print("     Bill for your cuisine : ",rate*quantity,"INR")
                  print("     Total amount          : ",rate*quantity,"INR")
                  print("________________________________________________")
                  more1=input("Would you like to proceed seeing our menu? ")
                  if more1=="yes" or more1=="y" or more1=="Yes":
                       continue
                  else:
                       break
                  if a == 3:
                       print("|=====================================================================|")
                       print("|                           CHINESE FOOD MENU                         |")       
                       print("|=====================================================================|")
                       print("|1. Appetizers                                                        |")
                       print("|2. Soups                                                             |")                                                                                                                                                                                                             
                       print("|3. Salad                                                             |")      
                       print("|4. Sandwich                                                          |")                                                                                                                                                                                                              
                       print("|=====================================================================|")
                       f=int(input("Enter your choice[in numbers only]"))
                       if f == 1:
                            print("|=====================================================================|")
                            print("|                          CHINESE FOOD MENU                          |")       
                            print("|=====================================================================|")
                            print("|S.no                        Dish                             Cost    |")
                            print("|1. Cold beef shank                                           420     |")                                                                                                                                                                                                                                                                                                                                                                                                            
                            print("|2. Chicken with wine sauce                                   310     |")                                                                                                                                                                                                             
                            print("|3. Szechwan wontons                                          410     |")                                                                                                                                                                                                                                                                               
                            print("|4. Steamed dumplings                                         300     |")                     
                            print("|5. Egg rolls                                                 290     |")
                            print("|6. Onion rings                                               300     |")
                            print("|7. Soft shell crab                                           310     |")
                            print("|8. Spicy shank                                               290     |")
                            print("|=====================================================================|")
                            o=int(input("Enter your order:"))
                            if o==1:
                              rate=420
                            elif o==2:
                              rate=310
                            elif o==3:
                              rate=410
                            elif o==4:
                              rate=300
                            elif o==5:
                              rate=290
                            elif o==6:
                               rate=300
                            elif o==7:
                               rate=310
                            elif o==8:
                               rate=290
                            quantity=int(input("Enter quantity : "))
                            more=input("Would you like to see more?")
                            if more=="Yes" or more=="yes" or more=="y":
                               continue
                            else:
                               break
                            
                       if f == 2:
                            print("|=====================================================================|")
                            print("|                          CHINESE FOOD MENU                          |")       
                            print("|=====================================================================|")
                            print("|S.no                        Dish                             Cost    |")
                            print("|1. Seafood chowder                                           300     |")
                            print("|2. Borscht                                                   380     |")
                            print("|3. Chicken corn cream                                        350     |")                                                                                                                                                                                                                                                                               
                            print("|4. Hot and sour                                              240     |")                     
                            print("|5. Wor wonton                                                300     |")                                                                                                                                                    
                            print("|=====================================================================|")
                            o=int(input("Enter your order:"))
                            if o==1:
                              rate=300
                            elif o==2:
                              rate=380
                            elif o==3:
                              rate=350
                            elif o==4:
                              rate=240
                            elif o==5:
                              rate=300
                            quantity=int(input("Enter quantity : "))
                            more=input("Would you like to see more?")
                            if more=="Yes" or more=="yes" or more=="y":
                               continue
                            else:
                               break
                           
                       if f == 3:
                            print("|=====================================================================|")
                            print("|                          CHINESE FOOD MENU                          |")       
                            print("|=====================================================================|")
                            print("|S.no                        Dish                             Cost    |")
                            print("|1. Garden green                                              290     |")
                            print("|2. Ham and chicken                                           300     |")                                                                                                                                                                                                             
                            print("|3. Crabmeat                                                  320     |")                                                                                                                                                                                                                                                                               
                            print("|4. Mixed fruit and prawn                                     350     |")                                                                                                                                                                
                            print("|=====================================================================|")
                            o=int(input("Enter your order:"))
                            if o==1:
                              rate=290
                            elif o==2:
                              rate=300
                            elif o==3:
                              rate=320
                            elif o==4:
                              rate=350
                            quantity=int(input("Enter quantity : "))
                            more=input("Would you like to see more?")
                            if more=="Yes" or more=="yes" or more=="y":
                               continue
                            else:
                               break
                        
                       if f == 4:
                            print("|=====================================================================|")
                            print("|                          CHINESE FOOD MENU                          |")       
                            print("|=====================================================================|")
                            print("|S.no                        Dish                             Cost    |")
                            print("|1. Club sandwich                                             300     |")
                            print("|2. Tuna sandwich                                             340     |")                                                                                                                                                                                                             
                            print("|3. Ham and egg tomato sandwich                               390     |")                                                                                                                                                                                                                                                                               
                            print("|4. Spam and egg sandwich                                     400     |")                     
                            print("|5. French toast                                              390     |")
                            print("|6. Garlic toast                                              390     |")
                            print("|=====================================================================|")
                            o=int(input("Enter your order:"))
                            if o==1:
                              rate=300
                            elif o==2:
                              rate=340
                            elif o==3:
                              rate=390
                            elif o==4:
                              rate=400
                            elif o==5:
                              rate=390
                            elif o==6:
                               rate=390
                            quantity=int(input("Enter quantity : "))
                            more=input("Would you like to see more?")
                            if more=="Yes" or more=="yes" or more=="y":
                               continue
                            else:
                               break
                  print("________________________________________________")
                  print("                                                ")
                  print("             F O O D   B I L L                  ")
                  print("________________________________________________")
                  print("                                                ")
                  print("     Bill for your cuisine : ",rate*quantity,"INR")
                  print("     Total amount          : ",rate*quantity,"INR")
                  print("________________________________________________")
                  more1=input("Would you like to proceed seeing our menu? ")
                  if more1=="yes" or more1=="y" or more1=="Yes":
                       continue
                  else:
                       break
                           
                  if a == 4:
                       print("|=====================================================================|")
                       print("|                           MALDIVIAN FOOD MENU                       |")       
                       print("|=====================================================================|")
                       print("|1. Maldivian exclusive                                               |")
                       print("|2. Poultry                                                           |")                                                                                                                                                                                                             
                       print("|3. Meat,fish and pasta                                               |")      
                       print("|4. Salad                                                             |")                                                                                                                                                                 
                       print("|=====================================================================|")
                       g=int(input("Enter your choice[in numbers only]"))
                       if g == 1:
                       
                            print("|=====================================================================|")
                            print("|                          MALDIVIAN FOOD MENU                          |")       
                            print("|=====================================================================|")
                            print("|S.no                        Dish                             Cost    |")
                            print("|1. Aluvi riha                                                450     |")
                            print("|2. Kiru garudhiya                                            340     |")                                                                                                                                                                                                             
                            print("|3. Kukulhu curry                                             360     |")                                                                                                                                                                                                                                                                               
                            print("|4. Mixed fruit and prawn                                     400     |")                                                                                                                                                                
                            print("|=====================================================================|")
                            o=int(input("Enter your order:"))
                            if o==1:
                              rate=450
                            elif o==2:
                              rate=340
                            elif o==3:
                              rate=360
                            elif o==4:
                              rate=400
                            quantity=int(input("Enter quantity : "))
                            more=input("Would you like to see more?")
                            if more=="Yes" or more=="yes" or more=="y":
                               continue
                            else:
                               break
                           
                       if g == 2:
                            print("|=====================================================================|")
                            print("|                          MALDIVIAN FOOD MENU                          |")       
                            print("|=====================================================================|")
                            print("|S.no                        Dish                             Cost    |")
                            print("|1. catch of the day                                           300    |")
                            print("|2. pan fried chicken breast                                   320    |")                                                                                                                                                                                                             
                            print("|3. seafood cassouley                                          390    |")                                                                                                                                                                                                                                                                               
                            print("|4. penne pasta                                                350    |")                                                                                                                                                                
                            print("|=====================================================================|")
                            o=int(input("Enter your order:"))
                            if o==1:
                              rate=300
                            elif o==2:
                              rate=320
                            elif o==3:
                              rate=390
                            elif o==4:
                              rate=350
                            quantity=int(input("Enter quantity : "))
                            more=input("Would you like to see more?")
                            if more=="Yes" or more=="yes" or more=="y":
                               continue
                            else:
                               break
                           
                       if g == 3:
                            print("|=====================================================================|")
                            print("|                          MALDIVIAN FOOD MENU                          |")       
                            print("|=====================================================================|")
                            print("|S.no                        Dish                             Cost    |")
                            print("|1. Duo of lamb                                               390     |")
                            print("|2. Pan Fried duck                                            400     |")                                                                                                                                                                                                             
                            print("|3. Tagliatelle temidor                                       290     |")                                                                                                                                                                                                                                                                               
                            print("|4. Grilled reef fish                                         300     |")                     
                            print("|5. Crispy prawns                                             340     |")                                                                                                                                                    
                            print("|=====================================================================|")
                            o=int(input("Enter your order:"))
                            if o==1:
                              rate=390
                            elif o==2:
                              rate=400
                            elif o==3:
                              rate=290
                            elif o==4:
                              rate=300
                            elif o==5:
                              rate=340
                            quantity=int(input("Enter quantity : "))
                            more=input("Would you like to see more?")
                            if more=="Yes" or more=="yes" or more=="y":
                               continue
                            else:
                               break
                       if g == 4:
                            print("|=====================================================================|")
                            print("|                          MALDIVIAN FOOD MENU                       |")       
                            print("|=====================================================================|")
                            print("|S.no                        Dish                             Cost    |")
                            print("|1. Brinjal tuna salad                                        340     |")
                            print("|2. Pumpkin tuna salad                                        290     |")                                                                                                                                                                                                             
                            print("|3. Green leaf tuna salad                                     300     |")                                                                                                                                                                                                                                                                               
                            print("|4. Plain tuna salad                                          280     |")                     
                            print("|5. veg salad                                                 250     |")                                                                                                                                                    
                            print("|=====================================================================|")
                            o=int(input("Enter your order:"))
                            if o==1:
                              rate=340
                            elif o==2:
                              rate=290
                            elif o==3:
                              rate=300
                            elif o==4:
                              rate=280
                            elif o==5:
                              rate=250
                            quantity=int(input("Enter quantity : "))
                            more=input("Would you like to see more?")
                            if more=="Yes" or more=="yes" or more=="y":
                               continue
                            else:
                               break
                            

                  print("________________________________________________")
                  print("                                                ")
                  print("             F O O D   B I L L                  ")
                  print("________________________________________________")
                  print("                                                ")
                  print("     Bill for your cuisine : ",rate*quantity,"INR")
                  print("     Total amount          : ",rate*quantity,"INR")
                  print("________________________________________________")
                  more1=input("Would you like to proceed seeing our menu? ")
                  if more1=="yes" or more1=="y" or more1=="Yes":
                       continue
                  else:
                       break
    
            #7 Feed back form
                           
            def feedback():
                     global r
                     r=0
                     print('feedback form')
                     while r == False:
                          feedback=input('would you like to provide us feedback? [yes/no]?')
                          if feedback=='yes':
                             rating=int(input('rate your experiance on the scale of 1-10 :'))
                             r1=[1,2,3,4]
                             r2=[5,6,7]
                             r3=[8,9,10]
                             if rating<=10:

                               if rating in r3:
                                  print("We appreciate your feedback!")
                               if rating in r2:
                                  average1=input("Thank you!would you like suggest any improvements?[yes/no]")
                                  if average1=="yes":
                                    improvements=input("Please type here:")
                                    print("Thank you,we are looking forward to improve!")
                               if rating in r1:
                                  bad1=input("We are sorry to hear that! Please suggest improvements :")
                                  print('thank you')
                               r = True      
                             if rating>10:
                                   print('invalid input')
                          if feedback=='no':
                               print("Thank you")
                               break

                  
            #8Transport
            def transport():       
                  d=str(input("Please enter you destination in Maldives:"))
                  print("Choose your mode of transport:")
                  print("1.Cab\n2.Caravan ")
                  print("[Enter 1 for cab and 2 for caravan]")
                  t=int(input("Enter 1 or 2:"))
                  print("Is tourist guide required?")
                  print("1.Yes\n2.No")
                  print("Enter 1 for tourist guide included and 2 for no tourist guide included]")
                  a=int(input("Enter 1 or 2:"))
                  print("Happy jouney!")
                  if t==1 and a==1:
                      print("You have booked a cab with tourist guide included")
                  elif t==1 and a==2:
                      print("You have booked a cab with no tourist guide included")
                  elif t==2 and a==1:
                      print("You have booked a caravan with a tourist guide included")
                  elif t==2 and a==2:
                      print("You have booked a caravan with no tourist guide included")
                  else:
                      print("Invalid input")
                      
               #9 Helpline
            def helpline():   
                  print("Let us know how we can help!")
                  print("Reach out us at:")
                  print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                  print("|             Room service                 |")
                  print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                  print("|   1. Food and beverages - '222'          |")
                  print("|   2. House keeping      - '333'          |")
                  print("|   3. Reception          - '444'          |")
                  print("|   4. Dry cleaning       - '555'          |")
                  print("|   5. Emergency          - '666'          |")
                  print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                  rs=int(input("Enter room service number:"))
                  sr=str(rs)
                  if len(sr)==3:
                     if rs==222 or rs==333 or rs==444 or rs==555 or rs==666:
                       print("Calling",rs,"...")
                       print("Our service will be provided soon")
                  else:
                       print("Service number not available")

            #3Gym and swmming pool
            def mainmenu():
                 while True:
                   print("\nHere is the list of things you can discover")
                   print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                   print("|                           RESORT FACILITIES                           |")
                   print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                   print("|1.Spa                                                                  |")
                   print("|2.Florist                                                              |")     
                   print("|3.Gym and swimming pool                                                |")
                   print("|4.Rules and regulations                                                |")
                   print("|5.Discount info                                                        |")
                   print("|6.Food menu                                                            |")
                   print("|7.Feedback form                                                        |")
                   print("|8.Transportation facilities                                            |")
                   print("|9.Helpline                                                             |")
                   print("|10.Exit                                                                |")
                   print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                   help=input("What would you like to choose: ")
                   if help =='1':
                       spa()
                   elif help =='2':
                       florist()
                   elif help=='3':
                       pool()
                   elif help =='4':
                       rr()
                   elif help=='5':
                       discount()
                   elif help=='6':
                       food()
                   elif help =='7':
                       feedback()
                   elif help =='8':
                       transport()
                   elif help =='9':
                       helpline()
                   elif help =='10':
                        exit1=input("You have chosen to exit.Would you like to continue ?[yes/no]")
                        if exit1=="no" or exit1=="n" or exit1=="N":
                               print("You may proceed to re-discover")

                        if exit1=='yes' or exit1=='y' or exit1=='Y':
                                print("Thank you for staying with us ! hope you had a great experience")
                                print(" ___________________________________________________")
                                print("                                                    ")
                                print("           PEARL VALLEY RESORTS-MALDIVES            ")
                                print("____________________________________________________")
                                print("                                                    ")
                                print("  Name:",name)
                                print("  Phone number:",b)
                                print(cid)
                                print("  Check in date  :",check_in,'\tCheck out date :',check_out)
                                print("  Room type      :",room)
                                print("  Room charges   :",finalprice)
                                if services==True:
                                    print("Belleza spa   :",hairrate)
                                elif c==True:
                                    print("Restaurant   :",rate*quantity)
                                print("----------------------------------------------------")
                                print("  Total=",finalprice+hairrate+rate*quantity)
                                print("____________________________________________________")
                                break
                   else:
                        print("Enter a valid choice")
            mainmenu()
main_menu()

## ref##

import random
global cost
cost=0
global num_rooms
global total_cost
total_cost=0
num_rooms=0

def signup():
    print(("*"*50).center(50))
    print("Registration".center(50))
    print(("*"*50).center(50))
    uname=input("Enter username : ")
    signup=True
    if len(uname)>20:
        print("Maximum permissible characters is 20")
        signup=False
    else:
        sql="select * from login"
        cursor.execute(sql)
        for i in cursor:
            if i[0]==uname:
                print("Username already exists")
                signup=False
                continue
        if signup:
            print()
            mycon.commit()
            
            while True:
                pwd=input("Enter password : ")
                repwd=input("Re-enter password : ")
                if pwd==repwd:
                    print()
                    break
                else:
                    print("Password doesn't match")
                    continue
             
    
            gender=input("Enter the gender [1 -Male   2- Female] : ")
            while True:
                if gender=='1':
                    gen='Male'
                    break
                if gender=='2':
                    gen='Female'
                    break
            else:
                 gender=input("Enter the valid gender : ")
            while True:
                age=input("Enter the age : ")
                age1=int(age)
                if age1<14:
                    print("Not eligible to create an account")
                    print("Thank you for choosing us")
                
                mobile=input("Enter your mobile no : ")
                if len(mobile)!=10:
                    print("Invalid mobile number")
                    mobile=input("Re-enter your mobile number : ")

                email=input("Enter the Email Address : ")
                if '@' and '.com' not in email:
                    print("Enter a valid Email id")
                    email=input("Enter the Email Address : ")
                    print(email)

                sql="insert into login (username,password,gender,age,mobile,email)values('{}','{}','{}','{}','{}','{}')".format(uname,pwd,gen,age,mobile,email)
                
                cursor.execute(sql)
                mycon.commit()
                print("\nAccount successfully created")
                print("Enter your login credentials !!!\n")
                login()
                break
            
mycon.commit()

def login():
    
    print(("_"*50).center(50))
    print("Login ".center(50))
    print(("_"*50).center(50))
    #Login Process
    uname=input("Enter username : ")
    pwd=input("Enter password : ")
    print()
    login=False
    sql="select * from login"
    cursor.execute(sql)
    for i in cursor:
        if i[0]==uname and i[1]==pwd:
            print("Hi",uname,"successfully logged in...")
            login=True
            continue
        
    if login==True:
        homepage(uname)
    if login==False:
        print("Invalid Credentials")