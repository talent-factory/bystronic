#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 2
Übung 3: Listen und Dictionaries

Diese Übung behandelt:
- Listen: Erstellung, Manipulation, List Comprehensions
- Dictionaries: Key-Value-Paare, verschachtelte Strukturen
- Sets: Mengenoperationen, eindeutige Elemente
- Tupel: Unveränderliche Datenstrukturen
- Praktische Anwendungen für Produktionsdaten
"""


def aufgabe_1_listen_grundlagen():
    """Aufgabe 1: Listen-Grundlagen"""
    print("AUFGABE 1: Listen-Grundlagen")
    print("-" * 40)

    # TODO: Erstellen Sie folgende Listen:
    # 1. maschinen: ["Laser", "Presse", "Stanze", "CNC", "Schweissroboter"]
    # 2. produktionszeiten: [8.5, 7.2, 9.1, 6.8, 8.0]
    # 3. teilenummern: ["P001", "P002", "P003", "P001", "P004", "P002"]

    # Ihre Lösung hier:
    # maschinen = ...
    # produktionszeiten = ...
    # teilenummern = ...

    # TODO: Listen-Operationen durchführen:
    # 1. Fügen Sie "Plasma" zu den Maschinen hinzu
    # 2. Fügen Sie "Biege" an Position 2 ein
    # 3. Entfernen Sie "CNC" aus der Liste
    # 4. Finden Sie die längste Produktionszeit
    # 5. Sortieren Sie die Produktionszeiten

    # Ihre Lösung hier:

    # TODO: List Comprehensions:
    # 1. Alle Produktionszeiten > 8.0 Stunden
    # 2. Quadrierte Werte aller Produktionszeiten
    # 3. Maschinentypen die mit "L" oder "P" beginnen

    # ueberstunden = [zeit for zeit in produktionszeiten if ...]
    # quadrate = [zeit**2 for zeit in ...]
    # l_oder_p_maschinen = [maschine for maschine in ... if ...]

    # TODO: Listen-Statistiken:
    # - Durchschnittliche Produktionszeit
    # - Anzahl eindeutiger Teilenummern
    # - Häufigste Teilenummer

    # Ihre Lösung hier:

    print("✅ Aufgabe 1 abgeschlossen!\n")


def aufgabe_2_dictionaries():
    """Aufgabe 2: Dictionaries"""
    print("AUFGABE 2: Dictionaries")
    print("-" * 40)

    # TODO: Erstellen Sie ein Dictionary für eine Maschine:
    laser_001 = {
        # "id": "LASER_001",
        # "typ": "ByStar Fiber",
        # "leistung": 6000,  # Watt
        # "baujahr": 2020,
        # "aktiv": True,
        # "standort": "Halle A"
    }

    # TODO: Dictionary-Operationen:
    # 1. Fügen Sie "wartung_datum": "2024-07-15" hinzu
    # 2. Ändern Sie die Leistung auf 8000 Watt
    # 3. Entfernen Sie das Baujahr
    # 4. Prüfen Sie, ob "standort" vorhanden ist

    # Ihre Lösung hier:

    # TODO: Verschachteltes Dictionary für Produktionsanlage:
    produktionsanlage = {
        "name": "Fertigung Halle A",
        "maschinen": {
            # "LASER_001": {
            #     "typ": "ByStar Fiber",
            #     "status": "Aktiv",
            #     "produktion": {
            #         "heute": 145,
            #         "diese_woche": 720,
            #         "diesen_monat": 3200
            #     },
            #     "wartung": {
            #         "letzter_service": "2024-01-15",
            #         "naechster_service": "2024-07-15"
            #     }
            # },
            # Fügen Sie weitere Maschinen hinzu...
        },
        "personal": [
            # {"name": "Max", "schicht": "Tag", "qualifikationen": ["Laser", "Presse"]},
            # {"name": "Anna", "schicht": "Nacht", "qualifikationen": ["Laser", "CNC"]},
            # Fügen Sie weiteres Personal hinzu...
        ],
    }

    # TODO: Navigieren Sie durch die verschachtelte Struktur:
    # 1. Geben Sie alle Maschinen-IDs aus
    # 2. Berechnen Sie die Gesamtproduktion heute
    # 3. Finden Sie alle Mitarbeiter mit Laser-Qualifikation
    # 4. Erstellen Sie eine Liste aller Qualifikationen (ohne Duplikate)

    # Ihre Lösung hier:

    # TODO: Dictionary Comprehension:
    # Erstellen Sie ein Dictionary mit Maschine -> Produktivität (Teile/Tag)

    # produktivitaet = {maschine: daten["produktion"]["heute"]
    #                   for maschine, daten in produktionsanlage["maschinen"].items()}

    print("✅ Aufgabe 2 abgeschlossen!\n")


def aufgabe_3_sets():
    """Aufgabe 3: Sets (Mengen)"""
    print("AUFGABE 3: Sets (Mengen)")
    print("-" * 40)

    # Gegeben: Materialien pro Maschinentyp
    laser_materialien = {"Stahl", "Aluminium", "Edelstahl", "Kupfer"}
    presse_materialien = {"Aluminium", "Kupfer", "Messing", "Titan"}
    cnc_materialien = {"Stahl", "Aluminium", "Titan", "Kunststoff"}

    print(f"Laser kann verarbeiten: {laser_materialien}")
    print(f"Presse kann verarbeiten: {presse_materialien}")
    print(f"CNC kann verarbeiten: {cnc_materialien}")

    # TODO: Mengenoperationen durchführen:
    # 1. Alle verfügbaren Materialien (Vereinigung)
    # 2. Materialien die alle drei Maschinen verarbeiten können (Schnittmenge)
    # 3. Materialien nur für Laser (Differenz)
    # 4. Materialien entweder für Laser oder Presse, aber nicht beide

    # alle_materialien = ...
    # gemeinsame_alle = ...
    # nur_laser = ...
    # laser_oder_presse = ...

    # TODO: Operatoren-Qualifikationen:
    laser_operatoren = {"Max", "Anna", "Peter", "Sarah"}
    presse_operatoren = {"Anna", "Tom", "Sarah", "Lisa"}
    cnc_operatoren = {"Peter", "Tom", "Michael", "Anna"}

    # Finden Sie:
    # 1. Universal-Operatoren (können alle drei Maschinen bedienen)
    # 2. Operatoren die mindestens zwei Maschinen bedienen können
    # 3. Operatoren die nur eine Maschine bedienen können

    # Ihre Lösung hier:

    # TODO: Duplikate aus Messdaten entfernen:
    messwerte = [2.1, 2.0, 2.1, 1.95, 2.0, 2.05, 2.1, 1.95, 2.0]

    # eindeutige_werte = ...
    # anzahl_duplikate = ...

    print("✅ Aufgabe 3 abgeschlossen!\n")


def aufgabe_4_tupel():
    """Aufgabe 4: Tupel"""
    print("AUFGABE 4: Tupel")
    print("-" * 40)

    # TODO: Erstellen Sie Tupel für:
    # 1. Maschinenposition (x, y, z): (10.5, 20.8, 0.0)
    # 2. RGB-Farbcode für Statusanzeige: (255, 0, 0) für Rot
    # 3. Produktionsparameter: ("BSF-6000", 2.5, 150, True) für (Typ, Dicke, Anzahl, OK)

    # position = ...
    # farbe_rot = ...
    # parameter = ...

    # TODO: Tupel-Entpackung:
    # Entpacken Sie die Position in x, y, z Variablen
    # x, y, z = ...

    # TODO: Tupel als Dictionary-Schlüssel:
    # Erstellen Sie ein Dictionary mit Positionen als Schlüssel
    maschinenpositionen = {
        # (0, 0): "Lagerplatz",
        # (10, 20): "Laser Station 1",
        # (15, 35): "Presse Station 1",
        # (25, 40): "Qualitätskontrolle"
    }

    # TODO: Mehrere Werte von einer Funktion zurückgeben:
    def analysiere_teil(laenge, breite, dicke, soll_laenge, soll_breite, soll_dicke):
        """
        Analysiert ein Teil und gibt (ist_ok, abweichungen, volumen) zurück
        """
        # toleranz = 0.1
        # laenge_ok = abs(laenge - soll_laenge) <= toleranz
        # breite_ok = abs(breite - soll_breite) <= toleranz
        # dicke_ok = abs(dicke - soll_dicke) <= toleranz
        # ist_ok = laenge_ok and breite_ok and dicke_ok
        #
        # abweichungen = (
        #     abs(laenge - soll_laenge),
        #     abs(breite - soll_breite),
        #     abs(dicke - soll_dicke)
        # )
        #
        # volumen = laenge * breite * dicke
        #
        # return ist_ok, abweichungen, volumen
        pass

    # TODO: Testen Sie die Funktion:
    testteile = [
        (100.05, 50.02, 2.08, 100.0, 50.0, 2.0),
        (99.85, 49.95, 2.15, 100.0, 50.0, 2.0),
        (100.20, 50.12, 1.95, 100.0, 50.0, 2.0),
    ]

    for i, (l, b, d, sl, sb, sd) in enumerate(testteile, 1):
        # ok, abw, vol = analysiere_teil(l, b, d, sl, sb, sd)
        # status = "✅ OK" if ok else "❌ NOK"
        # print(f"Teil {i}: {status}, Abweichungen: {abw}, Volumen: {vol:.2f}")
        pass

    print("✅ Aufgabe 4 abgeschlossen!\n")


def aufgabe_5_produktionsdaten_management():
    """Aufgabe 5: Produktionsdaten-Management"""
    print("AUFGABE 5: Produktionsdaten-Management")
    print("-" * 40)

    # TODO: Implementieren Sie ein System zur Verwaltung von Produktionsdaten
    # Verwenden Sie alle gelernten Collection-Typen

    class ProduktionsDatenManager:
        def __init__(self):
            # TODO: Initialisieren Sie die Datenstrukturen:
            # self.maschinen = {}  # Dictionary: id -> maschinen_info
            # self.materialien = set()  # Set aller verfügbaren Materialien
            # self.produktionsverlauf = []  # Liste der Produktionseinträge
            # self.qualitaetsdaten = {}  # Dictionary: teil_id -> qualitätsdaten
            pass

        def registriere_maschine(self, maschinen_id, typ, materialien_liste):
            """Registriert eine neue Maschine"""
            # TODO: Implementieren
            pass

        def erfasse_produktion(
            self, maschinen_id, teil_id, material, anzahl, qualitaet_ok
        ):
            """Erfasst einen Produktionseintrag"""
            # TODO: Implementieren
            # Fügen Sie Eintrag zu produktionsverlauf hinzu (Tupel mit Timestamp)
            # Aktualisieren Sie verfügbare Materialien
            pass

        def erstelle_tagesbericht(self, datum):
            """Erstellt einen Tagesbericht"""
            # TODO: Implementieren
            # Filtern Sie Produktionsdaten nach Datum
            # Berechnen Sie Zusammenfassungen pro Maschine
            pass

        def finde_kompatible_maschinen(self, material):
            """Findet alle Maschinen die ein Material verarbeiten können"""
            # TODO: Implementieren
            pass

        def berechne_ausschussrate(self, maschinen_id=None):
            """Berechnet Ausschussrate (gesamt oder pro Maschine)"""
            # TODO: Implementieren
            pass

    # TODO: Testen Sie das System:
    manager = ProduktionsDatenManager()

    # Maschinen registrieren
    # manager.registriere_maschine("LASER_001", "ByStar Fiber", ["Stahl", "Aluminium", "Edelstahl"])
    # manager.registriere_maschine("PRESSE_001", "Xpert Pro", ["Aluminium", "Kupfer", "Messing"])

    # Produktionsdaten erfassen (simuliert)
    # heute = date.today()
    # testdaten = [
    #     ("LASER_001", "P001", "Stahl", 150, True),
    #     ("LASER_001", "P002", "Aluminium", 120, False),
    #     ("PRESSE_001", "P003", "Kupfer", 89, True),
    # ]

    # for maschine, teil, material, anzahl, ok in testdaten:
    #     manager.erfasse_produktion(maschine, teil, material, anzahl, ok)

    # Berichte erstellen
    # bericht = manager.erstelle_tagesbericht(heute)
    # print(f"Tagesbericht: {bericht}")

    # kompatible = manager.finde_kompatible_maschinen("Aluminium")
    # print(f"Maschinen für Aluminium: {kompatible}")

    # ausschussrate = manager.berechne_ausschussrate()
    # print(f"Gesamte Ausschussrate: {ausschussrate:.1f}%")

    print("✅ Aufgabe 5 abgeschlossen!\n")


def bonus_aufgabe_datenstrukturen_optimierung():
    """Bonus-Aufgabe: Datenstrukturen-Optimierung"""
    print("BONUS-AUFGABE: Performance-Optimierung")
    print("-" * 40)

    # TODO: Vergleichen Sie die Performance verschiedener Datenstrukturen

    import time

    def messe_zeit(funktion):
        """Hilfsfunktion zur Zeitmessung"""
        start = time.time()
        ergebnis = funktion()
        ende = time.time()
        return ende - start, ergebnis

    # TODO: Erstellen Sie grosse Datenmengen für Tests
    # grosse_liste = list(range(100000))
    # grosses_set = set(range(100000))
    # grosses_dict = {i: f"Wert_{i}" for i in range(100000)}

    print("Performance-Tests:")
    print("-" * 30)

    # TODO: Test 1 - Mitgliedschaftsprüfung (in operator)
    # Vergleichen Sie: 99999 in grosse_liste vs. 99999 in grosses_set

    # def liste_suche():
    #     return 99999 in grosse_liste

    # def set_suche():
    #     return 99999 in grosses_set

    # zeit_liste, _ = messe_zeit(liste_suche)
    # zeit_set, _ = messe_zeit(set_suche)

    # print(f"Suche in Liste: {zeit_liste:.6f}s")
    # print(f"Suche in Set: {zeit_set:.6f}s")
    # print(f"Set ist {zeit_liste/zeit_set:.1f}x schneller")

    # TODO: Test 2 - Duplikate entfernen
    # Listen-Methode vs. Set-Konvertierung

    # duplikate_liste = [random.randint(0, 1000) for _ in range(10000)]

    # def duplikate_mit_liste():
    #     eindeutig = []
    #     for item in duplikate_liste:
    #         if item not in eindeutig:
    #             eindeutig.append(item)
    #     return eindeutig

    # def duplikate_mit_set():
    #     return list(set(duplikate_liste))

    # TODO: Test 3 - Dictionary vs. Liste für Lookups
    # Erstellen Sie ein Dictionary und eine Liste mit gleichen Daten
    # Vergleichen Sie die Geschwindigkeit für Wertesuche

    # TODO: Geben Sie Empfehlungen für die Wahl der Datenstruktur
    print(
        """
