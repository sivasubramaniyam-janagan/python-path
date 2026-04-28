class Student:
    def __init__(self,name,_id,age):
        self.name=name
        self._id=_id
        self.age=age

#--------------------------------------------------------------------------------------------

def viewstudent():
    file=open("data.txt","r")
    content=file.read()
    print(content)
    file.close()

#--------------------------------------------------------------------------------------------

def addstudent():
    file=open("data.txt","a")
    
    print("Enter Details")
    name=input("Enter name  >  ")
    _id=input("Enter id  >  ")
    age=input("Enter age  >  ")
    file.write(name+" "+_id+" "+age+"\n")
    file.close()

#--------------------------------------------------------------------------------------------

def searchstudent():
    students=[]
    file=open("data.txt","r")
    for line in file:
        parts=line.split()
        name=parts[0]
        _id=parts[1]
        age=parts[2]
        students.append(Student(name,_id,age))
    f=0
    try:
        ID=input("Enter ID >>   ")
    except Exception as e:
         print (e)
    else:
        for student in students:
            if(ID==student._id):
                print("matched")
                print(student.name)
                f=1
    if(f==0):
        print("not found")
                
    file.close()          



#--------------------------------------------------------------------------------------------


def deletestudent():
    students=[]
    file=open("data.txt","r")
    for line in file:
        parts=line.split()
        name=parts[0]
        _id=parts[1]
        age=parts[2]
        students.append(Student(name,_id,age))
    file.close()

    f=0
    try:
        ID=input("Enter ID  to delete>>   ")
    except Exception as e:
         print (e)
    else:
        for student in students:
            if(ID==student._id):
                print("Deleting ....")
    
                print(student.name)
                students.remove(student)
                print("sucess")
                f=1
                file=open("data.txt","w")
                for student in students:
                    file.write(student.name+" "+student._id+" "+student.age+"\n")
                file.close()
    if(f==0):
        print("not found")

    
        
    
        


#--------------------------------------------------------------------------------------------

def option(a):
    match a :
        case 1:
            addstudent()
        case 2:
            viewstudent()
        case 3:
            searchstudent()
        case 4:
            deletestudent()
        case 0:
            print("thank you ....")
            exit()
        case _:
            print("invalid choice")
    

#------------------------------------------------------------------

print("Student management system")
while(True):
    print("choose option")
    print("1 . Add Student")
    print("2 . View Student")
    print("3 . Search Student")
    print("4 . Delete Student")
    print("0 . Exit")

    try:
        a=int(input(">>>    "))
    except Exception as e:
        print ("somthing went wrong",e)
    else:
        option(a)

#--------------------------------------------------------------------------------------------
