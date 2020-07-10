class Columnar_Transposition:
 
    """
    Encrypts or decrypts an alphabetic text using the Columnar  
    transposition method. Current usage limited to the English alphabet.
    Plaintext is assumed to be entered by ROWS and, after transposition, 
    extracted by COLUMNS in accordance with the standards of the American
    Cryptogram Association.
    
    Works for both COMPLETE columnar transpostion and
    INCOMPLETE columnar transposition ciphers.
    
    Example of use:
        
        columnar_trans = Columnar_Transposition("crypto")
           Creates instance with keys:
                Encryption Key:  [0, 3, 5, 2, 4, 1]
                Decryption Key:  [0, 5, 3, 1, 4, 2]
           Note that the numerical key lists begin at ZERO.

        columnar_trans._encrypt("Now is the time for all good men")
           Produces ciphertext: NHFGNTELEIIADOEOOSMLMWTRO
           
        columnar_trans._decrypt("NHFGNTELEIIADOEOOSMLMWTRO")
           Produces plaintext: NOWISTHETIMEFORALLGOODMEN
        
        Methods preceded by an underscore(_) are class specific. Methods
        without an underscore are regular Python methods.
        
        Various class methods are used to ...
        
        * _format_input(text): Remove non-alphabetic characters and  
            spaces, and convert the given text to UPPERCASE. In the case of
            the KEYWORD, this allows it to be compared to a standard 
            alphabet of UPPERCASE letters.
            
        * len(self.key_word): Determine the number of columns. This is the
          standard list method of a string object.
        
        * list(key_word): Convert key_word into a list called 
          'key_word_list'. This is the standard list method of a string
          object which converts the string to a list of individual letters.
        
        * _key_letter_to_number((key_word_list): Convert key_word_list into 
            a list of numbers called 'encrypt_key'. This numberical list 
            will be used to determine the transposition order of the 
            columns.
     
    """

    def __init__(self,key_word):
        """
        Intializes the instance using the keyword. The keyword's length 
        determines the number of columns in the matrix to be transposed. 
        For a Complete Columnar Transposition, each column will have an 
        equal number of elements. If the number of columns (as determined
        by the number of letters in the keyword) does NOT evenly divide the
        plaintext or ciphertext, an INCOMPLETE Columnar Cipher will be the
        result. 
        """
        
        # The 'format_input' function removes all non-alpha characters and 
        #  spaces. It then converts the text to all UPPER CASE
        #  for consistency ...
        self.key_word = self._format_input(key_word)
        # Determine number of columns (= number of letters in keyword) ...
        self.columns = len(self.key_word)
        # Convert key_word to a list...
        self.key_word_list = list(self.key_word) 
        # Convert the keyword list into a list of numbers using 
        #  the 'key_transform' function. This is the 'encrypt_key', the
        #  ordering of the columns used to transpose plaintext ...
        self.encrypt_key = self._key_letter_to_number(self.key_word_list)
        # The 'decrypt_key' is the normal ordered sequence [0,1,2,...]
        #   transposed by the encryption key. For
        #   example, key_word 'YXWAZB' gives the number list [4,3,2,0,5,1]. 
        #   The 'decrypt_key' for this would be the list [3,5,2,1,0,4] ...
        self.pre_key = [x for x in range(len(self.encrypt_key))]
        self.decrypt_key = self._transpose_columns(self.pre_key,
            self.encrypt_key)
        
        
        
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
        # Check each letter in alphabet in turn ...
        for letter in letters_list: 
            y = 0
            while y < self.columns: # ...against each item in key_word_list
                # If, say, a key_word_list item = "A" ...
                if key_word_list[y] == letter: 
                    # Change that item to a numeral, then increment ... 
                    key_word_list[y] = i 
                    i += 1
                    y += 1
                else: # Letter not found? Move on to the next one
                    y += 1
        ###print("Key: ",key_word_list) ### for testing
        return key_word_list # When all are checked/converted, return list
            
    def _format_input(self, input_text):
        """
        Formats input by removing all non-alphabetic characters and spaces
        and converting to UPPERCASE, then returns that string.
        """
        # Removes non-alpha,spaces, makes UPPERCASE. Note that this is
        #   a 'continued line' (the entire equation could be written on 
        #   a single line but would exceed my self-imposed 80 character 
        #   per line limit ...
        input_text = "".join([i for i in 
            input_text.upper() if i.isalpha()]) 
        return input_text
        
    def _in_by_rows(self, text):
        """
        Returns a 'list of lists', a grid of the plain_text written in by 
        rows. In 'grid', each column is represented by each list in the
        list_of_lists, and each row by elements of each list with the same
        index.
        """
        columns = self.columns
        # Determine the number of 'extra' characters if this is an 
        #   INCOMPLETE Columnar Transposition. If the result of this 
        #   operation is ZERO, no 'extra' characters are present and the
        #   result is a COMPLETE Columnar Transposition...
        self.extras = len(text)%self.columns
        #print("Length: ",len(text)) ###
        #print("Extras: ",self.extras) ###
        index = 0
        column = 0
        initial_length = len(text) - self.extras
        # Initialize an empty list of lists to hold the text. 
        grid =[[] for x in range(columns)]
        # Place the text into the 'grid' by adding one number to each list,
        #   then the second letter to each list, and so on. Continue until
        #   until the entire text minus the 'extras' is in the grid ...
        while index < initial_length:
            while column < columns:
                grid[column].append(text[index])
                index += 1
                column += 1
            column = 0 
        # If there are 'extras', this will simply add them to the bottom
        #   row of the grid. The bottom row will not have the same number
        #   of characters as the previous rows (e.g., not every list will
        #   have the same number of elements. If there are no 'extras', 
        #   this loop will not run...
        if self.extras > 0:
            while index < len(text):
                grid[column].append(text[index])
                index += 1
                column += 1
          
        ###print("In by Rows Grid: ",grid) ###
        return grid    
     
    def _out_by_rows(self, list_of_lists):
        """
        Returns a string of letters 'read out' from a list of lists. The 
        letters are read out by rows. In the list of lists, rows are 
        represented by all items in each list with the same index.
        """
        columns = self.columns
        # print("What OutByRows is getting: \n", list_of_lists) ###
        # print("Columns: ",columns) ###
        # Initialize an empty list to hold each character ...
        cipher_text_list = []
        row = 0
        column = 0
        index = 0
        # print("Length: ",len(self.text)) ###
        while index < len(self.text):
            while column < columns and index < len(self.text):
                cipher_text_list.append(list_of_lists[column][row])
                column += 1
                # print("Index:",index) ###
                # print("CipherTextList: ",cipher_text_list) ###
                # print("Row: ",row,"Column: ",column) ###
                index += 1
            row += 1  
            column = 0
        # Join each character in the list together into a string ...
        text = "".join(str(x) for x in cipher_text_list)
        return text
    
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
        
    def _out_by_columns(self, list_of_lists):
        """
        Returns a string of letters 'read out' from a list of lists.
        The letters are read out by columns. In the list of lists,
        each column is represented by each one of the individual lists. 
        The resulting string is just the letters of each list in turn 
        concantenated into one larger string.
        """
   
        # Initialize one large list to hold all the letters ...
        text_list = []
        for each_list in list_of_lists:
            for element in each_list:
                text_list.append(element)
        # Take the list of letters and 'join' them into one string...        
        text = "".join(str(x) for x in text_list)
        return text 
        
    def _in_by_columns(self, text):
        """
        Returns a 'list of lists', a grid of the text written in by
        columns. In 'grid', each column is represented by each list in the
        list_of_lists, and each row by elements of each list with the same
        index.
        """
        columns = self.columns
        self.text = text
        # Determine the number of 'extra' characters if this is an 
        #   INCOMPLETE Columnar Transposition. If the result of this 
        #   operation is ZERO, no 'extra' characters are present and the
        #   result is a COMPLETE Columnar Transposition...
        self.extras = len(text)%self.columns
        # Determine the number of 'whole' rows, i.e., the number of rows
        #   that are not 'missing' a letter...
        whole_rows = int(len(self.text)/columns)
        # print("Whole Rows: ",whole_rows) ###
        index = 0
        column = 0
        row = 0
        # Intialize an empty list of lists to hold the characters ...
        grid =[[] for x in range(columns)]
        # print("In by Columns Grid: ",grid) ###
        # Enter the characters into each 'column', i.e., each list in the
        #   list of lists. Using the decryption key allows this loop to 
        #   determine which lists are 'complete' and build them first ...
        for digit in self.decrypt_key:
            row = 0 
            while row < whole_rows:
                # print("Row: ",row) ###
                # print("Column: ",digit) ###
                # print("Index: ",index) ###
                grid[digit].append(self.text[index])
                # print("Grid[",digit,"]",grid[digit]) ###
                index += 1
                row += 1
                #print("Grid: ",grid) ###  
            # If there are 'extras', these lists are built last and contain
            #   one fewer character than the 'whole' lists built above...
            if digit < self.extras:
                # print("In the extra loop...") ###
                # print("Row Now: ",row) ###
                # print("Column Now: ",digit) ###
                # print("Index Now: ",index) ###
                grid[digit].append(self.text[index])
                # print("Grid[",digit,"]",grid[digit]) ###
                index += 1
               
                    
        #print("Grid: ",grid) ###    
        return grid   

    def _encrypt(self, plaintext):
        
        # Remove all non-alphabetic characters and whitespace from the
        #  entered plaintext (e.g., "This is the message" would be
        #  transformed to "THISISTHEMESSAGE".
        plaintext = self._format_input(plaintext)
        # Put the plaintext into the grid, entering it row by row using 
        #   the 'self._in_by_rows' function above ...
        into_grid = self._in_by_rows(plaintext)
        # Transpose the columns in accordance with the keyword using the 
        #   'self._transpose_columns' function above ...
        transposed = self._transpose_columns(into_grid,self.encrypt_key)
        # Take the ciphertext out of the grid, column by column using the 
        #   'self._out_by_columns' function above ...
        ciphertext = self._out_by_columns(transposed)
        
        return ciphertext
        
    
    
    
    def _decrypt(self,ciphertext):
    
        # Remove all non-alphabetic characters and whitespace from the
        #  entered ciphertext (e.g., "ABCDE xyjqu UHHO" would be
        #  transformed to "ABCDEXYJQUUHHO"...
        ciphertext = self._format_input(ciphertext)
        # Put the ciphertext into the grid, column by column. The function
        #   'in_by_columns' determines which columns have an extra 
        #   character (if applicable) using the keyword
        into_grid = self._in_by_columns(ciphertext)
        #print("Grid to be decrypted: ",into_grid) ###
        # Read the plaintext out of the grid row by row ...
        plaintext = self._out_by_rows(into_grid)
        return plaintext