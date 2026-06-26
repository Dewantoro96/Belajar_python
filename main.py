def highest () :
    subjects = {}
    while True:
        data1 = input("enter subject = ")
        data2 = int(input("enter the value = "))
        subjects.update({
            data1 : data2
        })
        enough = input("is enough ? 'yes/no' =  ")
        if enough == "no":
            continue
        elif enough == "yes":
            break
    return subjects



print(highest())