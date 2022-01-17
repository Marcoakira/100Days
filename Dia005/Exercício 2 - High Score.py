# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

mais_alto = 0

for m in student_scores:
  if m > mais_alto:
    mais_alto = m

print(f'The highest score in the class is: {mais_alto}')
