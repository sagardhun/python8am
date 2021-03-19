def subjects():
    sub = []
    j = 1
    number_of_subjects = int(input("Enter the number of subjects:"))
    while j <= number_of_subjects:
        subject = input("Enter the subject name:")
        j += 1
        sub.append(subject)
    return (sub)


# subjects()

def students():
    names = []
    i = 1
    number_of_students = int(input("Enter the number of students:"))
    while i <= number_of_students:
        name = input(f"Enter the name of  the student {i}:")
        i += 1
        names.append(name)
    return (names)


# students()


def mark_obtained():
    subjects()
    students()

    n = len(students())
    m = len(subjects())

    w_mark = []

    x = 0
    y = 0
    while x < n:
        s_mark = []
        print(f"========NAME: {students()[x]}=====")
        while y < m:
            mark = int(input(f"Enter the marks of {subjects()[x]}:"))

            if mark > 100 or mark < 0:
                print("enter valid mark only.")
            else:
                s_mark.append(mark)

            y += 1

        x += 1

    w_mark.append(s_mark)

    print(n)

    return (w_mark)


mark_obtained()

'''
lib-sub=folder
    -test(file)'''


