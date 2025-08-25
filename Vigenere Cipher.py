keyAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = "abcdefghijklmnopqrstuvwxyz"

def calcShift(num):
    
    if num >= 26:
        num = num % 26 
    return num

def enc(plain ,keyStr, mode):

    text = ""

    if mode == "e":

        for x in range(0, len(plain)):
             keyCounter = x
             if keyCounter > (len(keyStr) -1) :
                keyCounter = x % len(keyStr)
             
             keyChar = keyStr[keyCounter]
             key = keyAlphabet.find(keyChar)
             print("plainIndex :" + str(x))
             print("plainChar : " + plain[x])
             print("keyIndex : " + str(key))
             print("keyChar : " + keyChar)
             
    
             text += alphabet[calcShift(alphabet.find(plain[x]) + int(key))]

    elif mode == "d":

        for x in range(0, len(plain)):
            keyCounter = x
            if keyCounter > (len(keyStr) -1) :
                keyCounter = x % len(keyStr)
            
            keyChar = keyStr[keyCounter]
            key = keyAlphabet.find(keyChar)
            # print("CipherText:" + plain[x])
            #print("C's value :" + str(alphabet.find(plain[x])))
            # print("Key Stream: " + str(key))

            if alphabet.find(plain[x]) >= int(key):
                # print("P's value: " + str(alphabet.find(plain[x]) - int(key)))
                # print("Plaintext: " + alphabet[alphabet.find(plain[x]) - int(key)])
                text += alphabet[alphabet.find(plain[x]) - int(key)]
            else:
                # print("P's value: " + str((alphabet.find(plain[x]) - int(key)) + 26)) 
                # print("Plaintext: " + alphabet[(alphabet.find(plain[x]) - int(key)) + 26])
                text += alphabet[(alphabet.find(plain[x]) - int(key)) + 26]

    return text


text = "HHWKSWXSLGNTCG".lower()
key = "PASCAL"
mode = "d"

print(enc(text,key,mode))