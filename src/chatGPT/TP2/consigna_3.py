import readline 
import os
from google import genai

#Ubicamos donde se almacena (o almacenara de ser la primera ejecucion) el historial de consultas
HISTORIAL_ARCHIVO = os.path.expanduser("~/.ultima_prompt_TP2_IS2")
readline.clear_history()

#Si existe el archivo, se lee la ultima linea que se encuentra en este
if os.path.exists(HISTORIAL_ARCHIVO):
    with open(HISTORIAL_ARCHIVO, 'r', encoding='utf-8') as arch:
        ultima_linea = arch.readline().strip()
        if ultima_linea:
            readline.add_history(ultima_linea)

#Intentamos pedirle al usuario que ingrese su consulta. De no ser posible, se llama a una excepcion
try:
    print("Por favor ingrese su consulta a chatGPT")
    request_cliente = input()
except:
    print("Error, hubo un error al recibir su consulta")


#De ser posible el ingreso de la consulta, se pasa al procesamiento de esta mediante 2 try anidados, uno para
#verificar el correcto procesamiento de la consulta y otro para verificar la correcta comunicacion de los
#resultados obtenidos
try:
    if (request_cliente):
        client = genai.Client(api_key="INSERTAR KEY")
        request_cliente = str(request_cliente)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=request_cliente
        )
        try:
            print("You: " + request_cliente)
            print("chatGPT: " + str(response.text))
        except:
            print("Hubo un error en la impresion del resultado de su consulta")
    else:
        print("Error, usted no ha ingresado ninguna consulta")
except:
    print("Hubo un error en el procesamiento de su consulta")


#Finalmente, se escribe la consulta del cliente en el historial para que pueda ser accedida en la siguiente ejecucion del programa
with open(HISTORIAL_ARCHIVO, 'w', encoding='utf-8') as arch:
    arch.write(request_cliente + '\n')

