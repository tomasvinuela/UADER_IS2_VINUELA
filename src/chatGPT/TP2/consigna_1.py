from google import genai


print("Por favor ingrese su consulta a chatGPT")
request_cliente = input()

if (request_cliente):
    client = genai.Client(api_key="INSERTAR KEY")
    request_cliente = str(request_cliente)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=request_cliente
    )
    print("You: " + request_cliente)
    print("chatGPT: " + str(response.text))
else:
    print("Error, usted no ha ingresado ninguna consulta")