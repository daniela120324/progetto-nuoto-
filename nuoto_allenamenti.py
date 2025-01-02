class Nuotatore:
    def __init__(self, id, nome, eta):
        self.id = id
        self.nome = nome
        self.eta = eta

class Allenamento:
    def __init__(self, id, nuotatore_id, data, durata):
        self.id = id
        self.nuotatore_id = nuotatore_id
        self.data = data
        self.durata = durata

nuotatori = []
allenamenti = []

# Funzioni

def aggiungi_nuotatore():
    id = input("Inserisci l'ID del nuotatore: ")
    nome = input("Inserisci il nome del nuotatore: ")
    eta = input("Inserisci l'età del nuotatore: ")
    nuotatori.append(Nuotatore(id, nome, eta))
    print("Nuotatore aggiunto.")

def modifica_nuotatore():
    id = input("Inserisci l'ID del nuotatore da modificare: ")
    for nuotatore in nuotatori:
        if nuotatore.id == id:
            nuotatore.nome = input("Inserisci il nuovo nome del nuotatore: ")
            nuotatore.eta = input("Inserisci la nuova età del nuotatore: ")
            print("Nuotatore modificato.")
            return
    print("Nuotatore non trovato.")

def elimina_nuotatore():
    id = input("Inserisci l'ID del nuotatore da eliminare: ")
    for nuotatore in nuotatori:
        if nuotatore.id == id:
            nuotatori.remove(nuotatore)
            print("Nuotatore eliminato.")
            return
    print("Nuotatore non trovato.")

def registra_allenamento():
    id = input("Inserisci l'ID dell'allenamento: ")
    nuotatore_id = input("Inserisci l'ID del nuotatore: ")
    data = input("Inserisci la data dell'allenamento (YYYY-MM-DD): ")
    durata = input("Inserisci la durata dell'allenamento in minuti: ")
    allenamenti.append(Allenamento(id, nuotatore_id, data, durata))
    print("Allenamento registrato.")


def menu():
    while True:
        print("Menu")
        print("1. Aggiungi Nuotatore")
        print("2. Modifica Nuotatore")
        print("3. Elimina Nuotatore")
        print("4. Registra Allenamento")
        print("5. Esci")


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
            print("Uscita dal programma.")
            break

        else:
            print("Opzione non valida.")


menu()

