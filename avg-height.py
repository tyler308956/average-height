#Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
ele = 0

while(ele < len(student_heights)):
    total_height = total_height + student_heights[ele]
    ele += 1

average_height = round(total_height / len(student_heights))

print(average_height)
