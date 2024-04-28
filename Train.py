while True:

    a1=int(input("Enter the Admin Password Of Railway Reservation.: "))

    if a1==123:

       print("Logging in...")



       try:

                import mysql.connector as msc

                import datetime

                import random as rd

                import pandas as pd

                import sys

                import matplotlib.pyplot as plt



      

                mydb=msc.connect(host="localhost",

                                 user="root",

                                 password="mysql",

                                 allow_local_infile=True

                                 )

                crs=mydb.cursor()

                qry01="CREATE DATABASE IF NOT EXISTS railway"

                crs.execute(qry01)

                qry02="USE railway"

                crs.execute(qry02)

                



                qry03="CREATE TABLE IF NOT EXISTS Passenger_Details (Pnr_Number int(10) primary key,Psn_Name varchar(25),Psn_Ph_no VARCHAR(10),Psn_age int(10),Psn_gender char(1),Train_from varchar(20),Train_to varchar(20),Scheduled_Date DATE,Email_ID varchar(30),Fare int(12))"

                crs.execute(qry03)



            

                qry21="INSERT INTO Passenger_Details   VALUES   (1021959091,'MOHAN','9658256315',25,'M','AJMER','DELHI','2021-03-09','Mohan@gmail.com',720) ON DUPLICATE KEY UPDATE Pnr_Number=1021959091"

                qry22="INSERT INTO Passenger_Details   VALUES   (1021959311,'ROHIT',9652256315,21,'M','AJMER','AJMER','2021-03-29','Rohit@gmail.com',452) ON DUPLICATE KEY UPDATE Pnr_Number=1021959311"

                qry23="INSERT INTO Passenger_Details   VALUES   (1021959332,'CARL',6235256363,20,'F','AGRA','MATHURA','2021-05-19','Carl@gmail.com', 1123) ON DUPLICATE KEY UPDATE Pnr_Number=1021959332"

                qry24="INSERT INTO Passenger_Details   VALUES   (1021959301,'MARK',6582563151,26,'M','SHIMLA','BANGLORE','2021-05-05','Mark11@gmail.com',558) ON DUPLICATE KEY UPDATE Pnr_Number=1021959301"

                qry25="INSERT INTO Passenger_Details   VALUES   (1021951231,'VON',7584635269,24,'M','CHENNAI','KANYKUMARI','2021-03-25','Von@gmail.com',320) ON DUPLICATE KEY UPDATE Pnr_Number=1021951231"

                qry26="INSERT INTO Passenger_Details   VALUES   (1021959441,'RONIT',8529639636,21,'M','HALDIA','DELHI','2021-05-09','Ronit45@gmail.com',750) ON DUPLICATE KEY UPDATE Pnr_Number=1021959441"

                qry27="INSERT INTO Passenger_Details   VALUES   (1021952331,'SUNIT',6589262529,22,'M','LUCKNOW','VARANASI','2021-06-23','Sunit11@gmail.com',950) ON DUPLICATE KEY UPDATE Pnr_Number=1021952331"

                crs.execute(qry21)

                crs.execute(qry22)

                crs.execute(qry23)

                crs.execute(qry24)

                crs.execute(qry25)

                crs.execute(qry26)

                crs.execute(qry27)

                

                qry04="USE railway"

                crs.execute(qry04) 

                qry02="CREATE TABLE IF NOT EXISTS avail_Train(Srno int(10),Train_No int(15) primary key,Train_Name varchar(250),Train_from varchar(200),Train_to varchar(300))"

                crs.execute(qry02)



                qry1="INSERT INTO avail_Train VALUES  (1001,12847,'Howrah - Digha SUPER AC Express','Howrah','Digha') ON DUPLICATE KEY UPDATE Train_No =12847"

                qry2="INSERT INTO avail_Train  VALUES  (1002,12009,'Mumbai Central - Ahmedabad Shatabdi Express','Mumbai','Ahmedabad') ON DUPLICATE KEY UPDATE Train_No =12009"

                qry3="INSERT INTO avail_Train  VALUES  (1003,120010,'New Delhi - Lucknow Jn Swarn Shatabdi Express','New Delhi'  ,'Lucknow ') ON DUPLICATE KEY UPDATE Train_No=120010"

                qry4="INSERT INTO avail_Train  VALUES  (1004,1280050,'New Delhi - Amritsar Shatabdi Express','New Delhi','Amritsa') ON DUPLICATE KEY UPDATE Train_No=1280050"

                qry5="INSERT INTO avail_Train  VALUES  (1005,1282371,'New Delhi - Daurai (Ajmer) Shatabdi Express','New Delhi','Ajmer') ON DUPLICATE KEY UPDATE Train_No=1282371"

                qry6="INSERT INTO avail_Train  VALUES  (1006,1204745,'Howrah - Ranchi Shatabdi Express','Digha','Ranchi') ON DUPLICATE KEY UPDATE Train_No=1204745"

                qry7="INSERT INTO avail_Train VALUES  (1007,1284769,'KSR Bengaluru - MGR Chennai Central Shatabdi Expres','Bengaluru','Chennai') ON DUPLICATE KEY UPDATE Train_No=1284769"

                qry8="INSERT INTO avail_Train VALUES (1008,1201789,'New Delhi - Kanpur Central Shatabdi Express','New Delhi','Kanpur') ON DUPLICATE KEY UPDATE Train_No=1201789"

                qry9="INSERT INTO avail_Train  VALUES  (1009,100052,'MGR Chennai Central - Coimbatore Shatabdi Express','Chennai','Coimbatore') ON DUPLICATE KEY UPDATE Train_No=100052"

                qry10="INSERT INTO avail_Train  VALUES  (1010,1286565,'New Delhi - Chandigarh Shatabdi Express','New Delhi','Chandigarh') ON DUPLICATE KEY UPDATE Train_No=1286565"

                qry11="INSERT INTO avail_Train VALUES   (1011,101285,'Pune - Secunderabad Shatabdi Express','Pune ','Secunderabad') ON DUPLICATE KEY UPDATE Train_No=101285"

                qry12="INSERT INTO avail_Train  VALUES (1012,100212,'New Delhi - Firozpur Cantt Shatabdi Express','New Delhi','Firozpur')  ON DUPLICATE KEY UPDATE Train_No=100212"

                qry13="INSERT INTO avail_Train  VALUES (1013,130201,'New Delhi - Jammu Tawi Rajdhani Express','New Delhi','Jammu ')  ON DUPLICATE KEY UPDATE Train_No=130201"

                qry14="INSERT INTO avail_Train  VALUES  (1014,111000,'KSR Bengaluru - Hazrat Nizamuddin Rajdhani Express','Bengaluru','Hazrat Nizamuddin') ON DUPLICATE KEY UPDATE Train_No=111000"

                qry15="INSERT INTO avail_Train  VALUES  (1015,100005,'M.G.R Chennai Central - Hazrat Nizamuddin Rajdhani E','Chennai','Hazrat Nizamuddin')  ON DUPLICATE KEY UPDATE Train_No=100005"

                qry16="INSERT INTO avail_Train  VALUES (1016,104040,'New Delhi - Ranchi Rajdhani Express','New Delhi','Ranchi')  ON DUPLICATE KEY UPDATE Train_No=104040"

                qry17="INSERT INTO avail_Train  VALUES (1017,121546,'MGR Chennai Central - Thiruvananthapuram Central','Chennai','Thiruvananthapuram')  ON DUPLICATE KEY UPDATE Train_No=121546"

                qry18="INSERT INTO avail_Train   VALUES( 1018,141524,'Mumbai LTT - Haridwar AC Express (PT)','Mumbai','Haridwar')  ON DUPLICATE KEY UPDATE Train_No=141524"

                qry19="INSERT INTO avail_Train  VALUES (1019,152634,'Bhuj - Mumbai Bandra (T.) AC SuperFast Express','Bhuj ','Mumbai') ON DUPLICATE KEY UPDATE Train_No=152634"

                qry20="INSERT INTO avail_Train  VALUES (1020,136524,'Lucknow - New Delhi AC Superfast Express','Lucknow','New Delhi') ON DUPLICATE KEY UPDATE Train_No=136524"

                qry31="INSERT INTO avail_Train VALUES (1021,1201546,'Nagpur - Amritsar AC SF Express','Nagpur','Amritsar') ON DUPLICATE KEY UPDATE Train_No=1201546"

                qry32="INSERT INTO avail_Train  VALUES (1022,126352,'Arunachal AC SF Express','New Delhi','Itanagar')  ON DUPLICATE KEY UPDATE Train_No=126352"

                qry33="INSERT INTO avail_Train  VALUES (1023,104152,'Darshan Express','Howrah','Digha')  ON DUPLICATE KEY UPDATE Train_No=104152"

                qry34="INSERT INTO avail_Train  VALUES (1024,100525,'Visakhapatnam - Secunderabad AC SF Express','Visakhapatnam','Secunderabad')  ON DUPLICATE KEY UPDATE Train_No=100525"

                qry35="INSERT INTO avail_Train  VALUES (1025,100121,'Patna - Ranchi AC Express','Patna','Ranchi')  ON DUPLICATE KEY UPDATE Train_No=100121"

                qry36="INSERT INTO avail_Train  VALUES (1026,114754,'Barmer - Yesvantpur AC Express','Barmer','Yesvantpur')  ON DUPLICATE KEY UPDATE Train_No=114754"

                qry37="INSERT INTO avail_Train  VALUES  (1027,128474,'Jammu Tawi - Ahmedabad Express','Jammu Tawi','Ahmedabad')  ON DUPLICATE KEY UPDATE Train_No=128474"

                qry38="INSERT INTO avail_Train  VALUES (1028,128654,'Jammu Tawi - Guwahati Amarnath Express (PT)','Jammu Tawi','Guwahati')  ON DUPLICATE KEY UPDATE Train_No=128654"

                qry39="INSERT INTO avail_Train  VALUES (1029,1280417,'Bandra Terminus - Gorakhpur Avadh Express (PT)','Mumbai','Gorakhpur')  ON DUPLICATE KEY UPDATE Train_No=1280417"

                qry40="INSERT INTO avail_Train  VALUES (1030,124557,'Dibrugarh - Amritsar Weekly Express (PT)','Dibrugarh','Amritsar')  ON DUPLICATE KEY UPDATE Train_No=124557"

                crs.execute(qry1)

                crs.execute(qry2)

                crs.execute(qry3)

                crs.execute(qry4)

                crs.execute(qry5)

                crs.execute(qry6)

                crs.execute(qry7)

                crs.execute(qry8)

                crs.execute(qry9)

                crs.execute(qry10)

                crs.execute(qry11)

                crs.execute(qry12)

                crs.execute(qry13)

                crs.execute(qry14)

                crs.execute(qry15)

                crs.execute(qry16)

                crs.execute(qry17)

                crs.execute(qry18)

                crs.execute(qry19)

                crs.execute(qry20)

                crs.execute(qry31)

                crs.execute(qry32)

                crs.execute(qry33)

                crs.execute(qry34)

                crs.execute(qry35)

                crs.execute(qry36)

                crs.execute(qry37)

                crs.execute(qry38)

                crs.execute(qry39)

                crs.execute(qry40)

                mydb.commit()

                

                

                crs.close()

               

                print("""  

                    _____         ___   _____   ____                ____   ____   _____                 ____           _____

                      |   |\   | |   \    |    |    | |\   |       |    | |    |    |    |     |    |  |    | \     / |     |

                      |   | \  | |    |   |    |____| | \  |       |____| |____|    |    |     |    |  |____|  \___/  |_____

                      |   |  \ | |    |   |    |    | |  \ |       |\     |    |    |    |     | /\ |  |    |    |          |

                    __|__ |   \| |___/  __|__  |    | |   \|       | \    |    |  __|__  |____ |/  \|  |    |    |    |_____|

                   __________________________________________     ____________________________________________________________

                                        

                       """)



                d=datetime.date.today()

                t=datetime.datetime.now()

                print(" ")

                print(" ")

                print("     DATE:-",d.strftime("%A, %d %B %Y"))

                print(" ")

                print("     TIME:-",t.strftime("%H:%M:%S"))

                print("")

                print('')

                print("    ")

                print("    =================================================================================================================================")

                print("                                                       WELCOME TO RAILWAY RESERVATION PORTAL")

                print("    =================================================================================================================================")

                print("    ")



                while True:



                    print(""" 

                                     *****************************    DASHBOARD    ********************************            

                                             

                                             

                                                         +--------------------------------+

                                                         |           1.Passenger          |

                                                         +--------------------------------+         

                                                         +--------------------------------+

                                                         |           2.EXIT               |

                                                         +--------------------------------+                                           """)

                    break

                e=input(" ||  **SELECT** || :-")





                def railsmenu():

                                print("""

                    

                                       +====================================+  

                                       |      ****  MAIN MENU  ****         |

                                       +====================================+

                                       |                                    |      

                                       |  1. Ticket Booking                 |

                                       |  2. Train_btw_Stations             |   

                                       |  3. Train List                     |

                                       |  4. Your Ticket                    |                                     

                                       |  5. Ticket Cancellation            |

                                       |  6. Analytics                      |

                                       |  7. Exit                           |

                                       |                                    |         

                                       |                                    |

                                       +====================================+

                                  """)

                                    #break

                                x=int(input("""YOUR OPTION:-"""))



                                if x==1:

                                        ticket_booking()



                                elif x==2:

                                          print(" ")

                                          print(btw_Stations())



                                elif x==3:

                                          print(" ")

                                          print("-----FOLLOWING TRAINS ARE AVAILABLE-----")

                                          print(" ")

                                          print(Available_ALL_Trains())



                                elif x==4:

                                          print(" ")

                                          print(self_booked_ticket())



                                elif x==5:

                                          print(" ")

                                          print(ticket_cancellation())





                                elif x==6:

                                          print(" ")

                                          print(Analytics())



                                elif x==7:

                                          print(" ")

                                          print("\n"

                                                  "      \n"

                                                  "          ##======================================================##\n"

                                                  "          ||                      THANK YOU                       ||\n"

                                                  "          ##======================================================##\n"

                                                                                                                              "\n")

                                          print('''

                        

                                                   DEVELOPED BY syed

                                                ''')





                                else:

                                     print(" ")

                                     print("~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")

                                return("")





                def ticket_booking():

                    import mysql.connector

                    mydb=mysql.connector.connect(host='localhost',

                                                 user='root',

                                                 password="mysql",

                                                 database='railway')

                    crs=mydb.cursor()

                    mydb.autocommit=True

                    Psn_Name=input('Enter  Name.:')

                    Psn_Ph=input('Enter  Phone No.:')

                    Psn_Ph_no=str(Psn_Ph)

                    Psn_age=int(input('Enter age.:'))

                    print()

                    print('               M=MALE','\t','F=FEMALE','\t','N=NOT TO MENTION')

                    while True:

                        Psn_gender=input('Enter  Gender M/F:')

                        if Psn_gender==("M") or Psn_gender==("F"):

                            break

                        else:

                            print("        !~!~!~~ M\F only ~~!~!~!~")

                    Gender=Psn_gender.upper()

                    print()

                    print('Journey Details__')

                    Train_from=input('       From Station.:')

                    Train_to=input('       Destination.:')

                    Scheduled_Date=input('Enter Date of Journey (YYYY-MM-DD):')



                    Pnr_Number="10"+str(Psn_age)+str(rd.randint(100000,999999))

                    Email_ID=input("Enter the Email_ID :")

                    Fare=rd.randint(400,1200)

                    s1="INSERT INTO  Passenger_Details VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                    data=(Pnr_Number,Psn_Name,Psn_Ph_no,Psn_age,Psn_gender,Train_from,Train_to,Scheduled_Date,Email_ID,Fare)

                    crs.execute(s1,(data),)

                    print()

                    print('  ***TICKET BOOKED SUCCESSFULLY***')

                    print("\t","Your Pnr Number is: ", Pnr_Number)

                    return("")





                def Available_ALL_Trains():

                        import mysql.connector as msc

                        mydb=msc.connect(host='localhost',user='root',passwd='mysql',database='railway',allow_local_infile=True)

                        crs=mydb.cursor()

                        mydb.autocommit=True

                        crs.execute("use railway")

                        crs.execute("LOAD DATA LOCAL INFILE 'D:/New folder/TRAIN.csv' into table avail_train fields terminated by ',' lines terminated by '\r\n' ;")

                        qry="Select * from avail_train "

                        crs.execute(qry)                                                                                                                             #Use Command to Upload file |LIST-OF-TRAINS| ---->

                        data1 = crs.fetchall()                                                                                                                       #"LOAD DATA LOCAL INFILE 'C:/Users/Jyoti/Desktop/Yash/Train.csv' into table avail_train fields terminated by ',' lines terminated by '\r\n' ;"



                        df = pd.DataFrame(data1, columns=["Srno","Train_No","Train_Name","Train_from","Train_to",])

                        print(df)

                        mydb.commit()

                        crs.close()

                        return("")



                def btw_Stations():

                        import mysql.connector as msc

                        mydb=msc.connect(host='localhost',user='root',passwd='mysql',database='railway')

                        crs=mydb.cursor()

                        mydb.autocommit=True

                        crs.execute("use railway")



                        Sr_train=input("Enter the Source Station.:")

                        De_train=input("Enter the Destination Station.:")

                        qry='select * from avail_train WHERE TRAIN_NO = 12009'

                        crs.execute(qry,)

                        data=crs.fetchall()

                        a=[]

                        for i in data:

                            a.append(i)



                        if len(a)!=1:

                            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')



                        else:

                            print("")

                            print("")

                            print(a)

                            mydb.commit()

                            df = pd.DataFrame(data, columns=["Srno","Train_No","Train_Name", "Train_from" ,  "Train_to"])



                            #print(df)

                            mydb.commit()

                            crs.close()

                        return("")



                def self_booked_ticket():

                        import mysql.connector as msc

                        mydb=msc.connect(host='localhost',user='root',passwd='mysql',database='railway')

                        crs=mydb.cursor()

                        mydb.autocommit=True

                        Self_Pnr=int(input('Enter your Pnr_number No:'))

                        crs.execute('select * from passenger_details where Pnr_Number=(%s)',(Self_Pnr,))

                        data=crs.fetchall()

                        a=[]

                        for i in data:

                            a.append(i)



                        if len(a)!=1:

                            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')



                        else:

                            print(a)

                            mydb.commit()

                        return("")



                def ticket_cancellation():

                        import mysql.connector as msc

                        mydb=msc.connect(host='localhost',user='root',passwd='mysql',database='railway')

                        crs=mydb.cursor()

                        mydb.autocommit=True

                        crs.execute("use railway")

                        Self_Pnr=int(input("Enter Your Pnr_Number.:"))

                        Self_Name=input("Enter Your Name.:")

                        Self_Phno=int(input("Enter You Phone no.:"))

                        #qry='DELETE FROM passenger_details WHERE Pnr_Number=(%s) or Psn_Name=(%s) or Psn_Ph_no=(%s)'



                        s=input("ARE YOU SURE  YOU WANT TO CANCEL THE TICKET (YES/NO): ")

                        a=[]

                        for i in s:

                            a.append(i)



                        if len(s)==3:

                           crs.execute('DELETE FROM passenger_details WHERE Pnr_Number=(%s) or Psn_Name=(%s) or Psn_Ph_no=(%s)',(Self_Pnr,Self_Name,Self_Phno,))



                        else:

                             print("         Ticket NOT Cancelled")



                        print("")

                        print("        Your Ticket is Cancelled")

                        return("")



                def Analytics():

                         print("""

                    

                                      +=====================================================+  

                                      |                ****  MAIN MENU  ****                |

                                      +=====================================================+

                                      |                                                     |      

                                      |  1. BAR PLOT :-   Fare  of  Passengers              |

                                      |  2. LINE PLOT :-  AC Fare  Of  Trains               |

                                      |  3. BAR PLOT :-   Sleeper Fare Of  Trains           |

                                      |  4. LINE PLOT :-  Average Distance Covered By Train |

                                      |                                                     |                                                  

                                      +=====================================================+

                                  """)

                         opt=int(input("""       YOUR OPTION:-"""))



                         if opt==1:

                                         print(" ")

                                         print(bar_plot())



                         elif opt==2:

                                          print(" ")

                                          print(line_plot())



                         elif opt==3:

                                          print(" ")

                                          print(barh_plot())



                         elif opt==4:

                                          print(" ")

                                          print(line1_plot())



                         else:

                                     print(" ")

                                     print("~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")











                def  bar_plot():

                                    plt.figure(figsize=(9,6))

                                    plt.bar(x=["MOHAN","ROHIT","CARL","MARK","VON","RONIT","SUNIT"],

                                    height=[720,452,1123,558,320,750,950],color='midnightblue')

                                    plt.xticks(rotation=45)

                                    plt.title("Fare of Passengers")

                                    plt.savefig("Fare of Passengers.png")

                                    plt.show()

                                    return("")



                def line_plot():

                                    print("Line Plot")

                                    x=["Goa Express","JammuTavi Superfast","Punjab Mail Express","Dakshin Express","Delhi-Mumbai Shatabdi"]

                                    y=[4500,8500,3600,7600,12000]

                                    plt.title("AC Fare Of Trains",fontsize=14,color="g")

                                    plt.xlabel("Trains",fontsize=14,color="g")

                                    plt.ylabel("AC Fare",fontsize=14,color="g")

                                    plt.xticks(rotation=12)



                                    plt.plot(x,y, marker="X",ls="dashed",linewidth=4, color="m")

                                    plt.savefig("AC Fare For Trains.png")

                                    plt.show()

                                    return("")



                def barh_plot():

                                    print("Horizontal Bar Plot")

                                    x=["Goa Express","JammuTavi Superfast","Punjab Mail Express","Dakshin Express","Delhi-Mumbai Shatabdi"]

                                    y=[1500,4500,2600,7600,9000]

                                    plt.title("Sleeper Fare  Of  Trains",fontsize=14,color="b")

                                    plt.xlabel("Trains",fontsize=14,color="c")

                                    plt.ylabel("Sleeper Fare",fontsize=14,color="c")

                                    plt.barh(x,y, color="y", edgecolor="pink")

                                    plt.savefig("Sleeper Fare Of Trains.png")

                                    plt.show()

                                    return("")



                def line1_plot():

                                    print("Line Plot")

                                    x=["Goa Express","JammuTavi Superfast","Punjab Mail Express","Dakshin Express","Delhi-Mumbai Shatabdi"]

                                    y=[500,1200,650,750,1350]

                                    plt.title("Average Distance Covered By Train",fontsize=14,color="c")

                                    plt.xlabel("Trains",fontsize=14,color="c")

                                    plt.ylabel("(Distance in Kms)",fontsize=14,color="r")

                                    plt.plot(x,y, marker="o", label="Avg Distance")

                                    plt.xticks(rotation=17)

                                    plt.legend()

                                    plt.savefig("Avearage Distance By Trains.png")

                                    plt.show()

                                    return("")





                if e=="1" :

                    print(railsmenu())

                elif e=="2":

                        print(" ")

                        print("\n"

                              "      \n"

                              "          ##======================================================##\n"

                              "          ||                      THANK YOU                       ||\n"

                              "          ##======================================================##\n"

                              "\n")

                        print('''

                        

    DEVELOPED BY RINI

                        ''')





                else:

                        print(" ")

                        print("~!~!~!~PLEASE ENTER 1 OR 2~!~!~!~")

                mydb.close()

       except():

                   pass

    else:

            print("Password is incorrect,\nPlease enter the correct password.")

            a2=str(input("Enter any number to again apply for password or press any alphabet to exit:"))

            print()

            if a2.isalpha():

                print("Thanks for using our service.")

                break
