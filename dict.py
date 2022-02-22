print("1.To append a record")
print("2.To search a record")
print("3.To read and display all records")
print("4.To exit")
import pickle
record={}
while True:
    ch=int(input("Enter your choice:"))
    if ch==1:
        while True:
            empid=int(input("Enter employee id:"))
            empname=input("Enter name of employee:")
            salary=int(input("Enter the salary of employee:"))
            data=[empid,empname,salary]
            record.append(data)
            choice=input("wish to continue(Y/N):")
            if choice=='n' or choice=='N':
                break
        f=open("Flight.dat",'wb')
        pickle.dump(record,f)
        print("Record added successfully")
        f.close()
    elif ch==2:
        f=open("Flight.dat",'rb+')
        flirec=pickle.load(f)
        found=0
        fno=int(input("Enter the flight id to be deleted:"))
        for r in flirec:
            if r[0]==fno:
                flirec.remove(r)
                found=1
                break
        if found==0:
             print("Sorry record not found")
        elif found==1:
            f.seek(0)
            pickle.dump(flirec,f)
            print("Flight record deleted")
        f.close()
    elif ch==3:
        f=open("Flight.dat",'rb')
        flirec=pickle.load(f)
        print("Contents of flight record are:")
        for i in flirec:
            fid=i[0]
            fname= i[1]
            pas= i[2]
            print(fid,fname,pas)
        f.close()
    elif ch==4:
        print("bye")
        break
    else:
        print("Invalid choice")
        

        
           
