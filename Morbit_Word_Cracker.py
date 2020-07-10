# Import the Columnar_Transposition class ...
from Morbit import Morbit
import sys
from itertools import permutations # needed for 'permutations' iterator
from math import factorial
import time     # needed for start/end time calculations.
from Dictionaries import English_FiftyK_words
from Morbit_English_Scorer import Morbit_English_Scorer
start = time.time()

# bigrams = ["th","he","in","er","an","re","on","at","en","nd","ti","es",
# "or","te","of","ed","is","it","al","ar","st","to","nt","ng","se","ha",
# "as","ou","io","le","ve","co","me","de","hi","ri","ro","ic","ne","ea",
# "ra","ce","li","ch","ll","be","ma","si","om","ur"]

# trigrams = ["the","and","ing","ion","tio","ent","ati","for","her","ter",
# "hat","tha","ere","ate","his","con","res","ver","all","ons","nce","men",
# "ith","ted","ers","pro","thi","wit","are","ess","not","ive","was","ect",
# "rea","com","eve","per","int","est","sta","cti","ica","ist","ear","ain",
# "one","our","iti","rat"]

# tetragrams = ["tion","atio","that","ther","with","ment","ions","this",
# "here","from","ould","ting","hich","whic","ctio","ence","have","othe",
# "ight","sion","ever","ical","they","inte","ough","ance","were","tive",
# "over","ding","pres","nter","comp","able","heir","thei","ally","ated",
# "ring","ture","cont","ents","cons","rati","thin","part","form","ning",
# "ecti","some"]

# pentagrams = ["ning","ecti","some","ation","tions","which","ction",
# "other","their","there","ition","ement","inter","ional","ratio",
# "would","tiona","these","state","natio","thing","under","ssion",
# "ectio","catio","latio","about","count","ments","rough","ative",
# "prese","feren","hough","ution","roduc","resen","thoug","press",
# "first","after","cause","where","tatio","could","efore","contr",
# "hould","shoul","tical","gener","esent","great"]

# common_words = {}

bigrams={"th":2.71,"he":2.33,"in":2.03,"er":1.78,"an":1.61,
"re":1.41,"on":1.32,"st":1.25,"nt":1.17,"en":1.13,"at":1.12,
"ed":1.08,"nd":1.07,"to":1.07,"or":1.06,"ea":1.00,"ti":0.99,
"ar":0.98,"te":0.98,"ng":0.89,"al":0.88,"it":0.88,"as":0.87,
"is":0.86,"ha":0.83,"et":0.76,"se":0.73,"ou":0.72,"of":0.71}

trigrams={"the":1.81,"and":0.73,"ing":0.72,"ent":0.42,"ion":0.42,
"her":0.26,"for":0.34,"tha":0.33,"nth":0.33,"int":0.32,"ere":0.31,
"tio":0.31,"ter":0.30,"est":0.28,"ers":0.28,"ati":0.26,"hat":0.26,
"ate":0.25,"all":0.25,"eth":0.24,"hes":0.24,"ver":0.24,"his":0.24,
"oft":0.22,"ith":0.21,"fth":0.21,"sth":0.21,"oth":0.21,"res":0.21,
"ont":0.20}

tetragrams={"tion":0.31,"othe":0.16,"them":0.12,"nthe":0.27,
"tthe":0.16,"rthe":0.12,"ther":0.24,"dthe":0.15,"thep":0.11,
"that":0.21,"ingt":0.15,"from":0.10,
"ofth":0.19,"ethe":0.15,"this":0.10,
"fthe":0.19,"sand":0.14,"ting":0.10,
"thes":0.18,"sthe":0.14,"thei":0.10,
"with":0.18,"here":0.13,"ngth":0.10,
"inth":0.17,"thec":0.13,"ions":0.10,
"atio":0.17,"ment":0.12,"andt":0.10}


pentagrams = {"ofthe":0.18,"andth":0.07,"ction":0.05,
"ation":0.17,"ndthe":0.07,"which":0.05,
"inthe":0.16,"onthe":0.07,"these":0.05,
"there":0.09,"edthe":0.06,"after":0.05,
"ingth":0.09,"their":0.06,"eofth":0.05,
"tothe":0.08,"tiona":0.06,"about":0.04,
"ngthe":0.08,"orthe":0.06,"erthe":0.04,
"other":0.07,"forth":0.06,"ional":0.04,
"atthe":0.07,"ingto":0.06,"first":0.04,
"tions":0.07,"theco":0.05,"would":0.04}

