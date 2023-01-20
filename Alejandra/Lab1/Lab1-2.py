#==================================================================================
#                          Segundo Código
#==================================================================================

#----------------------------------------------------------------------
#       Input permite obtener datos del usuario en prompter
#----------------------------------------------------------------------

nombre = input ("Dame tu nombre :")
print("Hola como estas", nombre)

#----------------------------------------------------------------------
#             Los enteros son de presición ilimitada
#----------------------------------------------------------------------

y = 5000000000000
print(y)

#----------------------------------------------------------------------
#     Se pueden delimitar números con guón bajo pero no con coma
#----------------------------------------------------------------------

y = 5_000_000
print(y)

#----------------------------------------------------------------------     
#       La función int() cambia strings y floats a enteros
#----------------------------------------------------------------------

numero = int(input("Dame tu edad: "))
type(numero)

#----------------------------------------------------------------------
#     La notación cientifica de flotantes utiliza a enteros
#----------------------------------------------------------------------

# 1.2 x 10 ^ {-9}
 
y = 1.2E-09
print(y)

#----------------------------------------------------------------------
#       La función float() convierte strings y enteros a floats
#----------------------------------------------------------------------

y = float ("14.3")

#---------------------------------------------------------------------
# LOs complejos se escriben con la raíz de menos de uno j siempre con 
# j siempre con un número como prefijo no acepta la j suelta
#---------------------------------------------------------------------

z = 1+1j

# suma                                  ->       + 
# resta                                 ->       -
# multiplicación                        ->       *
# división                              ->       /
# modulo                                ->       %
# Exponente                             ->       **
# Función piso                          ->       //
# Funciones para transformar números    ->       int() float() complex()
#  Operaciones                          ->       abs() round() pow()

print(round (3.1459,4))


#---------------------------------------------------------------------------------
#                        String de varias lineas 
#---------------------------------------------------------------------------------

parrafo = """ En el bosque de la china
 la china se pedrió """

print(parrafo)

#--------------------------------------------------------------------------------
#             La función len() obtiene el tamaño del string
#--------------------------------------------------------------------------------

n = len(parrafo)
print(n)

#--------------------------------------------------------------------------------
# Las letras en un string ocupan lugares como en un arreglo (también de atrás 
# para adelante comenzando en -1 el último)
#--------------------------------------------------------------------------------

palabra = "hola"
print(palabra[0])
print(palabra[-4])


