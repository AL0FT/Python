# Don't understand why line 240 and line 254 represent dictionary key_string
#   differently, eg, [item] - 1 and [item - 1].


class Morbit:

    def __init__(self,key_word):
        """
        Intializes the instance using the keyword. The keyword's length
        must be NINE characters in accordance with the American Cryptogram
        Association guidelines for the Morbit Cipher. The keyword is stripped
        of non-alphabetic characters and whitespace, converted to UPPERCASE
        and converted to a list of integers.
        """
        # The 'morbit_list' contains (in order) the elements of the table to
        # encrypt text using the Morbit Cipher...
        self.morbit_list = ("..",".-",".X","-.","--",
                "-X","X.","X-","XX")

        # The 'morse_code' dictionary provides the International Morse Code
        #   equivalents for the letters A-Z, numerals 0-9, and punctuation
        #   for symbols '@'(commercial AT), '!'(exclamation mark),
        #   '?'(question mark), '='(equals sign), '+'(plus sign),
        #   '.'(period) and ','(comma).
        #
        # To reverse this dictionary, use:
        #ß
        #    morse_reversed = {value:key for key,value in morse_code.items()}
        self.morse_code = {'A': '.-',     'B': '-...',   'C': '-.-.',
                'D': '-..',    'E': '.',      'F': '..-.',
                'G': '--.',    'H': '....',   'I': '..',
                'J': '.---',   'K': '-.-',    'L': '.-..',
                'M': '--',     'N': '-.',     'O': '---',
                'P': '.--.',   'Q': '--.-',   'R': '.-.',
                'S': '...',    'T': '-',      'U': '..-',
                'V': '...-',   'W': '.--',    'X': '-..-',
                'Y': '-.--',   'Z': '--..',
                '0': '-----',  '1': '.----',  '2': '..---',
                '3': '...--',  '4': '....-',  '5': '.....',
                '6': '-....',  '7': '--...',  '8': '---..',
                '9': '----.',
                ' ': ' ','':'', '@': '.--.-.', '!':'-.-.--',
                '.':'.-.-.-', ',':'--..--', '?':'..--..',
                '+':'.-.-.', '=':'-...-','-':'-....-',':':'---...',
                "'":'.----.','"':'.-..-.','(':'-.--.-',
                '/':'-..-.'
                }


        # The 'morbit_table' maps the symbols used for a Morbit Cipher or a
        # Fractionated Morse Cipher to their respective positions, represented by
        # an integer. The character '.' represents a 'dit' (or dot), the '-'
        # represents a 'dah'(or dash) and the 'X' is the separator between
        # enciphered characters (with 'XX' being the separator between
        # enciphered words). It is a Python DICTIONARY.
        self.morbit_table = {1:"..",2:".-",3:".X",4:"-.",5:"--",
                6:"-X",7:"X.",8:"X-",9:"XX"}

        # The 'format_key()' function removes all non-alpha characters and
        #  spaces. The keyword is restricted to alphabetic characters only.
        #  It then converts the text to all UPPER CASE for consistency ...
        self.key_word = self._format_key(key_word)

        # After '_format_key()', which removes any non alphabetic characters,
        # the key_word is checked to ensure it is NINE letters long ...
        if len(self.key_word) != 9:
            print("checking for 9 characters ...")
            raise ValueError("Keyword must have NINE letters!")
        # Convert key_word to a list...
        self.key_word_list = list(self.key_word)
        #print("Key Word List From Class:",self.key_word_list)
        # Morbit Ciphers must have a NINE letter keyword, hence, 'columns'
        # always = NINE
        self.columns = 9
        # Convert the keyword list into a list of numbers using
        #  the 'key_transform' function. This is the 'encrypt_key', the
        #  ordering of the columns used to transpose plaintext ...
        self.encrypt_key = self._key_letter_to_number(self.key_word_list)
        self.encrypt_dct = self._zip_key_and_morbit_table(self.encrypt_key)
        # The 'decrypt_key' is the normal ordered sequence [0,1,2,...]
        #   transposed by the encryption key. For example, key_word 'YXWAZBRTL'
        #    gives the number list [7, 6, 5, 0, 8, 1, 3, 4, 2].
        #    The 'decrypt_key' would be [3, 5, 8, 6, 7, 2, 1, 0, 4] ...
        #self.pre_key = [x for x in range(len(self.encrypt_key))]
        #self.decrypt_key = self._transpose_columns(self.pre_key,
        #    self.encrypt_key)




        # The fractionated morse table is not used in this class.
        self.fractionated_morse_table = {1:"...",2:"..-",3:"..X",4:".-.",
                5:".--",6:".-x",7:".X.",8:".X-",9:".XX",
                10:"-..",11:"-.-",12:"-.X",13:"--.",15:"--X",16:"-X.",
                17:"-X-",18:"-XX",19:"X..",20:"X.-",21:"X.X",22:"X-.",
                23:"X--",24:"X-X",25:"XX.",26:"XX-"}

    def _key_letter_to_number(self,key_word_list):
        """
        Transforms each alphabetic key_word_list element into a  numeric
        equivalent for use in the transposition cycle. Returns this
        as a list.
        """
        # Standard English Alphabet used to 'check' each letter of keyword ...
        letters_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        i = 0 # Counter for numeric equivalent of each letter in keyword
        y = 0 # Counter for index of each item in key_word_list

        # Copy 'self.key_word_list' to 'encrypt_key'. This is the list that will
        #  be changed to the equivalent number list. Note that the syntax for
        #  this copy is 'encrypt_key = self.key_word_list[:]' ... this is to
        #  create an entirely new list object for 'encrypt_key'. Otherwise, ABCDEFGHIJKLMNOPQRSTUVWXYZ
        #  changes to 'encrypt_list' will also change the original
        #  'key_word_list'.
        #print("Before loop:",self.key_word_list)
        encrypt_key = self.key_word_list[:]
        # Check each letter in alphabet in turn ...
        for letter in letters_list:
            y = 0
            while y < self.columns: # ...against each item in encrypt_key
                # If, say, a encrypt_key item = "A" ...
                if encrypt_key[y] == letter:
                    # Change that item to a numeral, then increment ...
                    encrypt_key[y] = i
                    i += 1
                    y += 1
                else: # Letter not found? Move on to the next one
                    y += 1
                #print("inside loop:",self.key_word_list)
        #print("after loop:",self.key_word_list) ### for testing
        return encrypt_key # When all are checked/converted, return list

    def _format_key(self, input_text):
        """
        Formats input by removing all non-alphabetic characters and spaces
        and converting to UPPERCASE, then returns that string. For the Morbit
        Cipher, a NINE character keyword is required. An exception is thrown
        in the initializer if the keyword does not meet this criteria.
        """
        # Removes any characters that are not letters ...
        input_text = "".join([i for i in input_text.upper() if i.isalpha()])
        return input_text

    def _format_input(self, input_text):
        """
        Formats input by removing all characters except letters, numbers,
        spaces, and select symbols and punctuation, strips leading and trailing
        whitespace, converts to UPPERCASE, then returns that string.
        """
        #print("Initial input from class:",input_text)

        # Replaces the 'closing paranthesis' with an 'opening paranthesis',
        #  since the morse code for each is identical. Whether a paranthesis
        #  is an opening or closing one must then be inferred from context.
        para_text = input_text.replace(")", "(")
        # Removes any characters that are not letters, numbers, spaces
        #  or one of the standard punctuation or symbols. These symbols are:
        #  /[forward slash]     ![exclamation mark]
        #  "[double quotation]  .[period]
        #  '[apostrophe]        ,[comma]
        #  @['at' symbol]       :[colon]
        #  +[plus sign]         ?[question mark]
        #  =[equals sign]       -[dash or minus sign]
        alpha_input_text = "".join([x for x in para_text.upper() if
            x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ/ \"\'0@1!2.3,4:5?6+7=8-('])
        print("after removing illegal stuff:",alpha_input_text)
        # Remove all leading and trailing whitespace ...
        stripped_input_text = alpha_input_text.strip()
        #print("after removing lead/trail whitespace:",stripped_input_text)
        # Remove any double spaces ...
        double_spaces_removed_input_text = " ".join(stripped_input_text.split())
        #print("after removing double spaces:",double_spaces_removed_input_text)
        # Convert all to upper case for consistency ...
        formatted_input_text = double_spaces_removed_input_text.upper()
        #print("input text from class ...",self.input_text)
        return formatted_input_text

    def _transpose_columns(self, list_of_lists,encrypt_key):
        """
        Takes a 'grid' of letters represented by a 'list of lists' in
        which columns are represented by each individual list and rows by
        each successive element within the lists, and returns a grid in
        which the columns are transposed in order of the encrypt_key.
        """
        columns = self.columns
        #print("Encrypt Key: ",encrypt_key) ###
        # Create empty grid to hold transposition ...
        trans_grid = [[] for x in range(columns)]
        i = 0
        for number in encrypt_key: # Build the transposed grid
            trans_grid[number] = list_of_lists[i]
            i += 1
            #print("Building grid ...",trans_grid[number]) ###
        #print("Transposed Grid: ",trans_grid) ###
        return trans_grid # ... and return it.

    def _text_to_morse_list(self,input_text):
        """
        Takes an input string consisting of alphanumeric characters,
        including spaces, and converts it to a morse code equivalent.
        The characters '*' and '-' are used for the 'dit'(dot) and
        'dah'(dash), respectively.
        """
        # Create a list of morse code characters from the input_text, which
        #   has been formatted by '_format_input()'...
        input_list = list(self._format_input(input_text))
        index = 0
        # Create an empty list to hold the morse characters ...
        morse_output_list = []
        # Append each character to the list, using the 'morse_code'
        #   dictionary to translate from each character in the input_text to
        #   the appropriate morse code character.
        while index < len(input_list):
            morse_output_list.append(self.morse_code[input_list[index]])
            index += 1
        # Return the list of morse code characters. It should be a list of
        #   characters that directly correspond to the characters of the input
        #   text string (after formatting).
        return morse_output_list

    def _add_x_string(self,morse_output_list):
        """
        Adds the "X" characters to the 'morse_output_list' in accordance within
        the Morbit Cipher rules: An "X" is added between each character, and
        any spaces inside the list(i.e., not at the beginning or end) are
        replaced with "XX".
        """
        # Initialize the index at ONE. Since the original input was stripped
        # of leading spaces, the ZERO element cannot be a space ...
        index = 1
        while index < len(morse_output_list):
            # If the element is a space, skip over it without putting an "X"
            # before it or after it ...
            if morse_output_list[index] == " ":
                index += 1
            # ... otherwise, insert an "X", increment the index and continue ...
            if morse_output_list[index - 1] != " ":
                morse_output_list.insert(index,"X")
                index += 1
            index += 1
        # Replace the space character with "XX" ...
        morse_output_list = ["XX" if x==" " else x for x in morse_output_list]
        # Convert the list to a string ...
        self.add_x_string = ''.join(morse_output_list)
        #print("add_x_string:",add_x_string)
        # check to see if there are an even number of characters in the
        #  'add_x_string'; if not, add an "X"
        if len(self.add_x_string) % 2 != 0:
            #print("Odd number!", len(self.add_x_string))
            self.add_x_string = self.add_x_string + "X"
        return self.add_x_string

    def _zip_key_and_morbit_table(self,encrypt_key):
        #print("Encrypt Key:",self.encrypt_key)
        #print("Morbit Table:",self.morbit_table)
        encrypt_dct = dict(zip(self.encrypt_key,self.morbit_list))
        return encrypt_dct

    def _encrypt(self,plaintext):
        # 'encrypt_dct' must be reversed. This next line does that ...
        rev_encr_dict = {v:k for k,v in self.encrypt_dct.items()}
        #print("Reverse Enc Dict:",rev_encr_dict)
        # Initialize counter for building list of 2 elements per item ...
        i = 0
        ciphertext_list = [] # Initialize ciphertext list
        off_by_2s = [] # Initialize 'off by 2s' list
        # Build a list of elements by taking TWO characters at a time from
        #   'add_x_string'. This creates a list where each element
        #   is a KEY in the 'encr_dict' dictionary ...
        while i < len(self.add_x_string):
           off_by_2s.append(self.add_x_string[i] + self.add_x_string[i + 1])
           i += 2
        # Build a list of the VALUES of 'encr_dict' by using the KEYS in the
        #   'off_by_2s' list. Note that '1' must be added to each VALUE since
        #   the Morbit cipher uses the numerals 1-9, but because Python lists
        #   are ZERO-based, the list uses the numerals 0-8.
        for item in off_by_2s:
            ciphertext_list.append(rev_encr_dict[item] + 1)
        # Convert 'ciphertext_list' to a string ...
        self.ciphertext = ''.join(str(ltr) for ltr in ciphertext_list)

        return self.ciphertext

    def _decrypt(self,ciphertext):
        ciphertext_nospace = "".join([i for i in ciphertext if i.isdigit()])
        cipher_list = list(int(x) for x in ciphertext_nospace)
        #print("Cipher List:",cipher_list)
        xmorse_list = []
        plain_list = []
        morse_reversed = {value:key for key,value in self.morse_code.items()}
        #print("Morse Reversed:\n",morse_reversed,"\n")
        #print("Cipher List",cipher_list)
        #print("Encrypt dictionary:",self.encrypt_dct)
        for item in cipher_list:
            corrected_cipher_list = [item - 1 for item in cipher_list]
        for item in corrected_cipher_list:
            xmorse_list.append(self.encrypt_dct[item])
        #print("Corrected Cipher List:",corrected_cipher_list)
        #print("xmorse list:",xmorse_list)
        xmorse_string = ''.join(str(ltr) for ltr in xmorse_list)
        #print("xmorse_string:",xmorse_string)
        spaced_string = xmorse_string.replace("XX"," ")
        #print("Spaces for XX:",spaced_string)
        morse_list = xmorse_string.split('X')
        #print("morse list",morse_list)
        for item in morse_list:
            #print("Looking for:",item)
            try:
                plain_list.append(morse_reversed[item])
            except KeyError:
                plain_list.append("*")
        #print("Plain List:",plain_list)
        plain_list = [" " if x == "" else x for x in plain_list]

        self.plaintext = ''.join(str(ltr) for ltr in plain_list)
        #print("Plaintext:",self.plaintext)
        return self.plaintext




        return
