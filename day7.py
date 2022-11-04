# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
student_count = 0;
student_heights_sum = 0;

for student in student_heights:
    student_count += 1
    student_heights_sum += student

print(int(student_heights_sum/student_count))
