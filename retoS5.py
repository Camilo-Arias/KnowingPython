#Defining variables initials
hours = int(input('Ingresa las horas trabajadas esta semana: ')) #Capturing the hours worked by the user
valueHour = int(input('Ingresa el valor de la hora: ')) # Value of the hour
sumDiscounts = 0 # Discount meter

# functions
def calGross(hours, valueHour): #Function to calculate the gross salary, receive as parameter the hour and value of the same
  if hours > 40: # If the hours are greater than 40 it's because he did overtime
    normalHour = 40*valueHour # Value * hours normals = salary basic
    extras = (hours - 40)*(valueHour*1.5) # Hours less 40 = Extras worked and we multiply the result for 1.5 times the value of the time.
    valueGross = extras+normalHour # salary basic + (0 = hours extras) = gross salary
    return [normalHour, extras, valueGross]
  extras = 0
  normalHour = hours*valueHour # Value * hours normals = salary basic
  valueGross = extras+normalHour # salary basic + (0 = hours extras) = gross salary
  return [normalHour, extras, valueGross] # Return the values to the 3 variables to subsequently print the individual values

def discounts(valueGross): #Function to calculate the discounts, receive as parameter the gross salary
  parafiscales = valueGross * 0.09 # gross * 9% = parafiscales
  health = valueGross * 0.04 # gross * 4% = health
  vacations = valueGross * 0.04 # gross * 4% = vacations
  return [parafiscales, health, vacations] # Return the values to the 3 variables to subsequently print the individual values and calculate the total sum

def neto(valueGross, discount): # Function to calculate the neto salary, receive as paratemer the gross salary and total discounts
  valueNeto = valueGross - discount # We subtract the Gross Salary with the total discounts made
  return valueNeto # Return the value of neto salary

def provisions(gross): #Function to calculate the gross salary, receive as parameter the hour and value of the same
  prima = gross * 0.0833 # gross * 8.33% = prima
  cessities = gross * 0.0833 # gross * 8.33% = cessities
  interestCessities = gross * 0.01 # gross * 1% = interes of cessities
  vacations = gross * 0.0417 # gross
  return [prima, cessities, interestCessities, vacations] # return the values to the 4 variables to subsequently print the individual values

# PRITING RESULTS
'''I make an instance of the fuction with the values it requires,
with reference to position 2 that will be the value of the gross salary'''
gross = calGross(hours, valueHour)[2] # The gross variable will be the parameter sent to the following fuctions
listGross = calGross(hours, valueHour) # ListGross is referenced to the list that returns me the function calGross
for printGross in listGross: # I walk the return list
  print(printGross) # Print values of the list

listDiscounts = discounts(gross) # ListDiscounts is referenced to the list that returns me the function discounts
for discounts in listDiscounts: # I walk the return list
  sumDiscounts += discounts # We add the discounts while the list is covered
  print(discounts) # Print the values on the list
print(sumDiscounts) # We printed the sum of discounts

print(neto(gross, sumDiscounts)) # Print the salary Neto, sending the two parameters required by the function

listprovisions = provisions(gross) # Listprovisions is referenced to the list that returns me the functions provisions
for provision in listprovisions: # I walk the return list
  print(provision) # Print the values on the list