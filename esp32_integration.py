import requests

# Configuração do IP do ESP32
ESP32_IP = "http://192.168.0.100"  # Altere para o IP real do ESP32 na sua rede

def open_gate():
    try:
        # Envia um comando HTTP GET para o ESP32 abrir a cancela
        response = requests.get(f"{ESP32_IP}/open")
        if response.status_code == 200:
            print("Comando de abertura da cancela enviado com sucesso!")
        else:
            print(f"Erro ao enviar comando: {response.status_code}")
    except Exception as e:
        print(f"Erro na comunicação com o ESP32: {e}")

# Outros métodos de integração com o ESP32 podem ser adicionados aqui
