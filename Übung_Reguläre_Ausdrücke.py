import re


text = "!!! Wellcome to the real world"
print("\nIm Folgenden wird nur abgefragt, ob ein Text oder Muster gefunden wurde.\nAusgangstext: ", text, "\n")

#-----Suche mit [ZEICHENKETTE]-----
print("Suchen mit ZEICHENKETTE")
muster = "re.l"
if(re.search(muster, text)):
    print("Suche mit (re.l) ==> gefunden\n")
else:
    print("Suche mit (re.l) ==> nicht gefunden\n")


#-----Suche mit [KLASSEN]-----
print("Muster mit KLASSEN")
muster = "r[e]al"
if(re.search(muster, text)):
    print("Suche mit (r[e]al) ==> gefunden\n")
else:
    print("Suche mit (r[e]al) ==> nicht gefunden\n")


#-----Suche mit [KLASSEN MIT SUCHBEREICH]-----
print("Muster mit Klassen mit SUCHBEREICH")
muster = "r[a-z]al"
if(re.search(muster, text)):
    print("Suche mit (r[a-z]al) ==> gefunden\n")
else:
    print("Suche mit (r[a-z]al) ==> nicht gefunden\n")


#-----Suche mit [KLASSEN MIT OPERATOREN]-----
print("Muster mit Klassen mit SUCHBEREICH")

muster = "rea\d"
if(re.search(muster, text)):
    print("Suche mit (rea\d) für Zahlen ==> gefunden")
else:
    print("Suche mit (rea\d) für Zahlen ==> nicht gefunden")

muster = "rea\w"
if(re.search(muster, text)):
    print("Suche mit (rea\w) für Buchstaben und Zahlen ==> gefunden")
else:
    print("Suche mit (rea\w) für Buchstaben und Zahlen ==> nicht gefunden")

muster = "rea\s"
if(re.search(muster, text)):
    print("Suche mit (rea\s) für Trennzeichen ==> gefunden\n")
else:
    print("Suche mit (rea\s) für Trennzeichen ==> nicht gefunden\n")


#-----Suche mit [INDEX]-----
print("Muster mit Klassen mit SUCHBEREICH")

muster = "^Wellcome"
if(re.search(muster, text)):
    print("Suche mit (^Wellcome) für Anfang des Ausdrucks ==> gefunden")
else:
    print("Suche mit (^Wellcome) für Anfang des Ausdrucks ==> nicht gefunden")

muster = "Wellcome$"
if(re.search(muster, text)):
    print("Suche mit (^Wellcome) für Ende des Ausdrucks ==> gefunden\n")
else:
    print("Suche mit (^Wellcome) für Ende des Ausdrucks ==> nicht gefunden\n")

# Umgang mit wiederkehrenden (optionale oder redundante) Informationen
text = "01.08.2018"
print("\n\nAusgangstext: ", text, "\n")

#-----Suche mit [optionalen Ausdrücken]-----
print("Muster mit Klassen mit OPTIONALEN AUSDRÜCKEN")

muster = "0?\d\."
if(re.search(muster, text)):
    print("Suche mit (0?\d\.) für optionale Ausdrücke ==> gefunden\n")
else:
    print("Suche mit (0?\d\.) für optionale Ausdrücke ==> nicht gefunden\n")


# Ab hier Prüfung auf Position im Text
text = "Die Konstante PI lautet: 3.141592"
print("\n------------------------\nIm Folgenden wird nun auch die Position und das Suchergebnis abgefragt.\nAusgangstext: ", text, "\n")

