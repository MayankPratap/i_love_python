"""  This example contains two types of classes - Person and MNNITPerson

     MNNIT Person derives all attributes of Person like name and birthday but has some of its own attributes like id .
     
"""     


import datetime

class Person(object):

    def __init__(self,name):
        self.name=name
        self.birthday=None
        self.lastName=name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def setBirthday(self,month,day,year):
        self.birthday=datetime.date(year,month,day)

    def getAge(self):
        if self.birthday==None:
            raise ValueError

        return (datetime.date.today()-self.birthday).days

    def __lt__(self,other):
        return self.name<other.name


    def __str__(self):
        return self.name

"""
me=Person("Mayank Pratap Singh")
print me

test="Mayank Pratap Singh"
#test.split(" ")
print test.split(" ")[-1]


print me.getLastName()
me.setBirthday(6,29,1996)
print me.getAge()

other=Person("Sunil Sangwan")
print other

print other.getLastName()
other.setBirthday(7,7,1997)

print other.getAge()

plist=[me,other]

for p in plist: print p

plist.sort()

for p in plist: print p"""

class MNNITPerson(Person):
    nextIdNum=0      # Class variable , same for every object f this class
 
    def __init__(self,name):
        Person.__init__(self,name) # Initialise Person attributes
        
        self.idNum=MNNITPerson.nextIdNum
        MNNITPerson.nextIdNum+=1

    def getIdNum(self):
        return self.idNum


    # Sorting MNNIT People using their ID number , not name!

    def __lt__(self,other):
        return self.idNum<other.idNum

p1=MNNITPerson('Mayank Pratap')
p2=MNNITPerson('Narendra Pal')
p3=MNNITPerson('Sunil Sangwan')
p4=Person('Amit Kumar Yadav')


print p1

print p1.getIdNum()

print p2.getIdNum()

print p1<p2

print p3<p2

print p4<p1

print p1<p4
