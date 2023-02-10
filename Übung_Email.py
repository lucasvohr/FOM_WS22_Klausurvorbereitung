import re

datensatz = "Dies ist meine Email-Adresse: test.name42@testfirma.de"
muster_1 = "[a-z A-Z 0-9 _ , \.]+@[a-z A-Z 0-9]+\.[a-z A-Z]+"
muster_2 = "[\w.-]+@[\w]+\.[\w]+"

ergebnis = re.search(muster_1, datensatz)


if ergebnis:
    gefunden = ergebnis.group()
    print("gefunden wurde: ", gefunden)
else:
    print("nicht gefunden")

