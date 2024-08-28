import tkinter as tk
from tkinter import messagebox
from models import connect_db

def carregar_configuracoes():
    db_connection = connect_db()
    cursor = db_connection.cursor()

    cursor.execute("SELECT valor FROM Configuracoes where chave = 'total_vagas' ")
    resultado = cursor.fetchone() #fetchone() retorna a próxima linha do resultado da consulta como uma tupla 
    db_connection.close()

    if resultado:
        return int(resultado[0]) #posição zero da tupla, ou seja, o total de vagas
    else:
        return None
    

def salvar_configuracoes(total_vagas):
    db_connection = connect_db()
    cursor = db_connection.cursor()

    cursor.execute("UPDATE Configuracoes SET valor = ? WHERE chave = 'total_vagas'",(total_vagas,))
    db_connection.commit()
    db_connection.close()

    messagebox.showinfo("Sucesso","Configurações salvas com sucesso!")


def atualizar_configuracoes():
    total_vagas = entry_total_vagas.get()

    if not total_vagas.isdigit():
        messagebox.showinfo("Erro","Por favor insira um número válido.")
        return
    
    salvar_configuracoes(total_vagas)


# função principal para exibir a interface de configurações

def main():
    global entry_total_vagas
    root = tk.Tk()
    root.title("Configurações do estacionamento")
    root.geometry("300x150")

    #label e entry para o total de vagas
    lbl_total_vagas = tk.Label(root, text="Total de vagas: ")
    lbl_total_vagas.pack(pady=10)

    total_vagas_atual = carregar_configuracoes()

    entry_total_vagas =tk.Entry(root, width=10)
    entry_total_vagas.pack(pady=10)
    entry_total_vagas.insert(0, total_vagas_atual if total_vagas_atual else '') #Esta linha insere um valor (ou vazio: '', se não tiver valor) no campo de entrada entry_total_vagas na posição 0 (início do campo).

    #botão para salvar as configurações
    btn_salvar = tk.Button(root, text="Salvar configurações", command=atualizar_configuracoes)
    btn_salvar.pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    main()



