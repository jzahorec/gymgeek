nakupni_list = []

##for i in range(10):
##    nakupni_list.append(input("Zadej vec do kosiku: "))

vec = input("Zadej věc do košíku: ")

while vec != "":
    nakupni_list.append(vec)
    vec = input("Zadej věc do košíku: ")

print ("Běž na nákup!")

# V obchodě
print("--- OBCHOD ---")

for i in range(len(nakupni_list)):
    zbozi = input("> ")

    if zbozi in nakupni_list:
        print("Je to v košíku.")
        nakupni_list.remove(zbozi)
    else:
        print("Měl jsi koupit něco jiného!")


for nenakoupene_zbozi in nakupni_list:
    print("Nenakoupil jsi: " + nenakoupene_zbozi)
