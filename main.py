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

#clase 6 
#ejercicio 1
a=float(input("Cuanto es el primer valor? "))
b=float(input("cuanto es el segundo valor? "))
def suma(n1,n2):
 sum=(n1+n2)
 print(sum)
suma(a,b)

#ejercicio 2
a=float(input("Cuanto es el primer valor? "))
b=float(input("cuanto es el segundo valor? "))
def resta(n1,n2):
 rest=(n1-n2)
 print(rest)
resta(a,b)

#ejercicio 3
a=float(input("Cuanto es el primer valor? "))
b=float(input("cuanto es el segundo valor? "))
def Multiplicacion(n1,n2):
 multi=(n1*n2)
 print(multi)
Multiplicacion(a,b)

#ejerciciio 4
a=float(input("Cuanto es el primer valor? "))
b=float(input("cuanto es el segundo valor? "))
def Divicion(n1,n2):
  if n1==0 or n2==0:
    print("no podemos proceder con 0 mi rey")
  else:
   divi=(n1/n2)
   print(divi)
Divicion(a,b)

#ejercicio 5
a=float(input("Ingrese numero para operar: "))
b=float(input("Ingrese otro numero para operar: "))
Menu=int(input("Este es su menu de operaciones, 1 para suma, 2 para resta, 3 para multiplicion y 4 para dividir, eliga que quiere rey: "))
def suma(n1,n2):
  sum=(n2+n1)
  print("SU SUMA: ",sum)
def resta(n1,n2):
  rest=(n2-n1)
  print("SU RESTA ES: ",rest)
def multi(n1,n2):
  mul=(n2*n1)
  print("SU MULTIPLICION ES: ", mul)
def divi(n1,n2):
  if n1==0:
    print("No sea webon no se puede dividir por cero -_-")
  else:
    div=(n1/n2)
    print("SU DIVISION ES: ", round(div,2))
if Menu==1:
  suma(a,b)
elif Menu==2:
  resta(a,b)
elif Menu==3:
  multi(a,b)
elif Menu==4:
  divi(a,b)
 
#clase 6 y 7
def intereses(inv):
  d= inv
  if (d >0 and d<1000000):
    return 2
  elif(d>=1000000 and d< 2000000):
    return 5
  else:
     return 7

def calBalance(int, inv):
  n= int
  d= inv
  return round((d*(1+(n/100))),2)
  
def ctaAhorro():
  #inversion, interes, b1,b2,b3 = 0.0
  inversion=float(input("ingrese el valor de la inversion: "))
  interes=intereses(inversion)
  b1=calBalance(interes,inversion)
  b2= calBalance(interes,b1)
  b3= calBalance(interes,b2)
  print("Balance año 1: " + str(b1) + " Balance año 2: " + str(b2) + " Balance año 3: " + str(b3))

ctaAhorro()

#clase 8
#ejercicio 1

def triangulo(b,a):
 return(b*a)/2

def cuadrado(L,l):
  return L*l

def circulo(r):
  return(3.14169*(r**2))

def areafig():
  area=0.0
  figura=""
  figura = input("escriba la figura que le desea sacar el area: ")
  if (figura.lower()=="triangulo"):
    base=0.0
    altura=0.0
    base = float(input("ingrese la base: "))
    altura = float(input("ingresa altura: "))
    area = triangulo(base,altura)
    print("El area del triangulo es: ", area)

  elif (figura.lower()=="cuadrado"):
   lado1=0.0
   lado2=0.0
   lado1 = float(input("ingrese el lado: ")) 
   lado2 = float(input("ingresa el segundo lado: "))
   Area = cuadrado(lado1,lado2)
   print("El area del cuadrado es: ", Area)

  elif (figura.lower()=="circulo"):
    radio=0.0
    radio = float(input("ingrese el radio: "))
    ARea = circulo(radio)
    print("El area del circulo es: ", ARea)
    
areafig()
    
#clase 8
def maximo(a,b):
  if a>b:
    return a
  else:
    return b

def minimo(a,b):
  if a<b:
    return a
  else:
    return b

#programa principal
x=int(input("un numero: "))
y=int(input("otro numero: "))
print(maximo(x-3, minimo(x+2, y-5)))

#clase 9
def descuento(E):
  return(E*10)/100

def descuentoMarca(E):
  return(E*5)/100

def IVA(E):
  return(E*20)/100

def tiendita():
  E=float(input("cuanto cuesta el Estereo Rey: "))
  M=input("su estereo es NOSY rey?: ")
  if M=="si" and E>=2000000:
    print("el estereo le sale en: ", E-descuentoMarca(E)-descuento(E)+IVA(E))
  elif M=="no" and E>=2000000:
    print("el estereo le sale en: ", E-descuento(E)+IVA(E))
  elif M=="si" and E<2000000:
    print("el estereo le sale en: ", E-descuentoMarca(E)+IVA(E))
  elif M=="no" and E<2000000:
    print("el estereo le sale en: ", E+IVA(E))

tiendita()

#Parcial
def interes2(a):
 return(a*0.02)
  
def interes5(a):
  return(a*0.05)
  
