name = input("what is your name?")
"""
if name == "harry" or name =="hermonie" or name =="ron":
    print("gryffindor")
elif name == "draco":
    print("slytherin")
else:
    print("who?")"""

match name:
    case "harry"|"hermonie"|"ron":
        print("gryffindor")
   
    case "Draco":
        print("sltherin")
    case _ : # whatever case it had not been handled
        print("who?")



    