print("Student Test Marks Averge And Grade Calculate:")
sub_cnt = int(input("Enter Subjects count : "))

marks = []

for i in range(sub_cnt):
    sub_mark = int(input(f"Enter subjet {i + 1} marks :"))
    marks.append(sub_mark)

print(f"Student Mark list : {marks}")

avg = sum(marks) / len(marks)

print(f"Your average mark is : {avg} for {sub_cnt} subjects \n")

if avg >= 90:
    print("Well done A Grade \n")
elif avg >= 80:
    print("Good Job B Grade \n")
elif avg >= 60 :
    print("Try to best C Grade \n")
elif avg >= 50:
    print("Focus on your studies D Grade \n" )
else:
    print("Youu are Fail in the Test F Grade\n")

print("Try Again")