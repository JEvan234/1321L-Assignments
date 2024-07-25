#start the program, define the methods
def average(total_grade, number_of_assignments):
    result = total_grade / number_of_assignments
    return result

def weightedpoints(average, catagory):
    match catagory:
        case 1:
            result = average * 0.10
            return result
        case 2:
            result = average * 0.40
            return result
        case 3:
            result = average * 0.20
            return result
        case 4:
            result = average * 0.30
            return result

print("[CSE1321L Grade Calculator]")
print("Labs")
labgrade = 0
labrange = 12
for i in range(1, 13):
    labgrade += int(input("Enter Grade #" + str(i) + ": "))
lab_average = average(labgrade, labrange)
print("Weighted Points: ", end="")
print(str(weightedpoints(lab_average, 1)))
print()
print("Assignments")
Assignmentgrade = 0
assignmentrange = 7
for i in range(1, 8):
    Assignmentgrade += int(input("Enter Grade #" + str(i) + ": "))
assignment_average = average(Assignmentgrade, assignmentrange)
print("Weighted Points: ", end="")
print(str(weightedpoints(assignment_average, 2)))
print()
print("Midterm")
midterm = int(input("Enter Grade #1: "))
print("Weighted Points: ", end="")
print(str(weightedpoints(midterm, 3)))
print()
print("Exam")
exam = int(input("Enter Grade #1: "))
print("Weighted Points: ", end="")
print(str(weightedpoints(exam, 4)))
print()
print("Your final grade for CSE1321L is: ", end="")
final_grade = weightedpoints(exam, 4) + weightedpoints(midterm, 3) + weightedpoints(assignment_average, 2) + weightedpoints(lab_average, 1)
print(str(final_grade))
