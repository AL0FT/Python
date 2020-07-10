
# Import the Columnar_Transposition class ...
from Columnar_Transposition import Columnar_Transposition
from itertools import permutations # needed for 'permutations' iterator
import time     # needed for start/end time calculations.

# Establish a start time to measure how long to completion ...   
start = time.time()


## JF 2018 E-24 ----------------------------------------------------------
# cipher1 = "AHRNL INDOT SDINS USMEH EATAF AHEIY SAAOC ATNOS ENPTN RHGRL AIRCI"
# cipher2 = "CATTO ETVLO WPCNA HOSBH ORNAE PNOPH SRULP AAALG NMEIL KORNR OXARC"
# cipher3 = "INCNE OCIHT SRTRE TFRAY OCTHS RDCLT AEPTS TCEOU MRSEA IESOB TIOAA"
# cipher4 = "CCSOA LGAUA EDASS MHESR ECONG SRLNS HSFTM LSIDT YELIS SELNY EDTTO"
# cipher5 = "ERINI NSTCA B"

cipher1 = "AHRNL INDOT SDINS USMEH EATAF AHEIY SAAOC ATNOS ENPTN RHGRL AIRCI"
cipher2 = "CATTO ETVLO WPCNA HOSBH ORNAE PNOPH SRULP AAALG NMEIL KORNR OXARC"
cipher3 = "INCNE OCIHT SRTRE TFRAY OCTHS RDCLT AEPTS TCEOU MRSEA IESOB TIOAA"
cipher4 = "CCSOA LGAUA EDASS MHESR ECONG SRLNS HSFTM LSIDT YELIS SELNY EDTTO"
cipher5 = "ERINI NSTCA B"
# ciphers = cipher1 + cipher2 + cipher3 + cipher4 + cipher5

ciphertext = cipher1 + cipher2 + cipher3 + cipher4 + cipher5
##-------------------------------------------------------------------------
# Comment out the lines from the 'plain = now ...' to 'crib2 = "NAVY" ...'
#  ... then uncomment the lines starting with 'cipher1 = ONGD ...' and 
#  ending with 'crib2 = "racing". Note that you if your ciphertext is long,
#  you can break it into 2 or more strings, then add those strings, as I do
#  here with 'ciphertext = ciphertext1 + ciphertext2'. To search for a 
#  single word, simply put a single letter in crib2 that occurs in crib1,
#  for example 'crib2 = "v" ' or any letter that is in the plaintext.
#  You may also search for more than 2 cribs by adding 'crib3', etc, but
#  remember to add this to 'cribs = [crib1,crib2]'.
### ------------ Begin Commenting Out ... -------------------------------
# plain = "nowisthetimeforallgoodmentocometotheaidoftheircountryandtheirnavy"
pregrid = Columnar_Transposition("cryptog")
# plain = pregrid._format_input(plain)
# print("\nPlain Text: ",plain)
# ciphertext = pregrid._encrypt(plain)
# print("\nCipher text: ",ciphertext,"\n")
replain = pregrid._decrypt(ciphertext)
# print("Back to plaintext ...",replain)
crib1 = "manhatten"
crib2 = ""
### --------------End Commenting Out ------------------------------------
### --------------Begin Uncommenting ... --------------------------------
# cipher1 = "ONGDRONGEAIDLUOMRACDCTTRLHIDSNLCPSWTWOTAPCIDUAREOESSEYS"
# cipher2 = "TRIAAIRMNHETITEOVERECUERIHOLGSDPWFONOOFAIHCHEUED"
# ciphertext = cipher1 + cipher2
# print("\nCipher text: ",ciphertext,"\n")

###---------------End Uncommenting----------------------------------------

crib1 = crib1.upper()
crib2 = crib2.upper()

cribs = [crib1,crib2]


# Various keyword lengths. More may be added if necessary ...
key3 = "abc"
key4 = "abcd"
key5 = "abcde"
key6 = "abcdef"
key7 = "abcdefg"
key8 = "abcdefgh"
key9 = "abcdefghi"
key10 ="abcdefghij"
key11 ="abcdefghijkl"
key12 ="abcdefghijklm"
key13 ="abcdefghijklmn"
key14 ="abcdefghijklmno"
key15 ="abcdefghijkmlnop"

