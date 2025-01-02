import mysql.connector

class Nuotatore:
    def __init__(self, id, nome, eta):
        self.id = id
        self.nome = nome
        self.eta = eta

class Allenamento:
    def __init__(self, id, nuotatore_id, data_allenamento, durata):
        self.id = id
        self.nuotatore_id = nuotatore_id
        self.data_allenamento = data_allenamento
        self.durata = durata

# Connessione al database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="progetto_nuoto"
)
cursor = mydb.cursor()


nuotatori = []
allenamenti = []

# Funzioni

def aggiungi_nuotatore():
    id = input("Inserisci l'ID del nuotatore: ")
    nome = input("Inserisci il nome del nuotatore: ")
    eta = input("Inserisci l'età del nuotatore: ")
    cursor.execute("INSERT INTO nuotatori (id, nome, eta) VALUES (%s, %s, %s)", (id, nome, eta))
    mydb.commit()
    print("Nuotatore aggiunto.")

def modifica_nuotatore():
    id = input("Inserisci l'ID del nuotatore da modificare: ")
    nome = input("Inserisci il nuovo nome del nuotatore: ")
    eta = input("Inserisci la nuova età del nuotatore: ")
    cursor.execute("UPDATE nuotatori SET nome = %s, eta = %s WHERE id = %s", (nome, eta, id))
    mydb.commit()
    print("Nuotatore modificato.")


def elimina_nuotatore():
    id = input("Inserisci l'ID del nuotatore da eliminare: ")
    cursor.execute("DELETE FROM nuotatori WHERE id = %s", (id,))
    mydb.commit()
    print("Nuotatore eliminato.")

def registra_allenamento():
    id = input("Inserisci l'ID dell'allenamento: ")
    nuotatore_id = input("Inserisci l'ID del nuotatore: ")
    data_allenamento = input("Inserisci la data dell'allenamento: ")
    durata = input("Inserisci la durata dell'allenamento in minuti: ")
    cursor.execute("INSERT INTO allenamenti (id, nuotatore_id, data_allenamento, durata) VALUES (%s, %s, %s, %s)", (id, nuotatore_id, data_allenamento, durata))
    mydb.commit()
    print("Allenamento registrato.")

def elimina_allenamento():
    id = input("Inserisci l'ID dell'allenamento da eliminare: ")
    cursor.execute("DELETE FROM allenamenti WHERE id = %s", (id,))
    mydb.commit()
    print("Allenamento eliminato.")


def visualizza_nuotatori():
    print("LISTA NUOTATORI")
    cursor.execute("SELECT * FROM nuotatori")
    for (id, nome, eta) in cursor.fetchall():
        print(f"ID: {id}, Nome: {nome}, Età: {eta}")

def visualizza_allenamenti():
    print("LISTA ALLENAMENTI")
    cursor.execute("SELECT * FROM allenamenti")
    for (id, nuotatore_id, data_allenamento, durata) in cursor.fetchall():
        print(f"ID: {id}, Nuotatore ID: {nuotatore_id}, Data: {data_allenamento}, Durata: {durata} minuti")


def menu():
    while True:
        print("Menu")
        print("1. Aggiungi Nuotatore")
        print("2. Modifica Nuotatore")
        print("3. Elimina Nuotatore")
        print("4. Registra Allenamento")
        print("5. Elimina Allenamento")
        print("6. Visualizza Tutti i Nuotatori")
        print("7. Visualizza Tutti gli Allenamenti")
        print("8. Esci")



        scelta = input("Scegli un'opzione: ")

        if scelta == '1':
            aggiungi_nuotatore()
        elif scelta == '2':
            modifica_nuotatore()
        elif scelta == '3':
            elimina_nuotatore()
        elif scelta == '4':
            registra_allenamento()
        elif scelta == '5':
            elimina_allenamento()
        elif scelta == '6':
            visualizza_nuotatori()
        elif scelta == '7':
            visualizza_allenamenti()
        elif scelta == '8':
            print("Uscita dal portale.")
            break
        else:
            print("Opzione selezionata non valida.")



menu()

# Chiusura connessione al database
cursor.close()
mydb.close()