common_words = {"the":6.42,"on":0.78,"are":0.47,
"of":2.76,"with":0.75,"this":0.42,
"and":2.75,"he":0.75,
"to":2.67,"it":0.74,"but":0.40,
"as":0.71,"have":0.39,
"in":2.31,"at":0.58,"an":0.37,
"is":1.12,"his":0.55,"has":0.35,
"for":1.01,"by":0.51,"not":0.34,
"that":0.92,"be":0.48,"they":0.33,
"was":0.88,"from":0.47,"or":0.30}

hexagrams = ["ations","ration","tional","nation","ection","cation",
"lation","though","presen","tation","should","resent","genera","dition",
"ationa","produc","throug","hrough","etween","betwee","differ","icatio",
"people","iffere","fferen","struct","action","person","eneral","system",
"relati","ctions","ecause","becaus","before","ession","develo","evelop",
"uction","change","follow","positi","govern","sition","merica","direct",
"bility","effect","americ","public"]

heptagrams = ["present","ational","through","between","ication","differe",
"ifferen","general","because","develop","america","however","eration",
"nationa","conside","onsider","ference","positio","osition","ization"
,"fferent","without","ernment","vernmen","overnme","governm","ulation"
,"another","importa","interes","nterest","elation","rmation","mportan"
,"product","formati","communi","lations","ormatio","certain","increas"
,"relatio","special","process","against","problem","nstitut","politic",
"ination","univers"]

octograms = ["differen","national","consider","position","ifferent",
"governme","vernment","overnmen","interest","importan","ormation",
"formatio","relation","question","american","characte","haracter",
"articula","possible","children","elopment","velopmen","developm",
"evelopme","conditio","ondition","mportant","rticular","particul",
"epresent","represen","increase","individu","ndividua","dividual",
"elations","nformati","politica","olitical","universi","function",
"informat","niversit","iversity","lication","experien","structur",
"determin","ollowing","followin"]

enneagrams = ["different","governmen","overnment","formation","character",
"velopment","developme","evelopmen","condition","important","articular",
"particula","represent","individua","ndividual","relations","political",
"informati","nformatio","universit","following","experienc","stitution",
"xperience","education","roduction","niversity","therefore","nstitutio",
"ification","establish","understan","nderstand","difficult","structure",
"knowledge","struction","something","necessary","hemselves","themselve",
"plication","anization","according","differenc","operation","ifference",
"rganizati","organizat","ganizatio"]


print()

# ---------- SO 2018 E-6 ------------------------------------------------------
# cipher1 = "94276 54151 67547 97315 45716 23865 57831 36215 14751 13757 72159"
# cipher2 = "77582 24341 61245 85417 56971 28528 51227 51572 19577 2"
# cipher3 = ""

#cipher1 = "27435881512827465679378" # 'Once upon a time'

# ---------- MJ 2018 E-18 ------------------------------------------------------
cipher1 = "98991 65751 96274 14842 67991 62754 31844 18538 98391 79728 99311"
cipher2 = "46757 27341 48519 19119 65384 81919 88375 39165 69854 13587 53585"
cipher3 = "91627 94699 11419 11489 4"
ciphers = cipher1 + cipher2 + cipher3


