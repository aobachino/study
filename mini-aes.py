# coding: utf-8
# Your code here!
# Nibble substitution table
nibble_sub_table = {
    0x0: 0x6, 0x1: 0x4, 0x2: 0xC, 0x3: 0x5,
    0x4: 0x0, 0x5: 0x7, 0x6: 0x2, 0x7: 0xE,
    0x8: 0x1, 0x9: 0xF, 0xA: 0x3, 0xB: 0xD,
    0xC: 0x8, 0xD: 0xA, 0xE: 0x9, 0xF: 0xB
}

def nibble_substitute(byte):
    return nibble_sub_table[byte]

def mini_aes_encrypt_block(block, key):
    if len(block) != 2 or len(key) != 2:
        raise ValueError("Block and key must be 2 bytes each.")

    state = bytearray(block)
    round_key = bytearray(key)

    # Round 0: Add round key
    for i in range(2):
        state[i] ^= round_key[i]

    # Round 1: Nibble substitution
    for i in range(2):
        state[i] = nibble_substitute(state[i])

    # Return the ciphertext block
    return bytes(state)

def mini_aes_encrypt(plaintext, key):
    print(len(key))
    if len(key) != 16:
        raise ValueError("Key must be 2 bytes.")

    ciphertext = bytearray()

    # Process plaintext in blocks of 16 bits (2 bytes)
    for i in range(0, len(plaintext), 2):
        block = plaintext[i:i+2]
        encrypted_block = mini_aes_encrypt_block(block, key)
        ciphertext.extend(encrypted_block)

    return bytes(ciphertext)

# Example usage
plaintext = b'ao'
key = b'1100011010100111'
print(plaintext)
print(key)

ciphertext = mini_aes_encrypt(plaintext, key)
print("Ciphertext:", ciphertext.hex())

