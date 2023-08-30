"""
Colecciones.

"""

def ejercicios9a10_1():
    
    a=[4,6,7,9,2]

    a.append(8)
    "a.clear() '''Borra todos los elementos'''  "
    a.remove(2)

    for x in a:
        print(x)

    print("el numero de elementos es:", len(a))


def ejercicios9a10_2():
    #Listas o Arreglo
    frutas = ['manzana','durazno','pera','mango']

    for fruta in frutas:
        print(fruta)

    frutas.sort() #  Te ordena el arreglo 

    for fruta in frutas:
        print(fruta)


def ejercicios10a11_1():
    #Dada una lista de horas trabajadas y honorarios por hora. Calcular el total de honorarios de un trabajador
    HorasTrabajadas = [5,8,7,6,9]
    CostoxHr = 100

    for hr in HorasTrabajadas:
        print('HorasTrabajas:', hr, 'Costo:', hr * CostoxHr)


def ejercicios10a11_2():
    #Dada una lista de horas trabajadas y honorarios por hora. Calcular el total de honorarios de un trabajador
    Empleados = ['Pedro', 'Pablo','Maria','Ana']
    HorasTrabajadas = [5,8,7,6,9] , [8,8,8,8,8] , [6,7,7,8,6] , [9,6,7,6,7]
    CostoxHr = 100

    # print(HorasTrabajadas[0])
    i=0

    for Empleado in Empleados:
        
        hrsTrabTemp=HorasTrabajadas[i]
        i=+1
        for hr in hrsTrabTemp:
            print('Empleado:', Empleado,'HorasTrabajas:', hr, 'Costo:', hr * CostoxHr)
            

def ejercicios10a11_3():
    dict={
        'nombre':'Juanito',
        'edad':29,
        'estatura':1.74
    }

    print(dict)

    frutas = {
        'platano': 3,
        'naranjas': 4,
        'mandarina':8
    }

    print(frutas)

    print(dict['nombre'])
    print(frutas['naranjas'])

    for x in dir(frutas):
        print(x)
    
    print(frutas.keys())
    print(frutas.values())


def ejercicios10a11_4():
    #Tuplas
    tuplaFrutas = ('naranja','mandarina','limon','toronja')

    print(tuplaFrutas)

    for x in tuplaFrutas:
        print(x)

def ejercicio11a12_1():
    #Conjuntos
    frutaSet={'Manzana','Pera','Naranja','Mango'}
    otras={'Mango','Durazno','Pera'}

    print(frutaSet)

    for x in frutaSet:
        print(x)

    for x in dir(frutaSet):
        print(x)

    todas = frutaSet.union(otras)

    print(todas)
    print(frutaSet.intersection(otras)) #Las coincidencias entre conjuntos


ejercicio11a12_1()