def interes7(a):
  return(a*0.07)
  
def Banco():
 año1=float(input("que valor va depositar este primer año?:"))
 if 0> año1 <1000000:
  año1F=(año1+interes2(año1))
  print("Esto le quedo este año", año1F)
 elif 1000000>año1<2000000:
  año1F=año1+interes5(año1)
  print("Esto le quedo este año", año1F)
 elif 2000000>año1:
   año1F=año1+interes7(año1)
   print("Esto le quedo este año", año1F)  

 año2=float(input("que valor va depositar este segundo año?:"))
 if 0>año2<1000000:
  año2F=año2+interes2(año2)
  print("Esto le quedo este año", año2F)
 elif 1000000>año2<2000000:
  año2F=(año2+interes5(año2))
  print("Esto le quedo este año", año2F)
 elif 2000000>año2:
  año2F=año2+interes7(año2)
  print("Esto le quedo este año", año2F)

 año3=float(input("que valor va depositar este tercer año?:"))  
 if 0>año3<1000000:
   año3F=(año3+interes2(año3))
   print("Esto le quedo este año", año3F)
 elif 1000000>año3<2000000:
   año3F=año3+interes5(año3)
   print("Esto le quedo este año", año3F)
 elif 2000000>año3:
   año3F=año3+interes7(año3)
   print("Esto le quedo este año", año3F)
 Balance=(año1F+año2F+año3F)
 print("este es su balance final",Balance)
Banco()

def porcentaje(w,y):

    return (w*(0+(y/100)))

 

w=int(input("Ingrese valor: "))

z=int(input("Ingrese porcentaje: "))
y=(z+886)

print(round(porcentaje(w,y),2))

#clase 11
A=0
while A < 10:
  print(A)
  A=A+1

def suma():
  return opcion1+opcion2
def resta():
  return opcion1-opcion2
def division():
  return opcion1/opcion2
def multiplicacion():
  return opcion1*opcion2

c=0
while c!=5:
  
  opcion1=int(input("ponga un numero: "))
  
  opcion2=int(input("ponga otro numero: "))

  c=int(input("elija una opcion \n 1. sumar:\n 2. resta:, \n 3. division: \n 4 multiplicacion: \n 5. terminar operaciones:"))
  """if (c<6):"""
    
  if (c==1):
    print("la suma es:",suma())
  elif (c==2):
    print("la resta es:",resta())
  elif (c==3):
    print("la division es:",division())
  elif (c==4):
     print("la multiplicacion es:",multiplicacion())
  elif (c==5):
    print("Adios")
  else:
    print("error")
    
#Clase 12
for c in range(1 ,12 ,2 ):
  print( c )

#ejercicio 1
import random
def adivina_el_numero():
  numero_secreto = random.randint(1,100)
  adivinado = False

  while not adivinado:
      intento = int(input("adivina el numero"))
      if intento == numero_secreto:
          print("Es correcto este es el numero")
          adivinado = True
      elif intento < numero_secreto:
        print("el numero es mayor")
      else:
        print("el numero es menor")
adivina_el_numero()

#Ejercicio 2
def tablas_de_multiplicar():
  print("Hola")
  tabla = int(input("De que numero quieres ver la tabla: "))

  for multi in range(1,11):
    resultado = (tabla * multi)
    print(tabla, "x", multi, "=" ,resultado)
tablas_de_multiplicar()

def Factoriali():
  print("Hola")
  numero = int(input("cual numero vamos a factorizar: "))
  factorial = 1
  
  for i in range(1, numero + 1):
    factorial = factorial * i
    
  print("esto da su factorial: ", factorial)
Factoriali()
'''
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

def verificar_ganador(tablero, jugador):
    for fila in tablero:
        if all([c == jugador for c in fila]):
            return True

    for columna in range(3):
        if all([tablero[fila][columna] == jugador for fila in range(3)]):
            return True

    if all([tablero[i][i] == jugador for i in range(3)]) or all([tablero[i][2 - i] == jugador for i in range(3)]):
        return True

    return False

def juego_triqui():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"
    movimientos_restantes = 9
    ganador = None

    print("¡Bienvenido al juego de Triqui!")
    imprimir_tablero(tablero)

    while movimientos_restantes > 0 and not ganador:
        fila = int(input(f"Jugador {jugador_actual}, elige una fila (0, 1 o 2): "))
        columna = int(input(f"Jugador {jugador_actual}, elige una columna (0, 1 o 2): "))

        if fila < 0 or fila > 2 or columna < 0 or columna > 2 or tablero[fila][columna] != " ":
            print("Movimiento inválido. Inténtalo de nuevo.")
            continue

        tablero[fila][columna] = jugador_actual
        imprimir_tablero(tablero)

        if verificar_ganador(tablero, jugador_actual):
            ganador = jugador_actual
        else:
            jugador_actual = "O" if jugador_actual == "X" else "X"
            movimientos_restantes -= 1

    if ganador:
        print(f"¡El jugador {ganador} ha ganado!")
    else:
        print("¡Es un empate!")

if __name__ == "__main__":
    juego_triqui()