# ---------- MA 2018 E-6 ------------------------------------------------------
# cipher1 = "38919 41513 97822 45419 37727 97669 45417 57169 98383 69797 85762"
# cipher2 = "89798 29744 77286 99762 86128 25776 31914 57317 94734 94364 31997"
# cipher3 = "12779 78349 76511"
# ciphers = cipher1 + cipher2 + cipher3
# -----------------------------------------------------------------------------
# ----------- JF 2018 E-7 [8,3,9,6,2,7,1,4,5] "Quip from a national ..." ------
# cipher1 = "52313 19365 86164 24717 49341 92761 73856 11218 12931 29939 19865"
# cipher2 = "37912 11615 36134 52765 78819 89117 39788 57271 89938 12942 41899"
# cipher3 = "39891 21896 25379 39941 89962"
# -----------------------------------------------------------------------
#----------- ND 2017 E-5 [2,7,1,3,4,6,5,9,8] "Clever remark from wag ..." -----
# cipher1 = "33531 12755 38711 45671 36571 71464 87679 38462 13356 71545 17292"
# cipher2 = "58291 56725 31967 99553 52846 23846 73513 51463 84626 71563 12755"
# cipher3 = "35256 71255 28753 58291 21791 1"
# ciphers = cipher1 + cipher2 + cipher3
# -----------------------------------------------------------------------
# #----------- SO 2017 ----------------------------------------------------
# cipher1 = "95627 43214 62516 72527 62145 17139 49327 54515 52415 48461 83686"
# cipher2 = "47962 14158 62557 49557 14144 66784 27797 87841 49326 97495 42525"
# cipher3 = "94751 59546 17939 14684 52972 6"
# #------------------------------------------------------------------------
# ---------- JA 2017 [5, 7, 3, 8, 2, 4, 0, 6, 1] "A man's library consists ..."
# cipher1 = "82315 91628 61496 19158 49329 97374 64616 71623 56928 19486 25661"
# cipher2 = "29673 73781 62661 26615 64716 48729 73764 35949 32858 74564 77329"
# cipher3 = "67319 19731 3"
# -----------------------------------------------------------------------
# #----------- MA 2014 ----------------------------------------------------
# cipher1 = "15521 65255 45636 52545 37387 22685 16464 54384 26515 45971 91794"
# cipher2 = "69872 26817 37153 84261 98722 68255 44939 54597 37272 55946 96287"
# cipher3 = "22684 46255 5255"
# ciphers = cipher1 + cipher2 + cipher3
# #------------------------------------------------------------------------
# -------Experiment with punctuation and numerals -----------------------
# cipher1 = "4251913585887425679916594191538594658919119653651285414323979375311"
# cipher2 = "48426298175553755565791485964232156491651489197845851217478929656541"
# cipher3 = "41827589335724964432158941135575785241485962113654465918775916523219"
# cipher4 = "8419345731988468531447927144692739564983997152"
# ciphers = cipher1 + cipher2 + cipher3 + cipher4
# -----------------------------------------------------------------------
#--------MJ 2017 --------------------------------------------------------
# cipher1 = "87763 46153 28713 26576 91169 16311 52597 97675 67375 96826 46769"
# cipher2 = "15138 77634 16887 65986 26797 61995 94564 61631 16461 66738 77631"
# cipher3 = "97676 68799"
# -----------------------------------------------------------------------
#-------- JF 2017 E-2 [6, 1, 3, 2, 5, 8, 4, 7, 9]------------------------
# cipher1 = "27596 32243 32713 34363 43578 68249 85874 63343 24133 22743 58295"
# cipher2 = "86291 27542 36743 22469 17323 74633 71358 13136 81274 35829 58629"
# cipher3 = "12754 54429 15926 42757 35818 63286 9"
# -----------------------------------------------------------------------
# --------Test with no spaces or punctuation ----------------------------
# cipher1 = "79911 75872 79437 84893 58938 84432 38989 19319"
# cipher2 = "18417 21519 18434 31988 54177 91387"
# cipher3 = "57991 85913 85315 14135 89758 89879 91391 89885 191"
# ciphers = cipher1 + cipher2 + cipher3
# -----------------------------------------------------------------------
#-------- MJ 2016 E-2 ---------------------------------------------------
# cipher1 = "64875 24227 52198 55139 91698 58769 85695 61396 37465 31739 85355"
# cipher2 = "73937 34856 52467 89627 21873 56729 79787 53913 98569 24818 13773"
# cipher3 = "14237 61431 42931 31957 29673 14"
# ciphers = cipher1 + cipher2 + cipher3
# -----------------------------------------------------------------------
#-------- Geocaching Cipher ---------------------------------------------
# cipher1 = "78589 64212 37756 11212 12796 97162 56392 58971 26952 43229 12153"
# cipher2 = "83617 29135 61298 12299 79773 43229 48118 37793 77921 15616 51521"
# cipher3 = "19618 32375 24229 37579 17574 69758 96517 19335 18361 32242 63821 92696 89773 88182 18719 71659"
# cipher4 = "13237  11989 92546 83283 68392 69269 77322 12217 21971 83757 91323 71166 64"
# ciphers = cipher1 + cipher2 + cipher3 + cipher4






