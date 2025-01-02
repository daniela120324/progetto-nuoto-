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
    print("Nuotatore aggiunto con successo.")

def modifica_nuotatore():
    id = input("Inserisci l'ID del nuotatore da modificare: ")
    for nuotatore in nuotatori:
        if nuotatore.id == id:
            nuotatore.nome = input("Inserisci il nuovo nome del nuotatore: ")
            nuotatore.eta = input("Inserisci la nuova età del nuotatore: ")
            print("Nuotatore modificato con successo.")
            return
    print("Nuotatore non trovato.")

def elimina_nuotatore():
    id = input("Inserisci l'ID del nuotatore da eliminare: ")
    for nuotatore in nuotatori:
        if nuotatore.id == id:
            nuotatori.remove(nuotatore)
            print("Nuotatore eliminato con successo.")
            return
    print("Nuotatore non trovato.")

def menu():
    while True:
        print("Menu")
        print("1. Aggiungi Nuotatore")
        print("2. Modifica Nuotatore")
        print("3. Elimina Nuotatore")

        scelta = input("Scegli un'opzione: ")

        if scelta == '1':
            aggiungi_nuotatore()
        elif scelta == '2':
            modifica_nuotatore()
        elif scelta == '3':
            elimina_nuotatore()
        else:
            print("Opzione non valida.")


menu()