EMPFEHLUNGEN FÜR DATENSTRUKTUREN:

1. LISTE verwenden für:
   - Geordnete Daten
   - Index-basierten Zugriff
   - Wenn Duplikate erlaubt sind

2. SET verwenden für:
   - Schnelle Mitgliedschaftsprüfung (in/not in)
   - Eindeutige Elemente
   - Mengenoperationen

3. DICTIONARY verwenden für:
   - Key-Value Zuordnungen
   - Schnelle Lookups über Keys
   - Strukturierte Daten

4. TUPEL verwenden für:
   - Unveränderliche Daten
   - Dictionary-Keys
   - Funktionsrückgabewerte
    """
    )

    print("✅ Bonus-Aufgabe abgeschlossen!\n")


def loesung_anzeigen():
    """Zeigt die Musterlösung an"""
    antwort = input("Möchten Sie die Musterlösung anzeigen? (j/n): ").lower().strip()
    if antwort in ["j", "ja", "y", "yes"]:
        print("\n" + "=" * 50)
        print("MUSTERLÖSUNG")
        print("=" * 50)

        print(
            """
# Aufgabe 1: Listen-Grundlagen
maschinen = ["Laser", "Presse", "Stanze", "CNC", "Schweissroboter"]
produktionszeiten = [8.5, 7.2, 9.1, 6.8, 8.0]
teilenummern = ["P001", "P002", "P003", "P001", "P004", "P002"]

