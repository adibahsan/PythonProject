str = "The Quick brown fox"

str2 = str[::2]

for x in str2:
    print(x, end="--> ")
print()

print(str[len(str) - 1:len(str) - 10:-1])
print(str[len(str) - 9:len(str)])

strReplaced = str.replace("Quick", "Slow")

print(str)
print(strReplaced)

print("you make me alive".strip("alive"))
print("")

f1 = 6
f2 = 3
print(f"{f1} + {f2} = {f1 + f2}")
