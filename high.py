#looking for the high score in a sujects
def high():
    subjects = {}

    while True:
        subject = input("Your subject: ")
        value = int(input("Your value: "))
        subjects[subject] = value

        if input("Continue? (y/n): ").lower() == "n":
            break

    max_value = max(subjects.values())
    max_subjects = [s for s, v in subjects.items() if v == max_value]

    return max_subjects, max_value

subjects, value = high()
print(subjects, value)