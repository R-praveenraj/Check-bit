def checkBit(number,bit):
    for i in range(bit):
        number >>= 1
    if number & 1:
        return 1
    else:
        return 0


number=int(input())
bit=int(input())
print(checkBit(number,bit))