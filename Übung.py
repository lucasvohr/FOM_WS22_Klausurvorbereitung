a = "Testtext"
b = 30
c = 1.43

print(a)
print(b)
print(c)

# b muss über einen Typecast in String umgewandelt werden, weil andernfalls eine Exception geworfen wird
print(a + " " + str(b))
#print(a + 5)

txt_1 = "Ein"
txt_2 ="super Test"
print(txt_1 + " " + txt_2)

print(c, "zusammen mit einem String")

print(a, b, c, sep = "__")
print("%10.3f" % (c))

print("----------------\n")

# hier wirkt das PLUS nicht als Konkatination sondern mathematisch als Addition
print(b + c)

print("----------------\n")

# Hier wird FÜNFMAL der Text von [a] ausgegeben
print(a * 5)

print("----------------\n")

# Es gilt grundsätzlich: wird ein String "multipliziert", wird dieser einfach vervielfältigt
var = "python" * 5
print(var)

print("----------------\n")

# Konkatination von Strings
var_1 = "Test-String"
var_2 = " direkt aus der Hölle"
var_3 = var_1 + var_2
print(var_3)

print("----------------\n")

# IF-Abfragen
if 2 < b < 10:
    print(str(b) + " ist größer als 2")
elif b > 10:
    print(str(b) + " ist größer als 10")
else:
    print(str(b) + " ist kleiner als 2")

print("----------------\n")

# WHILE-Schleife
while b > 0:
    print(b)
    # post-dekrement existiert in Python nicht, daher b = b - 1
    b = b - 1

print("----------------\n")

# FOR-Schleife
c = 30
for i in range (0, c):
    print(c-i)

print("----------------\n")

def Testfunktion(input):
    print(input, "\n")
    return("DONE")

Testfunktion(c)
Testfunktion(a)

ergebnis = Testfunktion("Super Duper Text")
print(ergebnis)

print("----------------\n")

def no_return(in_a, in_b):
    res = in_a + in_b

zwischenergebnis = no_return(3,3)
print(zwischenergebnis)


print("----------------\n")

def Hallo(name="Python-Nutzer"):
    print("Hallo " + name + "!")

Hallo()
Hallo("Joe")


print("----------------\n")

def f():
    global s
    print(s)
    s = "Perl"
    print(s)

s = "Python"
f()
print(s)

print("----------------\n")

def c():
    g = "Perl"
    print(g)

g = "Python"
c()
print(g)