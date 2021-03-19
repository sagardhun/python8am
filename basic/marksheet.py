students_name = []
tot_marks = []
div = []
percentage = []
marks_list = {}
result = {}
students_marks = []


def get_input():
    no_of_students = int(input('Enter the number of students: '))
    subjects = ['English', 'Nepali', 'Math', 'Computer', 'Science']
    x = 0

    while x < no_of_students:
        marks = []
        print("---------------------------------------")
        total = 0
        percent = 0
        flag = 1
        name = input("Enter the name of the students: ")

        result['name'] = students_name
        students_name.append(name)

        for i in subjects:
            mark = int(input(f"Enter the marks in %s: " % i))
            if mark < 30:
                flag = 0

            # result['marks'] = marks
            marks.append(mark)

        students_marks.append(marks)
        result['Students marks'] = students_marks

        total = sum(marks)
        percent = (total / 500) * 100

        result['total_marks'] = tot_marks
        tot_marks.append(total)

        result['percentage'] = percentage
        percentage.append(percent)

        result['Division'] = div
        if flag != 0:
            if percent >= 90:
                result['division'] = div
                div.append("Out Standing")
            elif 90 >percent >= 80:
                result['division'] = div
                div.append("Distinction")
            elif 80 > percent >= 60:
                div.append("1nd Division")
            elif 60 > percent >= 40:
                div.append("2nd Division")
            elif 40 > percent >= 30:
                div.append("3rd Division")
            else:
                div.append("Fail")
        else:
            div.append("Fail")
        x += 1

    return result


def display():
    get_input()
    for i in result:
        # print(result)
        print(i, "=", result[i])


display()
