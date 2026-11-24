from datetime import datetime, timedelta

nu = datetime.now()

nodig = False
if nodig:
    geboorteDag = int(input("Vul je geboortedag in: "))
    geboorteMaand = int(input("Vul je geboortemaand in: "))
    geboorteJaar = int(input("Vul je geboortejaar in: "))

def opdracht1():
    print(datetime.now())

def opdracht2():
    print(f"Jaar: {geboorteJaar} Maand: {geboorteMaand} Dag: {geboorteDag}")

def opdracht3():
    print(datetime.now().strftime("%A %d %B %Y"))

def opdracht4():
    nu = datetime.now()
    maand = int(input("Vul een maand in: "))
    dag = int(input("Vul een dag in: "))

    userDatum = datetime(nu.year, maand, dag)

    dagen_verschil = (userDatum - nu).days

    print(dagen_verschil + " dagen verschil")

def opdracht5():
    # Vraag de gebruiker om een geboortedatum
    geboorte_dag = int(input("Voer je geboortedag in: "))
    geboorte_maand = int(input("Voer je geboortemaand in: "))

    # Huidig jaar
    vandaag = datetime.today()
    verjaardag = datetime(vandaag.year, geboorte_maand, geboorte_dag)

    # Als de verjaardag al voorbij is dit jaar, neem volgend jaar
    if verjaardag < vandaag:
        verjaardag = datetime(vandaag.year + 1, geboorte_maand, geboorte_dag)

    # Bereken het aantal dagen tot de verjaardag
    dagen_te_gaan = (verjaardag - vandaag).days
    week_dag = verjaardag.strftime("%A")
    print(f"Je verjaardag is over {dagen_te_gaan} dagen! Je verjaardag is op een {week_dag}!")