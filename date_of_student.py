def students():
    date_students_list = []
    while True :
        date_students_dict = {}
        date_name = input("enter yor name = ").upper()
        date_id_number = int(input("your number ID student = "))
        date_major = input("your major = ").upper()
        date_place_of_birth = input("place of birth = ").upper()
        date_students_dict.update({
            'NAME'                      : date_name,
            'ID_STUDENT'                : date_id_number,
            'MAJOR'                     : date_major,
            'PLACE_OF_BIRTH'            : date_place_of_birth
        })
        date_students_list.append(date_students_dict)
        input_again = input("again ?(y/n)").lower()
        if input_again == "n" :
            break
    return date_students_list

date = students()
print(f"{'NUMBER':<8}{'NAME':<20}{'ID':<20}{'MAJOR':<18}{'PLACE OF BIRTH':<23}")
NUMBER = 0
for dataset in date :
    NUMBER += 1
    NAME = dataset['NAME']
    ID = dataset['ID_STUDENT']
    MAJOR = dataset['MAJOR']
    PLACE_OF_BIRTH = dataset['PLACE_OF_BIRTH']
    print(f"{NUMBER:^8}{NAME:<20}{ID:<20}{MAJOR:<18}{PLACE_OF_BIRTH:<23}")