# Scope

# Local scope: the variables and functions only may be accessed
# or have local scope inside their respective current symbol table

def convertFtoC(temp):
    convertedTemp = (5 / 9) * (temp - 32)
    return convertedTemp

tempInF = 32
print(convertFtoC(tempInF))

tempInF = 212
print(convertFtoC(tempInF))

# Here the variable convertedTemp has a global scope
def convertFtoC_2(temp):
    global convertedTemp
    convertedTemp = (5 / 9) * (temp - 32)
    return convertedTemp

tempInF_2 = 212
print(convertFtoC_2(tempInF_2))
print(convertedTemp)