# -----------------------------------------------------------------------

# ciphertext_grid = Columnar_Transposition("typ")
# encryptkey = ciphertext_grid.encrypt_key
# decryptkey = ciphertext_grid.decrypt_key
# ciphertext = ciphertext_grid._encrypt(ciphers)
ciphertext = ciphers
print("Ciphertext:",ciphertext)
# For breaking the cipher, the key must NOT have any repeated letters. Doing
#  so might cause the skipping of some permutations. For example, 'wisecrack'
#  has TWO occurrences of "c". For a Morbit Cipher, the keyword has 9 letters,
#  and ONLY 9 letters...
key = "fedcbahij"
ngrams = [bigrams]

score = 0
previous_score = 0
tries = 1
# There are 9! possible key combinations.
total_sols = factorial(9)
print("Total Solutions: ",total_sols)
def _check_for_ngram(ngram,text_to_check):
    occurrences = text_to_check.count(ngram)
    return occurrences
two = 2
# 'permutations' will produce ALL permutations of the keyword
perm = permutations(key)
for i in perm:
    # There are 9! possible key combinations. This calculates the progress as
    #  a percentage of the total.
    percent_done = (tries/total_sols) * 100.0
    key_string = "".join(i)
    finish = time.time()
    total = finish - start
    # 'divmod(x,y) returns a tuple of int(x/y) and remainder of x/y.
    m,s = divmod(total,60)
    h, m = divmod(m,60)
    # This next line produces a line that prints elapsed time, progress (as a
    #  percentage), and tries(as a fraction of total possible tries). The
    #  end="\r" and 'flush=True' arguments suppress the next-line character.
    #  This makes the line appear 'static' at the bottom of the terminal window.
    print("  Time: %d:%02d:%.2f" % (h, m, s),
        "Percent: {:0.2f}".format(percent_done),"Tries:",tries,
        "of",total_sols,
        end="\r",flush=True)
    tester = Morbit(key_string)
    plaintext = tester._decrypt(ciphertext)
    # The Morbit class inserts a '*' (asterisk) if a keyword produces an
    #  undefined solution. An illegal solution produces a 'KeyError', which is
    #  handled by inserting the asterisk character into the decrypted output.
    #  Therefore, if an '*' exists in the plaintext, the solution is NOT
    #  correct and may be skipped...
    if "*" in plaintext:
        tries += 1
        pass
    # Else, if the solution is a valid decrypt, its score is computed using ther
    #   Morbit_English_Scorer Class ...
    else:

        scorer = Morbit_English_Scorer(plaintext)
        score = scorer.score
        # If a decrypt scores equal to or greater than a previous solution,
        #   it is also scored and printed, updating the previous 'high score'...
        if score >= previous_score:
            wordlist = scorer.word_list
            print()
            print("Score:",score)
            print("Plaintext:",plaintext)
            enckey = tester.encrypt_key
            # The key returned from the Morbit Class is ZERO-based. For
            #  submissions to the ACA(American Cryptogram Association), a
            #  ONE-based key is created and printed...
            print_key = [(x + 1) for x in enckey]
            print("Key:",print_key)
            # A list of the actual 'found' words is generated by the
            #  Morbit_English_Scorer Class and printed ...
            print(len(wordlist),"Unique Words:\n",wordlist)
            # The 'previous_score' is updated with the new score...
            previous_score = score
            finish = time.time()
            total = finish - start
            # 'divmod(x,y) returns a tuple of int(x/y) and remainder of x/y.
            m,s = divmod(total,60)
            h, m = divmod(m,60)
            print()
            print("Try:",tries,"Reached at: %d hours %02d minutes %.2f seconds" % (h, m, s))
            print()
            tries += 1
print("----------------------------------------------------------------")

# Calculate the total time for run ...
finish = time.time()
total = finish - start
minutes,seconds = divmod(total,60)
hours, minutes = divmod(minutes,60)
print()
print("Total Time: %d hours %02d minutes %.2f seconds" % (hours, minutes, seconds),"Total Tries:",tries)
print("\a") # ... rings the 'bell' on most systems when finished
