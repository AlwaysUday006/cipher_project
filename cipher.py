# Input text to be decrypted (already encrypted using Vigenère cipher)
text = 'mrttaqrhknsw ih puggrur'

# Custom key used for encryption and decryption
custom_key = 'happycoding'


# Function that performs the core Vigenère cipher (both encryption & decryption)
def vigenere(message, key, direction=1):
    # Keeps track of which character of the key we are using
    key_index = 0
    # Alphabet used for substitution
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Final result (encrypted or decrypted message)
    final_message = ''

    # Go through every character in the given message
    for char in message.lower():

        # If the character is NOT a letter (like space, punctuation, numbers),
        # keep it unchanged and add directly to the result
        if not char.isalpha():
            final_message += char
        else:        
            # Pick the current character from the key (repeats when needed)
            key_char = key[key_index % len(key)]
            key_index += 1  # move to next key character for next round

            # Find how much to shift (offset) using the key character
            offset = alphabet.index(key_char)  # index of key_char in alphabet
            index = alphabet.find(char)        # index of message char in alphabet

            # For encryption, add offset; for decryption, subtract offset
            new_index = (index + offset * direction) % len(alphabet)

            # Add the resulting encrypted/decrypted character to final_message
            final_message += alphabet[new_index]
    
    # Return the completed message after applying the cipher
    return final_message


# Function for encryption (default direction = +1)
def encrypt(message, key):
    return vigenere(message, key)
    
# Function for decryption (direction = -1)
def decrypt(message, key):
    return vigenere(message, key, -1)


# --- Program execution starts here ---

# Display the encrypted text and key
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')

# Decrypt the message using the Vigenère cipher
decryption = decrypt(text, custom_key)

# Show the final decrypted message
print(f'\nDecrypted text: {decryption}\n')
