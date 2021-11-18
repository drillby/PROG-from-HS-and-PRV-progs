# print()
# for
# while
# break
# continue
# if
# elif
# else
# def
#
# 10001011     10111101 10101010          100101
# int          str      float             bool        None
# celé číslo   nápis    desetiné číslo    True/False  Nic
#
# Pole
# List                          Tuple                       range
# [ 1,"Ahoj", ["b", 1.2] ]     (1,2,4)+(5,6)->(1,2,4,5,6)   0,1,2,3,4,5...
#
# Slovník Dictionary
# {"Vek":17, "Jmeno":"Franta", "Vyska":187}


# try:
#     print("Ahoj", 5, "č", 8.9)
#     v = input("Zadej věk")  # přečte vždy nápis
#     print(int(v)*10)
# except ValueError:
#     print("Vek musí být číslo")
# except ZeroDivisionError:
#     pass


x = 10
if x < 10:
    print("X je menší než 10")
elif x == 10:
    print("X je rovno 10")
elif x == 20:
    print("X je rovno 20")
else:
    print("X je větší než 10")
    
for prvek in ["Nazdar", 5, "č", 5.8, ["a", 4]]:
    print("Prvek:", prvek)
    
y = 0
while y < 10:
    if y == 6:
        break  # skoč za konec whilecyklus
    
    if y == 2:
        y += 1
        continue  # skoč na podmínku whilecyklu
    print(y)
    y += 1  # y = y+1
    
print("Tady je y", y)


l = ["Nazdar", 5, "č", 5.8, ["a", 4]]
# index 0      1   2    3       4
print(l)
print(l[1])
l[1] = "Cauves"
print(l)
l.append(94)
print(l)

print("==========")
t = ("Nazdar", 5, "č", 5.8, ["a", 4])
# index 0      1   2    3       4
print(t)
print(t[1])
novylist = list(t)
novytuple = tuple(novylist)

print("=======")
print(range(3,10))
print(*range(3,10))
print(range(3,20, 2))
print(*range(3,20, 2))

print("=======")
s = {"Vek":17, "Jmeno":"Franta", "Vyska":187}
print(s)
print(s["Jmeno"])

print("=======")


def moje_funkce(x):
    y = 2*x
    z = y + 10
    return z


vysledek = moje_funkce(5)
print(vysledek)
vysledek = moje_funkce(10)
print(vysledek)
print(moje_funkce(40))





