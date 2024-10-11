# -----------------------------------
# declaring local arrayList
# -----------------------------------
vec1 = [5, 1, 7, 4, 9]
vec2 = [6, 8, 2, 5, 4, 3, 1]
# -----------------------------------
# Declaring a joins functions
# -----------------------------------
def Join():
 salida = []
 for act in vec1:
 control = act in vec2
 if control:
 salida.append(act)
 return salida
def FullJoin():
 salida2 = vec1
 for act in vec2:
 control = act in salida2
 if not control:
 salida2.append(act)
 return salida2

#----------------------------------------------------
#Full Outer Join where a.key is null and b.key is null
#-----------------------------------------------------
def FullOuterJoin():
  salida = []
  for act in vec1:       #esto es para los elementos que estan en el vec1 pero no en el vec2
   if act not in vec2:
    salida.append(act)
   return salida

#------------------------------
#Right Join where a.key is null
#------------------------------

def RighJoin():
 salida= []
 for act in vec2:  #Esta funcion es para imprimir los elementos que estan solo en el Vec2 pero no en el Vec1
  if act not in vec1:
   salida.append(act)
  return salida

# -----------------------------------
# Executing joins functions
# -----------------------------------
print(Join())
print('')
print(FullJoin())
print()
print("Funcion para imprimir elementos presentes en el Vec1, pero no presentes en el Vec2", FullOuterJoin())
print()
print ("Funcion para imprimir los elementos presentes unicamente en el Vec2, pero no en el Vec1", RighJoin())