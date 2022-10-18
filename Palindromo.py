entrada ="Oso BabOso"
# Quitamos los espacios 
entrada = entrada.replace(" ", "").lower()
resultado = ""

counter = len(entrada)-1
while counter >= 0:
  # print(entrada[counter])
  resultado += entrada[counter]
  # resultado = resultado + entrada[counter]
  counter-=1
  # counter = counter - 1

print("Cadena 1: "+entrada)
print("Cadena 2: "+resultado)

print("¿Es palindromo?: " + str(entrada==resultado))