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
    data = input("Inserisci la data dell'allenamento: ")
    durata = input("Inserisci la durata dell'allenamento in minuti: ")
    allenamenti.append(Allenamento(id, nuotatore_id, data, durata))
    print("Allenamento registrato.")

def elimina_allenamento():
    id = input("Inserisci l'ID dell'allenamento da eliminare: ")
    for allenamento in allenamenti:
        if allenamento.id == id:
            allenamenti.remove(allenamento)
            print("Allenamento eliminato.")
            return
    print("Allenamento non trovato.")

def visualizza_nuotatori():
    print("LISTA NUOTATORI")
    for nuotatore in nuotatori:
        print(f"ID: {nuotatore.id}, Nome: {nuotatore.nome}, Età: {nuotatore.eta}")

def visualizza_allenamenti():
    print("LISTA ALLENAMENTI")
    for allenamento in allenamenti:
        print(f"ID: {allenamento.id}, Nuotatore ID: {allenamento.nuotatore_id}, Data: {allenamento.data}, Durata: {allenamento.durata} minuti")



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

