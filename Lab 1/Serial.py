import pickle
class Student:
   def __init__(self, name, age):
       self.name=name
       self.age=age

Student1 = Student("Sita", 26)
Student2 = Student("Gita", 24)
print "First students name : ", Student1.name
print "Second students name : ",Student2.name
pickled_S1=pickle.dumps(Student1)
pickled_S2=pickle.dumps(Student2)
print("The serialised objects look like this")
print(pickled_S1)
print(pickled_S2)
f = open("s1file", "a")
f.write(pickled_S1)
g = open("s2file", "a")
g.write(pickled_S2)
h = open("s1file", "r")
i = open("s2file", "r")
buff1 = h.read()
buff2 = i.read()
print("Raw unpickled files look like this : ")
unpickled_S1 = pickle.loads(buff1)
unpickled_S2 = pickle.loads(buff2)
print(unpickled_S1)
print(unpickled_S2)
print("extracted data looks like this : ")
print "Student1 name : ", unpickled_S1.name
print "Student1 age : ", unpickled_S1.age
print"Student2 name : ", unpickled_S2.name
print"Student2 age : ", unpickled_S2.age
