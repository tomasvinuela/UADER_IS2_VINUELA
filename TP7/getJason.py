'''
copyright UADERFCyT-IS2©2024 todos los derechos reservados
'''
import json
import sys






class Token(object):
    _instance = None
    pepe=0
    def __init__(self):
        try:
            self.token = sys.argv[2]
        except:
            self.token = 'token1'

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Token, cls).__new__(cls)
        return cls._instance
    
    def computar_token(self):
        jsonfile = sys.argv[1]
        if self.token:
            jsonkey = str(self.token)
        else:
            jsonkey = 'token1'
        with open(jsonfile, 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)
        if obj:
            print(str(obj[jsonkey]))
        else:
            print("Error en la clave provista")




def main():
    VERSION_ACTUAL = "1.0.1"
    for i in range(len(sys.argv)):
        if (sys.argv[i]=='-v') :
            print('getJason.py version ' + VERSION_ACTUAL)

    if (VERSION_ACTUAL == '1.0.1'):
        print('Esta utilizando la version nueva')
        token_nuevo = Token()
        token_nuevo.computar_token()
    if (VERSION_ACTUAL == '1.0.0'):
        print('Esta utilizando la version vieja')
        jsonfile = sys.argv[1]
        if sys.argv[2]:
            jsonkey = str(sys.argv[2])
        else:
            jsonkey ='token1'
        with open(jsonfile, 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)
        print(str(obj[jsonkey]))

if __name__ == "__main__":
    main()