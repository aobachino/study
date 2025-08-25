

plain = "Everything Everywhere all at once".replace(" ", "").lower()

enc = [4,3,1,2]
dec = [1,2,3,4]

print(plain)
# print(len(plain))
plainList = []
cnt = 0
text = ""
for i in range(0, len(plain)):
    
    text += plain[i]
    cnt = cnt + 1
    if cnt == len(enc):
        # print(text)
        plainList.append(text)        
        cnt = 0
        text = ""

    # print(str(i))
    # print(plain[i]) 
    if i == len(plain) - 1:
        if len(text) < len(enc):
            text = text.ljust(len(enc), "z")

        # print(i)
        # print(text)
        plainList.append(text)        
        break
    
print(plainList)

for i, val1 in enumerate(plainList):
    sortedText = ""
    for j in range(0, len(val1)):
        sortedText += val1[enc[j] - 1]
    
    plainList[i] = sortedText
    # print(sortedText)

print(plainList)
print("".join(plainList))

cipherText = ""
cipherSplit = []
for i in range(len(plainList[0])):
    cipherText = ""   
    for val in plainList:
        cipherText += val[i]

    cipherSplit.append(cipherText)

print(cipherSplit)
print("".join(cipherSplit))
