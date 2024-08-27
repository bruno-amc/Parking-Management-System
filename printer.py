from escpos.printer import Usb
import time
from PIL import Image

VENDOR_ID = 0x0483
PRODUCT_ID = 0x5720

# Inicializando a impressora USB
try:
    p = Usb(VENDOR_ID, PRODUCT_ID, 0, out_ep=0x03)
except Exception as e:
    print(f"Erro ao conectar à impressora: {e}")
    p = None

def imprimir_ticket(codigo_ticket, caminho_qrcode):
    if p is None:
        print("****impressora não disponível / printer not available ****")
        return
    
    try:
        print(f"Imprimindo o ticket: {codigo_ticket}")
        print(f"caminho do QRCODE: {caminho_qrcode}")

        # Imprimir texto do ticket
        p.text("Estacionamento\n")
        p.text(f"Ticket: {codigo_ticket}\n")
        p.text(f"Data/Hora: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

        # Imprimir QR code
        try:
            img = Image.open(caminho_qrcode)
            p.image(img)
        except Exception as e:
            print(f"Erro ao imprimir o QR code: {e}")
        
        # Finalizar a impressão
        p.text("\nObrigado por usar nosso estacionamento!\n")
        p.text("Volte sempre!\n")
        
        p.cut()  # Realiza o corte do papel (se a impressora suportar)

        print("Ticket impresso com sucesso.")
    
    except Exception as e:
        print(f"Erro ao imprimir o ticket: {e}")


