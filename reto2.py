# defining variables to save the data entered by the user

# name = input('Ingresa tu nombre: ')
# lastName = input('Ingresa tu apellido: ')
age = int(input('Ingresa tu edad en años: '))
examScore = int(input('Ingresa el puntaje(en números enteros) que obtuvo en el examen de ingreso : '))
familySalary = float(input('Ingresa el número(en decimales) de salarios mínimos mensuales que gana su familia: '))

# Condition for calculed discount for age
if age >= 15 and age <= 18:
  discountAge = 25
elif age >= 19 and age <= 21:
  discountAge = 15
elif age >= 22 and age <= 25:
  discountAge = 10
else:
  discountAge = 0

#print the name and last name of candidate
# print('\n', name, lastName)

#print the discunt for age of the candidated
print(discountAge)

# Condition for calculed discount by exam score
if examScore >= 80 and examScore < 86:
  discountExam = 30
elif examScore >= 86 and examScore < 91:
  discountExam = 35
elif examScore >= 91 and examScore < 96:
  discountExam = 40
elif examScore >= 96 and examScore <= 100:
  discountExam = 45
else:
  discountExam = 0

#print the discunt by exam score of the candidated
print(discountExam)

# Condition for calculed discount by family salary
if familySalary <= 1:
  discountSalary = 30
elif familySalary > 1 and familySalary <= 2:
  discountSalary = 20
elif familySalary > 2 and familySalary <= 3:
  discountSalary = 10
elif familySalary > 3 and familySalary <= 4:
  discountSalary = 5
else:
  discountSalary = 0

# print the discunt by family salary
print(discountSalary)

# Calculating the total discount the candidate will receive
totalDiscount = discountAge + discountExam + discountSalary

# print the total discount
print(totalDiscount)