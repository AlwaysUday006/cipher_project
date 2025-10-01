import streamlit as st

# --- Your Cipher Code ---
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def vigenere(message, key, direction=1):
    key_index = 0
    final_message = ''
    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

# --- Streamlit UI ---
st.title("🔐 Vigenère Cipher Tool")
st.write("Encrypt or decrypt text using the Vigenère cipher")

text = st.text_area("Enter your text:")
key = st.text_input("Enter your key (letters only):", value="happycoding")
mode = st.radio("Choose mode:", ["Encrypt", "Decrypt"])

if st.button("Run Cipher"):
    if mode == "Encrypt":
        result = encrypt(text, key)
    else:
        result = decrypt(text, key)
    st.success(f"**Result:** {result}")
