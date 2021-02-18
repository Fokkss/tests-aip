school = {"1": 33, "7": 26, "9": 22, "11": 11}
q = 0
while q == 0:
    for i in input("1 - change, 2 - add, 3 - delete, 4 - quantity of all, 0 - finish: "):
        if i == "1":
            clas = input("class: ")
            child = int(input("how many child: "))
            school[clas] = child
        elif i == "2":
            clas = input("class: ")
            child = int(input("how many child: "))
            school[clas] = child
        elif i == "3":
            clas = int(input("class: "))
            del school[clas]
        elif i == "4":
           quannn = sum(school.values())
           print(quannn)
        elif i == "0":
            q = 1
            print("end")
        else:
            print("another one")
        print(school)