maschinen.append("Plasma")
maschinen.insert(2, "Biege")
maschinen.remove("CNC")
max_zeit = max(produktionszeiten)
sortierte_zeiten = sorted(produktionszeiten)

ueberstunden = [zeit for zeit in produktionszeiten if zeit > 8.0]
quadrate = [zeit**2 for zeit in produktionszeiten]
l_oder_p_maschinen = [m for m in maschinen if m.startswith(('L', 'P'))]

durchschnitt = sum(produktionszeiten) / len(produktionszeiten)
eindeutige_teile = len(set(teilenummern))
haeufigste = max(set(teilenummern), key=teilenummern.count)

# Aufgabe 2: Dictionaries
laser_001 = {
    "id": "LASER_001",
    "typ": "ByStar Fiber",
    "leistung": 6000,
    "baujahr": 2020,
    "aktiv": True,
    "standort": "Halle A"
}

laser_001["wartung_datum"] = "2024-07-15"
laser_001["leistung"] = 8000
del laser_001["baujahr"]
hat_standort = "standort" in laser_001

# Verschachtelte Struktur
alle_maschinen_ids = list(produktionsanlage["maschinen"].keys())
gesamt_produktion = sum(m["produktion"]["heute"] for m in produktionsanlage["maschinen"].values())

