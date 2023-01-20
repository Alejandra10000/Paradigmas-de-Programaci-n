#------------------------------------------------------------------
#                   PROGRAMACION ORIENTADA A OBJETOS
#------------------------------------------------------------------

#------------------------------------------------------------------
# Una clase para todo objeto vacío no esta tan vacio, necesita la
# palabra pass = pasar
#------------------------------------------------------------------

class ObjetoVacio:
    pass

#------------------------------------------------------------------
# Nada es un ObjetoVacio
#------------------------------------------------------------------

nada=ObjetoVacio()
print(type(nada))

#------------------------------------------------------------------
# La clase llanta
#------------------------------------------------------------------

class Llanta:
    #--------------------------------------------
    # Variable cuenta es de toda la clase
    #--------------------------------------------
    cuenta=0
    #--------------------------------------------
    # Funcion constructora de indentidad _init_
    # es una funcion reservada comienza con uno
    # mismo: self pero puede ser otro nombre (mi)
    # parametros de entrada = default
    #--------------------------------------------

    def __init__(mi, radio=50, ancho=30, presion=1.5):
        #variable de la estructura completa llanta
        Llanta.cuenta +=1
        #variables exclusivas de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presion = presion

#------------------------
#  Objetos Instanciados
#------------------------
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presion = 1.2)
llanta3 = Llanta()
llanta4 = Llanta(40,30,1.6)

#-----------------------------------
# Objeto que contiene otros Objetos
#-----------------------------------

class Coche:
    def __init__ (mi, ll1, ll2, ll3, ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2 
        mi.llanta3 = ll3
        mi.llanta4 = ll4
        
micoche = Coche(llanta1, llanta2, llanta3, llanta4)

print("Total de llantas = ", Llanta.cuenta) #variable global de la clase
print("Presion de la llanta 4 = ", llanta4.presion)
print("Radio de la llanta 4 = ", llanta4.radio)
print("Radio de la llanta 3 = ", llanta3.radio)
print("Presion de la llanta 1 de mi coche = ", micoche.llanta1.presion)

#------------------
# Encapsulamiento
#------------------

#---------------------------------------------------------------------
# Uso de la funcion de python property para poner y obtener atributos
#---------------------------------------------------------------------
class Estudiante:
    def __init__(mi):
        mi.__nombre = ''
    def ponerme_nombre(mi,nombre):
        print('se llamo a ponerme_nombre')
        mi.__nombre =  nombre
    def obtener_nombre(mi):
        print('se llamoa obtener_nombre')
        return mi.__nombre
        nombre= property(obtener_nombre, ponerme_nombre)
        
#-------------------------------------
# Crear Objeto estudiante sin nombre
#-------------------------------------

estudiante = Estudiante()

#----------------------------------------------------------------------------
# Ponerle nombre usando la propiedad de nombre y el metodo de porneme nombre
# sin tener que llamar explicitamente a la funcion
#----------------------------------------------------------------------------

estudiante.nombre = "Diego"

#--------------------------------------------------------------------------------------
# Obtener el nombre con el metodo obtener_nombre, __nombre es una variable encapsulada
# (no visible desde afuera), (sin tener qque llamar a la funcion a la funcion
# obtener_nombre)
#--------------------------------------------------------------------------------------

print(estudiante.nombre)

# Esto no funciona
# print(estudiante.__nombre)

#---------------------
# Herencia de clases
#---------------------

class Cuadrilatero:
    def __init__ (mi,a,b,c,d):
        mi.lado1 = a
        mi.lado2 = b
        mi.lado3 = c 
        mi.lado4 = d
        
    def perimetro(mi):
        p = mi.lado1 + mi.lado2 + mi.lado3 + mi.lado4 
        print("perimetro = ", p)
        return p
        
#--------------------------------------------------------
# Su hijo rectangulo, rectangulo es hijo de Cuadrilatero
# rectangulo(cuadrilatero)
#--------------------------------------------------------

class Rectangulo(Cuadrilatero):
    def __init__(self,a,b):
        #-------------------------
        # Constructor de su madre
        #-------------------------
        super().__init__(a,b,a,b)

#-------------------
# Su nieto cuadrado
#-------------------
class Cuadrado(Rectangulo):
    def __init__ (self, a):
        super().__init__(a,a)
        
    def area(self):
        area =  self.lado1**2
        return area
        
    #def perimetro(self)
    #p = 4.0 * self.lado1
    #print("perimetro = ", p)
    # return p
    
#-------------------
# Crear un Cuadrado
#-------------------
cuadrado1 = Cuadrado(5)

#------------------------------------------------------
# Llamar al metodo perimetro de sua buelo Cuadrilatero
#------------------------------------------------------
perimetro1 = cuadrado1.perimetro()

#---------------------------------
# Llamar a su propio metodo area
#---------------------------------
area1 = cuadrado1.area()

print("Area = ", area1)
print("Perimetro= ", perimetro1)

#--------------------------------------------------------------
# Sobrescribir un metodo de su madre o abuela o tatarabuela....
# Es vover a definir una funcion ya existente
#--------------------------------------------------------------
    










