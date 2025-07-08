cop=[]
liste=[]
while True:
    a = input("\t \t*********\n 1.Adding new student names\n 2.updating existing student name\n 3.Deleting student names\n 4.Listing all student names\n 5.swapping student names\n q quit the program")
    if a not in ["1","2","3","4","5","q"]:
        print("please answer the questions")
        continue
    elif a == "q":
        break
    elif a == "1":
        b=input("are you sure you want to add a new student? (y for yes, n for no)")
        b.lower()
        if b == "y":
            ab=(input("what is the students name?"))

            liste.append(ab)
        elif b == "n":
            continue
    elif a == "2":
        ac=input("Do you want to update a student in the list? (y for Yes / n for No) ")
        ac.lower()
        if ac == "y":
           av=input("which student you want to update?")
           ap = input("which student you want to update with?")
           if av  not in liste:
               print("please say a valid student name")
               continue
           elif av    in liste:
               index = liste.index(av)
               liste[index] = ap
    elif a == "3":
            c=(input("what you want to delete say name."))
            if c not in liste:
                print("this name is not in your list")
            elif c in liste:
                    liste.remove(c)
    elif a == "5":
        print("you can swap your students now, which one you would swap? say the 2 number only.")
        print(liste)
        d=int(input("what is the first numbers place whit numbers."))
        e=int(input("what is the second numbers place whit numbers."))
        liste[d-1], liste[e-1]=liste[e-1], liste[d-1]
    elif a == "4":
        print(liste)