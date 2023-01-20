''' supercomenatrio de
                               Inicio de resumen '''

#-----------------------------------------------------------------------------
#                           Operaciones basicas 
#-----------------------------------------------------------------------------

print(2+3)
print(2*3)
print(6/3)
print(3**4)
print(4**2)   #raiz cuadrada
print(10%2)
print(10%0.1) #exclusivo de python

#-----------------------------------------------------------------------------                Para                  Saber el tipo de objeto se usa type
#-----------------------------------------------------------------------------

t=0
print(type(t)) #entero
t=3.6
print(type(t)) #flotante real
t=True;
print(type(t)) #Boleano (bool)

#-----------------------------------------------------------------------------
#                           Mensajes a pantalla
#-----------------------------------------------------------------------------

print("este es un comando de python", "este es otro enunciado", t)
print('id : ', 1)
print('First Name: ', 'Alejandra')
print('Last Name: ', 'Sanchez')
print("vamos a sumar esto" + "con esto otro")

#-----------------------------------------------------------------------------
#                 Continuar una instrucción en varios renglones 
#-----------------------------------------------------------------------------

if 100>99 and \
   200 <=300 and \
   True !=False:
       print('Hola Mundo')

#----------------------------------------------------------------------------
# Comando diferentes en la misma linea
#----------------------------------------------------------------------------

print("hola"); print("tu!")   #Se considera mala practica

#----------------------------------------------------------------------------
# Usando paréntesis redondos, cuadrados o llaves, se puede escribir
#                          en varios renglones
#----------------------------------------------------------------------------

list = [1, 2, 3, 4,
        5, 6, 7, 8, 
        9, 10, 11, 12]

matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]

print(list)
print(matriz)

#----------------------------------------------------------------------------
#    Indentación estricta para procesos dependientes de: (dos puntos)
#----------------------------------------------------------------------------

if 10>5:
  print("diez mayor que cinco")
  print("otra indentación")
for i in list:
  print(i)
  print("ok")
if 10>5:
    print("verdadero")
    if 10<20:
       print("verdadero")
elif 5>3:                    #comienza segundo condicional
    print("esto no se imprimira")
else:
    print("aqui nunca llega")
#---------------------------------------------------------------------------
#                               Funciones
#---------------------------------------------------------------------------

def say_hello(name):
    print("hello", name)
    print("Bienvenido a tutoriales de python")

say_hello ("Hannah")