laser_mitarbeiter = [p["name"] for p in produktionsanlage["personal"]
                    if "Laser" in p["qualifikationen"]]

alle_qualifikationen = set()
for person in produktionsanlage["personal"]:
    alle_qualifikationen.update(person["qualifikationen"])

# Aufgabe 3: Sets
alle_materialien = laser_materialien | presse_materialien | cnc_materialien
gemeinsame_alle = laser_materialien & presse_materialien & cnc_materialien
nur_laser = laser_materialien - presse_materialien
laser_oder_presse = laser_materialien ^ presse_materialien

universal_operatoren = laser_operatoren & presse_operatoren & cnc_operatoren
mindestens_zwei = set()
for op in laser_operatoren | presse_operatoren | cnc_operatoren:
    count = 0
    if op in laser_operatoren: count += 1
    if op in presse_operatoren: count += 1
    if op in cnc_operatoren: count += 1
    if count >= 2:
        mindestens_zwei.add(op)

eindeutige_werte = sorted(list(set(messwerte)))
anzahl_duplikate = len(messwerte) - len(set(messwerte))

# Aufgabe 4: Tupel
position = (10.5, 20.8, 0.0)
farbe_rot = (255, 0, 0)
parameter = ("BSF-6000", 2.5, 150, True)

x, y, z = position

