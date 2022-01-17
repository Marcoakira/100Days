# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

valor_total = 0
for n in range(0, len(student_heights)):
  valor_total += student_heights[n]

media = valor_total / len(student_heights)

media = int (round(media,0))
print(media)
print(round(media,0))

print(valor_total)
print(type(valor_total))
