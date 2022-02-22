f=open("data.txt",'w')
print("STORY CREATION")
while True:
    a=input("enter line:")
    f.write(a)
    f.write('\n')
    ch=input("wish to continue(y/n):")
    if ch=='n':
        break
f.close()
f=open("data.txt",'r+')
f.seek(0)
w=input("enter the word to be counted:")
c=0
for data in f:
        words=data.split()
        for j in words:
             if j==w:
                c+=1
print("The frequency of ",w,"in the story is",c)
import random
f.seek(0)
dat=f.readlines()
n=random.randrange(0,len(dat))
print("Random line : ",dat[n])
f.close()
