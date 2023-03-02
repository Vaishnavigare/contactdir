'''
main file
=========
'''
def validate_mob(x):
    if x.isdigit() and len(x)==10:
        return 1
    else:
        return 0
def create_contact():    
        fp=open('data.txt','a')
        n=input("Enter Name:")
        mn=input("Enter mobile number:")
        res=validate_mob(mn)
        #print(res)
        if res==1:
           a,b=searchmob(mn)
           if b==1:
               print()
               print("Number Already Exist")
               
           else:
                d=n+":"+mn+"\n"
                fp.write(d)
                fp.close()
                print("contact created successfully!!")
        else:
            print("please enter a valid mobile number")

def searchmob(n):
    
    fp=open('data.txt','r')
    data=fp.readlines()
    for x in data:
       l=x.split(":")
       if int(n)==int(l[1]):
         #print("Contact found")
         #print(x)
         return x,1
    else:
         return ' ',0            
def display():
    fp=open('data.txt','r')
    d=fp.read()
    print("============Contact Directory================")
    print()
    print(d)
    print("=============================================")
def searchname():
  print("Search contact number by name:")
  ns=input("Enter name:")
  fp=open('data.txt','r')
  data=fp.readlines()
  # print(data)
  flag=0
  for x in data:
    # print(x)
    l=x.split(":")
    #print(l)
    #print(l[0])
    if ns.upper()==l[0].upper():
       print(x)
       flag=1
       if flag==0:
          print("Contact not found")
          fp.close()
print("Welcome to Contact Directory console Application")
print()
while True:
    print("1.Create contact")
    print("2.View Contact")
    print("3.Search by Name")
    print("4.Search by Mobile Number")
    print("5.Exit")
    ch=int(input("Enter your choice:"))

    if ch==1:
        create_contact()
    elif ch==2:
        display()
    elif ch==3:
        searchname()
        
    elif ch==4:
        ms=input("Enter mobile number to be searched:")
        a,b=searchmob(ms)
        print(a)
        print(b)
        if b==1:
            print("number Found")
            print(a)
        else:
            print("Not Found")
            print()
    elif ch==5:
        break
    else:
        print("Please Enter valid option!!!")

print("Thank you for using Application")