maschinenpositionen = {
    (0, 0): "Lagerplatz",
    (10, 20): "Laser Station 1",
    (15, 35): "Presse Station 1",
    (25, 40): "Qualitätskontrolle"
}

def analysiere_teil(laenge, breite, dicke, soll_laenge, soll_breite, soll_dicke):
    toleranz = 0.1
    laenge_ok = abs(laenge - soll_laenge) <= toleranz
    breite_ok = abs(breite - soll_breite) <= toleranz
    dicke_ok = abs(dicke - soll_dicke) <= toleranz
    ist_ok = laenge_ok and breite_ok and dicke_ok

    abweichungen = (
        abs(laenge - soll_laenge),
        abs(breite - soll_breite),
        abs(dicke - soll_dicke)
    )

    volumen = laenge * breite * dicke
    return ist_ok, abweichungen, volumen

# Aufgabe 5: Produktionsdaten-Management
class ProduktionsDatenManager:
    def __init__(self):
        self.maschinen = {}
        self.materialien = set()
        self.produktionsverlauf = []
        self.qualitaetsdaten = {}

    def registriere_maschine(self, maschinen_id, typ, materialien_liste):
        self.maschinen[maschinen_id] = {
            "typ": typ,
            "materialien": set(materialien_liste),
            "registriert": datetime.now()
        }
        self.materialien.update(materialien_liste)

    def erfasse_produktion(self, maschinen_id, teil_id, material, anzahl, qualitaet_ok):
        eintrag = (datetime.now(), maschinen_id, teil_id, material, anzahl, qualitaet_ok)
        self.produktionsverlauf.append(eintrag)
        self.materialien.add(material)

        if teil_id not in self.qualitaetsdaten:
            self.qualitaetsdaten[teil_id] = []
        self.qualitaetsdaten[teil_id].append(qualitaet_ok)

    def finde_kompatible_maschinen(self, material):
        return [mid for mid, daten in self.maschinen.items()
                if material in daten["materialien"]]

    def berechne_ausschussrate(self, maschinen_id=None):
        relevante_eintraege = self.produktionsverlauf
        if maschinen_id:
            relevante_eintraege = [e for e in relevante_eintraege if e[1] == maschinen_id]

        if not relevante_eintraege:
            return 0.0

        gesamt = len(relevante_eintraege)
        nok = len([e for e in relevante_eintraege if not e[5]])
        return (nok / gesamt) * 100
