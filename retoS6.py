def addPerson():
  print('Digite la información del beneficiario a agregar:')
  with open('agenda.txt', 'a') as data:
    data.write(input().title()+'\n')
    data.write(input()+'\n')
    data.write(input()+'\n')
    print('El beneficiario ha sido agregado')

def listComplete():
  print('Listado de beneficiarios')
  with open('agenda.txt', 'r') as data:
    for line in data.readlines():
      print(line.strip())

def listFilter():
  letter = input('Digite la letra por la que empiezan los beneficiarios: ').upper()
  print('Listado filtrado de beneficiarios: ')
  with open('agenda.txt', 'r') as data:
    content = data.readlines()
    for line in content:
      if line.strip()[0] == letter:
        indexl = content.index(line)
        for i in range(3):
          print(content[indexl+i].strip())

def search():
  person = input('Digite el nombre y apellido del beneficiario a buscar: ').title()
  with open('agenda.txt', 'r') as data:
    content = data.readlines()
    for line in content:
      if line.strip() == person:
        indexP = content.index()
        for i in range(3):
          print(content[indexP+i].strip())

def delete():
  identify = input('Digite la cedula del beneficiario a borrar: ')
  with open('agenda.txt', 'r') as data:
    content = data.readlines()
    for line in content:
      if line.strip() == identify:
        indexI = content.index(line)

    data = open('agenda.txt', 'w')
    for line in content:
      if line.strip() != content[indexI].strip() and line != content[indexI-1] and line != content[indexI+1]:
        data.write(line)
  print('El usuario ha sido eliminado del listado')

while True:
  print('''Menu Principal
1. Ver listado
2. Ver listado filtrado
3. Agregar beneficiario
4. Buscar beneficiario
5. Borrar beneficiario
6. Salir''')
  switch = int(input())
  if switch == 1:
    listComplete()
  elif switch == 2:
    listFilter()
  elif switch == 3:
    addPerson()
  elif switch == 4:
    search()
  elif switch == 5:
    delete()
  else:
    print('Hasta pronto')
    break
