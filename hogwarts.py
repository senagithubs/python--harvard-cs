#lists
students = ["hermonie","harry","ron"]

#print(students)

#if u just wanna spesific value:
""""
print(students[1]) # it print outs only harry

print(students[0])
print(students[1])
print(students[2])
"""
"""
for student in students:
    print(student) #it initalizes automaticly

"""
#for i in range(students): # students is not an integer. range expects an integer
# for this we will use len function
"""
for i in range(len(students)):
    print(students[i])
"""
"""
for i in range(len(students)):
    print(i+1,students[i])   # we ranked students
"""
#dict : data structure that allows u to associate one value with another, just like an dictionary
"""

students =["hermonie","harry","ron","draco"]
houses = ["gryffindor","gryffindor","gryffindor","slytherin"]

"""

students ={   # keys on the left values on the right
    "hermonie":"gryffindor",
    "harry":"gryffindor",
    "ron":"gryffindor"
    ,"draco":"slytherin",
    
    
    
    }
"""
print(students["hermonie"])
print(students["harry"])
print(students["ron"])
print(students["draco"])
"""


# how to make it more dynamicly?
"""
for student in students:
    print(student)  # it gives ua only keys, iwanna see houses too."""
"""""
for student in students:
    print(student,students[student] ,sep =",") """

# what if we have lots of datas about students?

# we should think like each of those students itselfs are dictionary

students = {
    {"name":"hermonie" ,"house":"gryffindor","patronus":"otter"},
    {"name":"harry","house":"gryffindor","patronus":"stag"},

    {"name":"ron","house":"gryffindor","patronus":"jack russel teerier"},
     {"name":"draco","house":"slytheri","patronus":None}# we used None keyword

}

for student in students:
    print(student["name"],student["house"],student["patronus"],sep=",")
    