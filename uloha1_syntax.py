# Zadání - seznam
chars = [65, 656, 111, 74, 32, 106, 101, 32, 146, 111, 268, 692,
         203, 137, 267, 268, 214, 179, 375, 199, -53, 626, 192, 62,
         194, 185, 195, 268, 146, 183, 184, 662, 268, 280, 192, 189,
         196, 183, 62, 242, 259, 272, 268, 114, 199, 29, 268, 183,
         412, 268, 185, 626, 268, 136, 195, 268, 191, -67, 412, 199,
         -53, 188, 200, 255, 184, 268, 190, 203, 62, 229, 195, 692,
         228, 147, 202, 254]

result = ""

# Jestliže je seznam prázdný, tak můžeme skončit
if (len(chars) < 0):
    exit

# Procházíme celý seznam podle indexu
for index in range(len(chars)):
    ch = chars[index]
                   
    if index % 5 == 3:
        result += chr(ch - 30)
    elif index % 10 == 1:
        result += chr((ch + 4) // 6)
    elif index < 10:
        result += chr(ch)
    else:
        result += chr(300 - ch)

print (result)
