#---------------------------------------------------------------------------
#                          CONJUNTO EN PYTHON
#---------------------------------------------------------------------------

even_nums = {2,4,6,8,10} # conjunto de numeros pares
print(even_nums)

# el booleano no es parte del conjunto

emp = {1, 'Steve', 10.5, True} #conjunto de diferentes objetos
print(emp)

nums = {1,2,2,3,4,4,5,5}
print(nums)

#---------------------------------------------------------------------------
#  Covertir secuencia a conjunto, no lo genera el orden
#---------------------------------------------------------------------------
 
s =  set('hello')
print(s)
s =set((1,2,3,4,5))   #tupla al conjunto
print(s)

#---------------------------------------------------------------------------
#              De diccionario a conjunto: conjunto de llaves
#---------------------------------------------------------------------------

d = {1: 'one', 2: 'two'}
s = set(d)
print(s)

s.add(100)
print(s)

s.update(nums)
print(s)

s.remove(100)
print(s)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

su= s1|s2 # Unión
print(su)

si = s1&s2 #Insertesección
print(si)

sr = s1-s2 #Diferencia de conjuntos
print(sr)

sp = s2-s1 #lo mismo que el anterior
print(sp)

ss = s1^s2 #Diferencia Simetrica
print(ss)

#-----------------------------------------------------------------------------
#                         Uso de diccionarios
#-----------------------------------------------------------------------------

capitals = {"USA":"Washingthon D.C", "France":"Paris", "India":"New Delthi"} 
print(capitals)

#-----------------------------------------------------------------------------
#                             llave:valor
#-----------------------------------------------------------------------------

d = {}  # Diccionario vacio

numNames = {1:"One", 2:"Two", 3:"Three"} # Llave entera valor string

decNames = {1.5: "One and Half", 2.5:"Two and Half", 3.5:"Three and half"} #llave real, valor string

items = {("Paker", "Reynolds", "Camlin"):"pen", ("LG", "Whirlpool", "Samsung"):"Refrigerator"}  #Llave tupla, valor string  

romanNums = { 'I':1, 'II':2, 'III':3, 'IV':4, 'V':5} #Llave string, valor int
print(romanNums)
print(romanNums['I'])

print(capitals.get("India"))
print(capitals.get("india"))

for k in capitals:
    print("Key = "+k+"Value = "+ capitals[k])

# Nuevo dato para el diccionario
capitals["Mexico"] =  "CDMX"
print(capitals)

# Borra dato del diccionario
del capitals["Mexico"]
print(capitals)

# Borra todo el diccionario
del capitals

# Reportar llaves
print(romanNums.keys())

# Reportar valores
print(romanNums.values())
# Jucio de llave (está o no la llave en el diccionario
print("I" in romanNums)
print("X" in romanNums)
print("XX" not in romanNums)







