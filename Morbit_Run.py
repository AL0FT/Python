from Morbit import Morbit

cipher1 = "64875 24227 52198 55139 91698 58769 85695 61396 37465 31739 85355"
cipher2 = "73937 34856 52467 89627 21873 56729 79787 53913 98569 24818 13773"
cipher3 = "14237 61431 42931 31957 29673 14"
cipher = cipher1 + cipher2 + cipher3
tester = Morbit("interlock")
plaintext = tester._decrypt(cipher)
print("Plain:",plaintext)
