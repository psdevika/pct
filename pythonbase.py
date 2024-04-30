def create():
        print("to create blogs")
        cr2=input("Go back to previous page")
        if cr2=='':
          select()
        hp1=input("Go to HOME PAGE")
        if hp1=="":
           homepage()

def read():
        print("to read blogs")
        re1=input("Go back to previous page")
        if re1=='':
           select()
        hp1=input("Go to HOME PAGE")
        if hp1=="":
           homepage()

def profile():
       print("profile")
       pr1=input("Go back to previous page")
       if pr1=='':
           select()
       hp=input("Go to HOME PAGE")
       if hp=="":
          homepage()

def select():
    print("1. create \n 2. read\n 3. Profile ")
    a5=int(input(" enter your choice "))
    if a5 ==1:
        create()
    elif a5 == 2:
         read()
    elif a5 == 3:
        profile()
    else:
        print(" enter valid choice ")
    hp=input("Go to HOME PAGE")
    if hp=="":
        homepage()


def categorymng():
        print("you can add or remove any category if you want")
        print("enter the category you wanted to add ")
        print(" select the category you want to remove ")
        ca1=input("Go back to DASHBOARD")
        if ca1=='':
           dashboard()
        hp=input("Go to HOME PAGE")
        if hp=="":
           homepage()

def profilemng():
          print(" to manage profile")
          pr1=input("Go back to DASHBOARD")
          if pr1=='':
            dashboard()
          hp=input("Go to HOME PAGE")
          if hp=="":
             homepage()

def commentmng():
     print("comment")
     co1=input("Go back to DASHBOARD")
     if co1=='':
        dashboard()
     hp=input("Go to HOME PAGE")
     if hp=="":
        homepage()

def dashboard():
           print("  ADMIN PANEL")
           print("_______________")
           print("DASHBOARD")
           print("\n\n")
           print(" what you wanted to manage ")
           print(" 1. Category \n 2. Profile \n 3.Commands")
           a4 = int(input("enter your choice "))
           if a4==1:
              categorymng()
           elif a4==2:
               profilemng()
           elif a4==3:
               commentmng()
           else:
               print(" enter valid choice ")
           hp=input("Go to HOME PAGE")
           if hp=="":
               homepage()

def admin():
     print("Enter the password to log in to the ADMIN PANEL \n (Remember you have only 3 chances to login ) ")
     num=1
     while num<=3:
         a2 = int(input("Enter the password here"))
         if a2 == 1234:
             dashboard()
         num=num+1
     print("password is incorrect")
     hp=input("Go to HOME PAGE")
     if hp=="":
        homepage()

def user():
    a3 = int(input("enter the password "))
    if a3 == 4321:
       select()
    print("You donot have an account here\n")
    act=input("Enter here to create an account")
    if act =='' :
        print("\n")
    hp=input("Go to HOME PAGE")
    if hp=="":
        homepage()

def homepage():
    print("Enter 1 for logging into Admin panel || Enter 2 for login as a user")
    print("1.ADMIN PANEL")
    print("2.USER")
    a1 = int(input("Enter your choice"))
    if a1==1:
          print("Admin panel")
          admin()
    elif a1==2 :
         print("User")
         user()
    else:
         print("please enter valid choice")
   


home=input("Enter here to go to home page")
if home=='':
   homepage()