#keys = (key4,key5,key6,key7,key8,,key9,key10,key11,key12,key13,key14,key15)
# Which keywords to include. Up to a nine-character keyword can usually
#   be completed in less than one minute, but a 10 character might take
#   up to 10 minutes, increasing greatly with longer keywords...
keys = [key9]

count = 0
tries = 0
for key in keys:
    perm = permutations(key)
    for i in perm:
        key_string = "".join(i)
        # print("Trying: ",key_string) ###
        # print("Key String:",key_string,"Length:",len(key_string))###
        test_grid = Columnar_Transposition(key_string)
        plaintext = test_grid._decrypt(ciphertext)
        tries += 1
        #print(plaintext) ###
        if all(crib in plaintext for crib in cribs):
            print("Looking for substring ",cribs)
            count += 1
            decrypt_key = [(x + 1) for x in test_grid.decrypt_key]
            encrypt_key = [(x + 1) for x in test_grid.encrypt_key]
            print("-------------------------------------------------")
            print("Solution: ",count,"\n\nDecrypt Key: ",decrypt_key,
            "\nOriginal Key: ",encrypt_key)
            print(plaintext,"\n\n") # Prints 2 'new lines' for separation.
            print("... Plaintext in by rows, Ciphertext out by columns\n")
            print("-------------------------------------------------")
print("\nCiphertext Length:",len(plaintext),"\n")
if count == 0:
        print("\nTried ",tries,"times,","'",cribs,"'"," not found!")
print("Tries ... ",tries)  

# Calculate the total time to run ...  
finish = time.time()
total = finish - start
print("\nTotal Time: {:0.2f} seconds".format(total))
print("\a") # ... rings the 'bell' on most systems when finished

## -------------- EXAMPLES -------------------------------------------

## JF 2017 E-12 ----------------------------------------------
# cipher1 = "ONGDRONGEAIDLUOMRACDCTTRLHIDSNLCPSWTWOTAPCIDUAREOESSEYS"
# cipher2 = "TRIAAIRMNHETITEOVERECUERIHOLGSDPWFONOOFAIHCHEUED"
# ciphertext = cipher1 + cipher2
# crib1 = "formula"
# crib2 = "racing"
##-------------------------------------------------------------
##-------SO 2017 E-1 ------------------------------------------------------
# cipher1 = "ULMDNQYDAEEYGIFIIOOANEDOCAEUMCTSLIRTIONIHSRYMT"
# cipher2 = "GUIINHDMTQASTUNLGNTNAKCEOIOEIYTESMRDNN"
# ciphertext = cipher1 + cipher2
# crib1 = "QU"
# crib2 = "family"
##-----------------------------------------------
## SO 2017 E-7 -----clue: 'Everyday problems ------------------------------
# cipher1 = "SOETT GTCPI YANTT FTGIT KIAEM OEUHL EASIO"
# cipher2 = "DOENS YEVDC AEMTT IADAA HSHOR DONDH HA"
# ciphertext = cipher1 + cipher2
# crib1 = "provide"
# crib2 = "e"
##-------------------------------------------------------
## ND 2017 --------------------------------------------------
# cipher1 = "TTTIEFAEESLNNSTNCNVIHSSHIESSIAKIEMOAIOYNSFKYOSCHODIOFRA"
# cipher2 = "BUIIIREEOUATTAFTRIBEDHTLOINLTUGNGLTPOENOTFENDYSTEILEGKH"
# cipher3 = "LKDEHAAGAOTYNNISIYEISCRWALDLWUAOIGNSNUHKULSGNITTKNNRFRT"
# cipher4 = "HOZLHC"
# ciphertext = cipher1 + cipher2 + cipher3 + cipher4
# crib1 = "cloudcover"
# crib2 = "sun"
##------------------------------------------------------------
## ND 2017 E-15 ----------------------------------------------
# cipher1 = "VPSEASPFBRTROOOEOEWEOERCSSSHEEWYBULAMROAUEYMBDAIIDOIIDL"
# cipher2 ="LVSESUSLFAEDEYCLLYD"
# ciphertext = cipher1 + cipher2
# crib1 = "ould"
# crib2 = "proble"
##-------------------------------------------------------------
## JF2018 E-1 ----------------------------------------------------
# cipher1 = "HMTEV IDSNN BIAOA OEOGR GWTMN KPOEG UASGT HNNSI NETIO ILIS"
# cipher2 = ""
# ciphertext = cipher1 + cipher2
# crib1 = "the"
# crib2 = "washingtonmonument"
##------------------------------------------------------------------------
