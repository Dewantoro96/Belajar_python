#looking for the high score in a sujects

def highest () :
    subjects = {}
    while True:
        data1 = input("enter subject = ")
        data2 = int(input("enter the value = "))
        subjects.update({
            data1 : data2
        })
        CONTINUE = input("continue ? 'yes/no' =  ").lower()
        if CONTINUE == "no":
            break
    list_score = []
    score_high = max(subjects.values())
    for SUBJECTS , SCORE in subjects.items():
        if SCORE >= score_high:
            list_score.append(SUBJECTS)
    return (f"result subjects with score highest : {list_score}, {score_high}")

print(highest())