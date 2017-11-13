# Naam: Niek Dorrepaal
# Datum: 13-11-2017
# Versie: Afvinkopdracht 1

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():
    bestand = "alpaca.fa" # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
    
    bestand = input("Geef de naam van het fasta bestand: ")

    """
    Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
    De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
    """

    try:
        headers, seqs = lees_inhoud(bestand) 

        zoekwoord = input("Geef het zoekwoord op: ")

        # schrijf hier de rest van de code nodig om de aanroepen te doen

        for index in range(len(headers)):
            print(index, headers[index])
            print(50*'-')
            if zoekwoord in headers[index]:
                is_dna(seqs[index])
                knipt(seqs[index])
            else:
                print("Het woord dat u zoekt staat niet in de header.")
                print(50*'-')
                print()
                
    except IOError:
        print("Dit bestand is foutief.")
    
def lees_inhoud(bestands_naam):
    bestand = open(bestands_naam)
    headers = []
    seqs = []
    
    """
    Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
    Lever twee lijsten op:
        - headers = [] met daarin alle headers
        - seqs = [] met daarin alle sequenties behorend bij de headers
    Hieronder vind je de return nodig om deze twee lijsten op te leveren
    """
    seq = ""
    for line in bestand:
        line=line.strip()
        if ">" in line:
            if seq != "":
                seqs.append(seq)
                seq = ""
            headers.append(line)
        else:
            seq += line.strip()
    seqs.append(seq)
                  
    return headers, seqs

    
def is_dna(seq):
    """
    Deze functie bepaald of de sequentie (een element uit seqs) DNA is.
    Indien ja, return True
    Zo niet, return False
    """

    total = 0
    
    for ch in ('A', 'C', 'G', 'T'):
        total += seq.count(ch)

    if total == len(seq):
        print("Deze sequentie is een DNA.")
    
    else:
        print("De sequentie is geen DNA.")

    print(50*"-")

def knipt(seq):
    """
    Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken
    Deze functie bepaald of een restrictie enzym in de sequentie (een element uit seqs) knipt.
    Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
    """

    if "CCCGGG" in seq:
        print("SmaI is aanwezig in de sequenties")
    else:
        print("SmaI is in deze sequentie niet aanwezig")

    print(50*"-")


main()
