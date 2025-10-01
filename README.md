# 🔐 Vigenère Cipher in Python

This project demonstrates how to **encrypt and decrypt text** using the **Vigenère Cipher**, a classical encryption technique that uses a repeating key to shift characters in the alphabet. It also shows how to convert the project into a **simple interactive webpage using Streamlit**.

---

## 📖 About Vigenère Cipher
The Vigenère cipher is a method of encrypting alphabetic text using a series of Caesar ciphers based on a keyword.  
- Each letter in the plaintext is shifted by the alphabetical index of the corresponding letter in the key.  
- The key repeats if the message is longer than the key.  
- Non-alphabet characters (spaces, punctuation, numbers) remain unchanged.  

---

## 🚀 Features
- Encrypt and decrypt messages with a custom key.  
- Handles spaces and non-alphabetic characters without modification.  
- Case-insensitive (converts input internally to lowercase).  
- **Interactive Streamlit webpage**: input messages and keys via a web form, select cipher, and get instant results.

---

## 🛠️ How It Works
1. Enter a **message** and a **key**.  
2. Each letter of the key shifts the corresponding letter of the message.  
3. For decryption, the shift is reversed.  
4. Optional: Run the Streamlit app for a web-based interface.

---

## 📂 Project Structure
- `cipher.py` – Contains encryption and decryption functions.  
- `app.py` – Streamlit app for the interactive webpage.  
- `README.md` – Project documentation and instructions.  

---

## 🎯 Steps Followed
1. Learned the logic of Caesar and Vigenère ciphers.  
2. Planned user-friendly CLI interface.  
3. Implemented encryption and decryption functions in Python.  
4. Tested correctness using sample texts.  
5. Added Streamlit app for web interaction.  
6. Documented the project for easy understanding and usage.

---

## 💡 Outcome
This project provides a hands-on understanding of classical cryptography, Python programming practices, and building simple interactive web applications with Streamlit.
