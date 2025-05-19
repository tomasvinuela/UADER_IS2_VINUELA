'''
El programa primero obtiene la ubicacion del json mediante la variable jsonfile
Luego, se chequea si se paso otra clave especifica que se debera buscar en el archivo. De ser asi, se procedera
con jsonkey valiendo este parametro. Si no se le pasa algun valor en especifico, jsonkey sera token1
'''
import json
import sys
jsonfile = sys.argv[1]
if sys.argv[2]:
    jsonkey = str(sys.argv[2])
else:
    jsonkey: "token1"
with open(jsonfile, 'r') as myfile:
    data = myfile.read()
obj = json.loads(data)
print(str(obj[jsonkey]))