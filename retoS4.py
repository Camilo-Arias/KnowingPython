# Contenedor de temperáturas
TemMaxList = []
TemMinList = []
# contador de días
dias = 0
diasMinErr = 0
diasMaxErr = 0
diasTwoErr = 0
diasErr = 0
# Medias
MediaTempMax = 0
MediaTempMin = 0
# Promedio días errados
diasErrProm = 0

# Capturando datos para comparación de while
TempMax = int(input('Ingresa la temperatura máxima: '))
TempMin = int(input('Ingresa la temperatura mínima: '))

# while ciclo repetitivo
while TempMax != 0 and TempMin != 0:
  # Almacenando datos en las listas
  TemMaxList.append(TempMax)
  TemMinList.append(TempMin)
  # Contador de número de días
  dias += 1
  # Capturando datos para no quedar en ciclo infinito
  TempMax = int(input('Ingresa la temperatura máxima: '))
  TempMin = int(input('Ingresa la temperatura mínima: '))

# for que iterara las dos listas, ZIP es una función de python que une las dos listas y muestra el resultado como
# tupla en el orden que se requiera
for i in zip(TemMaxList, TemMinList):

  if i[0] > 35 and i[1] >= 5:
    diasMaxErr += 1
  elif i[0] <= 35 and i[1] < 5:
    diasMinErr += 1
  elif i[0] > 35 and i[1] < 5:
    diasTwoErr += 1
  else:
    MediaTempMin = MediaTempMin + i[1]
    MediaTempMax = MediaTempMax + i[0]

# DIAS TOTALES DE ERROR
diasErr = diasMinErr + diasMaxErr + diasTwoErr

# MEDIA TEMPERATURAS
MediaTempMax = MediaTempMax/(dias-diasErr)
MediaTempMin = MediaTempMin/(dias-diasErr)

# PROMEDIO ERROR CON RESPECTO AL TOTAL DE DÍAS
diasErrProm = (diasErr/dias)*100

print(dias)
print(diasErr)
print(diasMinErr)
print(diasMaxErr)
print(diasTwoErr)
print(MediaTempMax)
print(MediaTempMin)
print(diasErrProm)