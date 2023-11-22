#Hexadecimal a Binario, octal y Decimal
def hextonum(hex):
    pnum = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10
        }
    if hex in pnum:
        return pnum[hex]
    else:
        return int (hex)
def hextodec2(hex):
    hex = hex.lower()
    hex = hex[::-1]
    decimal = 0
    posición = 0
    for digit in hex:
        valor = hextonum(digit)
        elevado = 16 ** posición
        pnum = elevado * valor
        decimal += pnum
        posición += 1
    return decimal
def hextobin(número):
    a=int(número,16)
    return hextobin (a)

def hextooct(número):
    a=int(número,16)
    return hextooct(a)

def hextodec(número):
    a=int(hextodec2)(número)
    return a