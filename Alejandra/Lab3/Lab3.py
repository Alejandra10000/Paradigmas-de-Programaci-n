#-------------------------------------------------------------------------
#                     Condinacionales
#-------------------------------------------------------------------------

precio=50
#------  Si esto (condicion), entonces

if precio<50:
    print("el precio es menor que 50")

#------  Si no, si este otro (condicion), entonces

elif precio>50:
    print("el precio es mayor a 50")
# Si no sucede ningún caso anterior, entonces

else:
    print("el precio es 50")

#----------------------------------------------------------------------
#                 Condicionales anidados
#----------------------------------------------------------------------
cantidad=5
total=precio*cantidad
if total>100:
    if total>500:
        print("total es mayor que 500")
    else:
        if total<500 and total>400:
            print("total es menor que 500 pero mayor a 400")
        elif total<500 and total>300:
            print("total es menor que 500 pero mayor a 300")
        else:
            print("total esta entre 100 y 300")

#---------------------------------------------------------------------
#                    Condicional de igualdad son ==
#---------------------------------------------------------------------

elif total==100:
    print("total es 100")
else:
    print("total es menor que 100")

#--------------------------------------------------------------------
#            Contador mientras la condición sea verdaera
#--------------------------------------------------------------------

num=0
while num>5:
    num=num+1
    print('num = ', num)
    if num==3:
        break
num=0
while num<5:
    num+=1
    if num>3:
        continue   # no continuará si num es menor que 3
    print('num = ', num)

#--------------------------------------------------------------------
#                    Bucle sobre lista
#--------------------------------------------------------------------

nums=[10,20,30,40,50]
for i in nums:
    print(i)

#-------------------------------------------------------------------
#                  Bucle sobre un string
#-------------------------------------------------------------------
for char in 'hello':
    print(char)

#-------------------------------------------------------------------
#                Bucle sobre un diccionario
#                    items = elementos
#-------------------------------------------------------------------
numNames = {1: 'one', 2: 'two', 3: 'three' }
for pair in numNames.items():
    print(pair)
    
#-------------------------------------------------------------------
# Bucle sobre el diccionario, key = llave, value = valor
#-------------------------------------------------------------------

for k,v in numNames.items():
    print("key = ", k , ", value = ", v)
    
# CONTINUACION 3.1

#-------------------------------------------------------------------
# Primera Función
#-------------------------------------------------------------------
def saludo():
    #---------------------------
    #  Documentacion
    #---------------------------
    """Esta funcion saluda"""
    print('¡Quiboles!, ¿como estas?')
    
#----------------------------
#   Llamado de la funcion
#----------------------------
saludo()

#--------------------------------
# Se ejecuta pero no se asigna
#--------------------------------
salida =  saludo()

#-------------------
# Esto no funciona
#-------------------
print(salida)

#--------------------------
# Mostrar Documentacion
#--------------------------
#help(saludo)

#-----------------------
# Funcion con argumento
#-----------------------
def salu2(nombre):
    """ Esta funcion te saluda por tu nombre """
    print("¡Que onda ese", nombre, "!")
salu2("Julian")
salu2("Hannah")

#------------------------------------------------
# Ahorrar trabajo del interprete
# nombre:str  la variable nombre es un str
#------------------------------------------------
def saludos(nombre:str):
    """Esta funcion te saluda por tu nombre estrictamente"""
    print("¡Que onda ese", nombre, "!")
saludos("Alejandro")

a =  123
print(type(a))
saludos(a)

#----------------------------------
#  Funcion con muchos argumentos
#----------------------------------
def saludos_multiples(nombre1, nombre2, nombre3):
    """Esta funcion saluda a 3 personas al mismo tiempo"""
    print("Hola", nombre1, ",", nombre2, "y ", nombre3)
saludos_multiples("Hugo", "Paco", "Luis")

#----------------------------------------------
# Funcion con cualquier numero de argumentos
# ---------------------------------------------
def muchos_saludos(*nombres):
    """Esta funcion saluda a todos los que quieras"""
    i=0
    #--------------------------------
    # end es para ponerlo de corrido
    #--------------------------------
    print("Hola ", end="")
    while len(nombres)>i:
        # Ultimo nombre
        if(i==len(nombres)>i-1):
            print(nombres[i])
        else:
            #cualquier otro nombre
            print(nombres[i], end=",")
            i+=1
            
muchos_saludos("Bosco", "Angel", "David", "Tamra", "Mili", "Edwin", "Lev", "Luis", "Abigail")

def greet(firstname, lastname):
    print('Hello', firstname, lastname)
    
#------------------------------------------------
# Llamar la funcion con argumentos en desorden
#------------------------------------------------
print("\n")
greet(lastname = 'Jobs', firstname = 'Steve') 
#Se puede especficar las variables en desorden
greet( firstname = 'Steve', lastname = 'Jobs')

#--------------------------------------------------------------------
#             Funcion con argumentos escondidos
#--------------------------------------------------------------------
def greet(**person):
    #--------------------------------------------------------
    # La persona tiene caracteristicas firstname y lastname
    #--------------------------------------------------------
    print('Hello', person['firstname'], person['lastname'])
    
greet( firstname = 'Steve', lastname = 'Jobs')
greet(lastname = 'Jobs', firstname = 'Steve', age=55) #se pueden utilizar mas parametros de los necesarios
greet(lastname = 'Bill', firstname = 'Gates') 

#---------------------------------------------------------------------
#             Funcion con valores por defecto
#---------------------------------------------------------------------
def greet (name = 'Guest'):
    print('Hello', name)
    
greet()                    #Utiliza el valor dado de antemano
greet('Steve')

#----------------------------------------------------------------------
#                Funcion con resultado
#----------------------------------------------------------------------
def suma (a,b):
    return a+b
#------------------------------------------------------------
# Programacion Funcional, se pueden funciones en funciones
#------------------------------------------------------------
total = suma(5, suma(10,20))
print(total)

#-----------------------------------------------------------------
#                   Calculo de lambda
#----------------------------------------------------------------
x_al_cuadrado = lambda x: x*x
a1 = x_al_cuadrado(5)
print(a1)

#------------------------------------------------
#       Lambda de varias variables
#------------------------------------------------
suma = lambda x1, x2, x3 : x1+x2+x3
print(suma(99,98,97))

sumas =  lambda *x: x[0]+x[1]+x[2]+x[3]

print(sumas(100,200,300,400))

#------------------------------------------------------------
#      Uso de una funcion anonima
# El argumento va fura entre parentesis
#------------------------------------------------------------
print((lambda x : x*x)(6))  #Funcion Anonima

#------------------------------------------------------------
# Funcion con variable global
# Evite el exceso !!!
#------------------------------------------------------------
name = 'Steve'

def greet():
    global name # Para utilizar una variable Global (que viene fuera del bloque)
    name='Bill'
    print('Hello', name)
    
greet();

#-------------------------------------------------------------
# Algoritmo 1
#-------------------------------------------------------------
#  Serie exponencial
#  Factorizacion de x
#  Negativos con funcion inversa
#-------------------------------------------------------------

n = 200
x = -100.0
flag =  False
if  x<0:
    flag = True
x = -x
s =-1.0
for i in range(n, 0, -1):
    s *= x/float(i)
    s += 1.0
if flag == True:
    s-1/s
print(s)
