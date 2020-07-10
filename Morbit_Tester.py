# Must change _format_input to allow punctuation to pass through ...

# Morbit Tester
from Morbit import Morbit
print()
print("--------------------")
key = "wisecrack"
plain1 = "THEARTOFMEDICINE"
plain2 = "CONSISTSINAMUSINGTHE"
plain3 = "PATIENTWHILENATURECURESTHEDISEASE"

plain = plain1 + plain2 + plain3
print("Plaintext Input from tester:\n\n",plain)
print()
# A = 1   E = 5   i = 9
# B = 2   F = 6
# C = 3   G = 7
# D = 4   H = 8
morb = Morbit('interlock')
print("Key word after formatting:",morb.key_word)
morbkeylist = morb.key_word_list
print("Key Word List:",morbkeylist)
morbenckey = print("Encrypt Key:",morb.encrypt_key)
morbencdict = print("Encrypt Dictionary:",morb.encrypt_dct)
morb_input = print("formatted input:",morb._format_input(plain))

morbmorse = morb._text_to_morse_list(plain)
print("Text to Morse:\n",morbmorse)

xstring = print("With X's:",morb._add_x_string(morbmorse))
print("Now Decrypt .........................\n")
enc = morb._encrypt(plain)
print("Ciphertext:",enc)

dec = morb._decrypt(enc)
print("Back to plain:",dec)





print()
print("--------------------")
