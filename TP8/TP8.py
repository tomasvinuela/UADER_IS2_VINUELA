'''
copyright UADERFCyT-IS2©2024 todos los derechos reservados
'''
import json
import sys


class AbstractHandler(object):
    def __init__(self, nxt):
        self._nxt = nxt

    def handle(self, request):
        handled = self.processRequest(request)
        if not handled:
            self._nxt.handle(request)

    def processRequest(self, request):
        raise NotImplementedError('First implement it !')


class CuentaToken1(AbstractHandler):
    def __init__(self, nxt):
        super().__init__(nxt)
        self.saldo = 1000
        self.pagos_efectuados = []
        self.contador_pagos = 0

    def processRequest(self, request):

        if request <= 'token1':
            self.saldo = (self.saldo - 500)
            self.contador_pagos += 1
            return True
    
    def mostrar_listado(self):
        return self.pagos_efectuados

class CuentaToken2(AbstractHandler):
    def __init__(self, nxt):
        super().__init__(nxt)
        self.saldo = 2000
        self.pagos_efectuados = []
        self.contador_pagos = 0

    def processRequest(self, request):

        if 'token1' < request <= 'token2':
            self.saldo = (self.saldo - 500)
            self.contador_pagos += 1
            self.pagos_efectuados.append([str(self.contador_pagos), str(request), '$500'])
            return True
    
    def mostrar_listado(self):
            return self.pagos_efectuados


class DefaultHandler(AbstractHandler):

    def processRequest(self, request):

        print("No existe una cuenta con ese token")
        return True


class ControladorCuentas:
    def __init__(self):

        initial = None

        self.handler = CuentaToken1(CuentaToken2(DefaultHandler(initial)))

    def pagos(self, user_request):

        for request in user_request:
            self.handler.handle(request)
    
    def listar_pagos(self):
        listado_total = self.handler.mostrar_listado
        return listado_total


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
            a_print = str(obj[jsonkey])
            print(a_print)
            return jsonkey
        else:
            print("Error en la clave provista")




def main():
    VERSION_ACTUAL = "1.0.2"
    for i in range(len(sys.argv)):
        if (sys.argv[i]=='-v') :
            print('getJason.py version ' + VERSION_ACTUAL)

    if (VERSION_ACTUAL == '1.0.2'):
        print('Esta utilizando la version: ' + str(VERSION_ACTUAL))
        controlador = ControladorCuentas()
        token_nuevo = Token()
        token = token_nuevo.computar_token()
        controlador.pagos(token)
        controlador.listar_pagos

    if (VERSION_ACTUAL == '1.0.1'):
        print('Esta utilizando la version: ' + str(VERSION_ACTUAL))
        token_nuevo = Token()
        token_nuevo.computar_token()

    if (VERSION_ACTUAL == '1.0.0'):
        print('Esta utilizando la version: ' + str(VERSION_ACTUAL))
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