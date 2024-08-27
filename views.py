import tkinter as tk
from tkinter import messagebox
from models import connect_db
import datetime
import uuid
from qrcode_generator import gerar_qrcode
from printer import imprimir_ticket

# Função para emitir um ticket e gerar QR code
def emitir_ticket():
    db_connection = connect_db()
    cursor = db_connection.cursor()

    # Gera um UUID como código de ticket
    codigo_ticket = str(uuid.uuid4())
    hora_entrada = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Inserir o ticket no banco de dados
    cursor.execute('''
        INSERT INTO Tickets (codigo, hora_entrada) 
        VALUES (?, ?)
    ''', (codigo_ticket, hora_entrada))

    db_connection.commit()
    db_connection.close()

    # Gera o QR code do ticket
    caminho_qrcode = r"C:\Users\bruam\Documents\parking_management_system_python\Parking-Management-System\qr_codes_directory\{}.png".format(codigo_ticket)
    
    # Gera o QR Code
    gerar_qrcode(codigo_ticket, caminho_qrcode)

    # Imprime o ticket com o QR code
    imprimir_ticket(codigo_ticket, caminho_qrcode)

    # Mensagem de sucesso
    messagebox.showinfo("Sucesso", f"Ticket {codigo_ticket} emitido e impresso com sucesso!")

# Configuração básica do Tkinter
def main():
    root = tk.Tk()
    root.title("Gestão de Estacionamento - Emissão de Tickets")
    root.geometry("400x200")

    lbl_instrucao = tk.Label(root, text="Clique no botão para emitir um ticket")
    lbl_instrucao.pack(pady=20)

    btn_emitir = tk.Button(root, text="Emitir Ticket", command=emitir_ticket)
    btn_emitir.pack(pady=20)

    root.mainloop()

if __name__ == '__main__':
    main()
