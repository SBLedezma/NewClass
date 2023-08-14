#que se
#ejercicio 1:
'''
print(Hola Mundo)

#Ejercicio 2:

NewWorld="¡Hola Mundo!"
print(NewWorld)

#ejercicio 3:

Name=input("¿perro como se llama?: ")
print("ah mi soci@ se llama "+Name)

#ejercicio 4:
print(((3+2)/(2*5))**2)

#ejercicio 5
horas=float(input("cuantas horas haces: "))
costo=float(input("cuanto ganas por hora: "))
resultado=horas*costo
print("ganas " ,resultado)
#tambien se puede usar str

#ejercicio 6
Numero=int(input("Introduce un numero entero positivo: "))
print("el resultado es: ",Numero*(Numero+1)/(2))

#ejercicio 7
peso=float(input("cuanto kg pesas? "))
altura=float(input("cuantos metros mides? "))
indice=round(peso/altura**2,2)
print("tu indice de masa corporal es:",indice)

#ejercicio 8
N=int(input("introduce un numero: "))
M=int(input("introduce otro numero: "))
D=round(N/M,2)
C=N//M
R=N%M
print("la divicion da ",D," el cociente da",C," y el residuo da ",R,)
print("""\
⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉""")

#ejercicio 9
I=int(input("Cuanto vamos a invertir "))
i=int(input("cuanto interes anual mano "))
A=int(input("y cuantos años mi rey "))
Formula=round(I*(i/100+1)**A)
print("esto hicimos mi rey",Formula)

#ejercicio 10
P=int(input("cuantos payasos va a llevar mi rey "))
M=int(input("y cuantas Muñecas va a llevar mi rey "))
R=(P*112)+(M*75)
print("el paquete pesa ",R)

#ejercicio 11
#ejercicio 12

#Clase 5

#ejercicio 1
N=int(input("cuantas puñaladas le pegaron "))
R=N*(N+1)/2
if R>20:
  print(R,"usted esta mueto mi hermano")
else:
  print(R,"al menos esta vivo")
  
#ejercicio 2
N=int(input("dame un numero entero sapa "))
M=int(input("Dame otro numero sapa "))
C=N//M
D=N/M
R=N%M
print("el resultado de la divicion es ",D," El cociente es ",C," y el resto es ",R)
if C<1:
  print("El divisor es mayor al dividiendo")
  
#ejercicio 3
P=float(input("cuanto vamos a invertir manito "))
i=float(input("cuanto es el interes manito "))
A=int(input("Por cuantos añitos manito "))
C=round(P*((i/100)+1)**A)
if C<100000:
  print(C," es baja rentabilidad manito")
elif C>100000 and C<1000000:
  print(C," Es una rentabilidad moderada manito")
elif C>1000000:
  print(C," Es buena invercion manito")
'''
#Ejercicio 4
P=int(input("cuantos payasos va a llevar mi rey "))
M=int(input("y cuantas Muñecas va a llevar mi rey "))
R=(P*112)+(M*75)
if R>3000:
  X=input("lo vamos a enviar o no lo vamos a enviar ?")
  if X =="si":
   print("Ya lo mandamos mi Rey")
  elif X =="no":
   print("Cancelamos mision mi Rey")

    