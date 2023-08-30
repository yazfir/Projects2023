

import json

autos = {
    'Ford': 'Fiesta',
    'Nissan':'Tsuru',
    'Toyota':'Avanza'
}

print(autos)

a = json.dumps(autos) #Convierte el diccionario en arreglo

print(a)
print(type(a))

b = json.loads(a) #Convierte el arreglo a diccionario

print(b)
print(type(b))
print(b.keys())
print(b.values())

c = json.loads('{"Ford": "Figo", "Nissan": "Versa", "Toyota": "Sienna"}') #Convierte la cadena a diccionario

print(c)
print(type(c))
print(c.keys())
print(c.values())