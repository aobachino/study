# coding: utf-8
# Your code here!

def calcShift(num):
    
    if num >= 26:
        num = num % 26 
    
    return num


plain = "tepungpelita"
crypt = ""

key = 10
alphabet = "abcdefghijklmnopqrstuvwxyz"

for x in range(0, len(plain)):
   crypt += alphabet[calcShift(alphabet.find(plain[x]) + int(key))]

print (plain)

print (crypt)