def highest():
    subjects = {}

    while True:
        subject = input("Enter subject: ")
        score = int(input("Enter score: "))

        subjects[subject] = score

        if input("Continue? (yes/no): ").lower() == "no":
            break

    highest_score = max(subjects.values())

    result = []

    for subject, score in subjects.items():
        if score == highest_score:
            result.append(subject)

    return result, highest_score


subjects, score = highest()

print("Highest score:", score)
print("Subjects:")
for subject in subjects:
    print(subject)