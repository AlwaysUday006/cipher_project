# Vigenère Cipher in Python

This project demonstrates how to **encrypt and decrypt text** using the **Vigenère Cipher**, a classical encryption technique that uses a repeating key to shift characters in the alphabet.

---

## 📖 About Vigenère Cipher
The Vigenère cipher is a method of encrypting alphabetic text by using a series of Caesar ciphers based on the letters of a keyword.  
- Each letter in the plaintext is shifted by the alphabetical index of the corresponding letter in the key.  
- The key repeats when the message is longer than the key.  
- Non-alphabet characters (spaces, punctuation, numbers) remain unchanged.

---

## 🚀 Features
- Encrypts a message with a custom key.
- Decrypts the encrypted message back to the original.
- Handles spaces and non-alphabetic characters without modification.
- Case-insensitive (works on lowercase internally).

---

## 🛠️ How It Works
1. Choose a **message** and a **key**.
2. Each letter of the key decides how many positions to shift the message’s letters.
3. For decryption, the same process is reversed.

---

## 📂 Project Structure