"""
        )


def main():
    """Hauptfunktion der Übung"""
    print("=" * 50)
    print("BYSTRONIC PYTHON GRUNDKURS")
    print("Kapitel 2 - Übung 3: Collections")
    print("=" * 50)

    print(
        """
Diese Übung behandelt die wichtigsten Collection-Typen in Python:
• Listen: Dynamische Arrays mit vielen Methoden
• Dictionaries: Key-Value-Paare für strukturierte Daten
• Sets: Mengen mit eindeutigen Elementen
• Tupel: Unveränderliche, geordnete Sammlungen

Bearbeiten Sie die Aufgaben der Reihe nach und implementieren
Sie die TODO-Kommentare.
"""
    )

    try:
        aufgabe_1_listen_grundlagen()
        aufgabe_2_dictionaries()
        aufgabe_3_sets()
        aufgabe_4_tupel()
        aufgabe_5_produktionsdaten_management()
        bonus_aufgabe_datenstrukturen_optimierung()

        print("🎉 Alle Aufgaben abgeschlossen!")
        print("\nSie haben erfolgreich gelernt:")
        print("✓ Listen für dynamische Datensammlungen zu verwenden")
        print("✓ Dictionaries für strukturierte Key-Value-Daten zu nutzen")
        print("✓ Sets für Mengenoperationen und eindeutige Elemente")
        print("✓ Tupel für unveränderliche Datenstrukturen")
        print("✓ Komplexe Datenstrukturen zu modellieren")
        print("✓ Die richtige Datenstruktur für verschiedene Anwendungen zu wählen")

        loesung_anzeigen()

    except KeyboardInterrupt:
        print("\n\nÜbung durch Benutzer abgebrochen.")
    except Exception as e:
        print(f"\nFehler in der Übung: {e}")
        print("Überprüfen Sie Ihre Implementierung und versuchen Sie es erneut.")


if __name__ == "__main__":
    main()

    print("\nDrücken Sie Enter zum Beenden...")
    input()
