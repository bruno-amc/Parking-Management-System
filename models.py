import sqlite3

# conexão com o banco de dados / connction with data bank
def connect_db():
    connection = sqlite3.connect('parking.db')
    return connection


# criar as tabelas no banco de dados (se elas já não existirem) / create tables (if not exists)
def create_tables():
    db_connection = connect_db()
    cursor = db_connection.cursor()

    #criação da tabela tickets / create table tickets
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Tickets (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   codigo TEXT NOT NULL,
                   placa TEXT,
                   hora_entrada TEXT NOT NULL,
                   hora_saida TEXT,
                   valor_pago REAL
                   )                 
                    ''')
    
    #criação da tabela vagas / table spots
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Vagas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   numero INTEGER NOT NULL,
                   ocupada BOOLEAN NOT NULL DEFAULT 0,
                   prioritaria BOOLEAN NOT NULL DEFAULT 0
                   )    
                    ''')


    #criação da tabela de pagamentos / payments table
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Pagamentos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   ticket_id INTEGER,
                   valor REAL NOT NULL,
                   data_pagamento TEXT NOT NULL,
                   metodo_pagamento TEXT,
                   status TEXT,
                   FOREIGN KEY(ticket_id) REFERENCES Tickets(id)
                   )   
                    ''')
     # Criação da tabela de Administração / adm table
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Administracao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                configuracao TEXT NOT NULL,
                valor TEXT
                )
                ''')

    db_connection.commit()  # Salva as alterações no banco de dados
    db_connection.close()  # Fecha a conexão com o banco de dados


# Executa a criação das tabelas ao iniciar
if __name__ == '__main__':
    create_tables()
    print("Tabelas criadas com sucesso no banco de dados 'parking.db'")