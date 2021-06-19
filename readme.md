# Encryptor Decryptor Caesar Cipher
This project is built using python to encrypt and/or decyrpt English text and retreiving its key

## Program Design
![alt text](https://github.com/KhaledTaymour/Encryptor-Decryptor-Caesar-Cipher/blob/master/images/Program%20Design.png?raw=true)

## Code Design
![alt text](https://github.com/KhaledTaymour/Encryptor-Decryptor-Caesar-Cipher/blob/master/images/Code%20Design.png?raw=true)

## Encrypt & Decrypt Workflows
1. Loop thru the text
2. Keep the info about is it capitalized or not
3. Check if this character is a letter
    * If No -> return the character as it is
    * If Yes Continue
4. Shift the letter by the value of the input key
5. Apply if capitalized

## Brute Force Workflow
* Decrypt using keys from 0 to 26
    * In each one: calculate the frequency for each letter, and the Correlation Coefficient.
    * Save the Correlation Coefficient for each key
* Choose the best Correlation Coefficient from the keys

## How To use?
### In caesar cipher.ipynb:
Import helper class:
```python
from helper import Helper
```

e.g.: `textToEncrypt = 'The duke spent 16 years modifying this particular model'`

Call the encrypt function:
e.g.: 
```python
helper.encrypt(textToEncrypt, 5)
```

Call the decrypt function:
e.g.: 
```python
helper.decrypt(textToEncrypt, 5)
```

Call the bruteForceCipher function:
e.g.: 
```python
helper.bruteForceCipher('Ymj izpj xujsy 16 djfwx rtinkdnsl ymnx ufwynhzqfw rtijq')
```


