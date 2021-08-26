def delete():

  f = open("prueba.txt","r")
  eliminados = f.readlines()
  eliminado = input("Digite la cedula del beneficiario: ")
  w = open("prueba.txt","w")
  for linea in range(len(eliminados)):
    # print(eliminados[linea])
    # if eliminados[linea].strip() != eliminado:
    if eliminados[linea].strip() = eliminado:
      w.write(eliminados[linea+1])
      # print(eliminados[linea-1])
      # w.write(eliminados[linea])
      # w.write(eliminados[linea+1])


delete()