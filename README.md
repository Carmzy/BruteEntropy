# BruteEntropy
A password bruteforce attack by comparing probability distributions. Note that the output of this program will primarily depend on the wordlist/s fed into it.

## Author
- Carman Zyre A. Bautista

## Dependencies
If possible that you don't have any of these common libraries, then install them. This relies on accurate calculations that is why we need decimal to control floating point numbers and integers...

**Itertools**
- ```pip install itertools```

**decimal**
- ```pip install decimal```

**math**
- ```pip install math```

**hashlib**
- ```pip install hashlib```

## Sources
Use datasets available online and try to merge them to a single text where this program will loop into. The most accessible one is located in your own local computer (***C:\Users\USER_NAME\AppData\Local\Google\Chrome\User Data\ZxcvbnData***). I don't know why Google Chrome has it's own password lists but you can play with it. You can also use other websites such as:

---
> "The entire set of passwords is downloadable for free below with each password being represented as either a SHA-1 or an NTLM hash to protect the original value (some passwords contain personally identifiable information) followed by a count of how many times that password had been seen in the source data breaches."

— https://haveibeenpwned.com/Passwords

---
> "The Passwords directory will hold a number of password lists that can be used by multiple tools when attempting to guess credentials for a given targeted service. This will include a number of very popular lists in cooperation with their maintainers, including the RockYou lists maintained by Rob Bowes."

— https://github.com/danielmiessler/SecLists/tree/master/Passwords

And possibly...

---
> "RockYou2021.txt is a MASSIVE WORDLIST compiled of various other wordlists. RockYou2021.txt DOES NOT CONTAIN USER:PASS logins!"

— https://github.com/ohmybahgosh/RockYou2021.txt

## Usage
Very simple, input all the required parameters for testing. Currently, this open-source project is in development. The inputs given are as follows:
- True total number of characters the password have.
- initial characters of the true password.
- Wordlist full file path.
- One-way SHA-1 of the true password.

***Note: You can test this to any passwords. Use with caution***
