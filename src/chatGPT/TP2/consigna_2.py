from google import genai

try:
    print("Por favor ingrese su consulta a chatGPT")
    request_cliente = input()
except:
    print("Error, hubo un error al recibir su consulta")

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