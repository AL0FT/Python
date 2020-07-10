# Tries all 26 combinations for brute-force Caesar Cipher cryptanalysis

class CaesarCipher:
    """
    Encrypts or Decrypts input text using a Caesar Cipher, i.e., by shifting
    the alphabet by a specified number of places. Argument to constructor
    must be an integer. Currently limited to English alphabet only.
    
    Example Usage:
    
    >>> caesar_cipher = CaesarCipher(3)
    >>> cipher_text = caesar_cipher.encrypt('abcdefg')
    >>> cipher_text
    'DEFGHIJ'
    >>> plain_text = caesar_cipher.decrypt('DEFGHIJ')
    >>> plain_text
    'abcdefg'
    >>> cipher_text = caesar_cipher.encrypt_raw("Whether you say, 'I can' or 'I cannot', you're right!")
    >>> cipher_text
    Zkhwkhu brx vdb, 'L fdq' ru 'L fdqqrw', brx'uh uljkw!
    plain_text = caesar_cipher.decrypt("Zkhwkhu brx vdb, 'L fdq' ru 'L fdqqrw', brx'uh uljkw!")
    >>> plain_text
    Whether you say, 'I can' or 'I cannot', you're right!
    """
    def __init__(self,text_shift = 0):
        """Creates the object with a specified shift; Default = 0. Must be an
        integer argument."""
        try:
            self.text_shift = int(text_shift % 26)
        except TypeError:
            print("Argument to create CaesarCipher Object must be an integer!")
    def encrypt(self,input_text):
        """ Encrypts the input text after removing ALL non alphabetic
        characters (including punctuation and spaces) and returns an 
        unformatted string in UPPER case.
        """
        self.input_text = "".join([i for i in input_text if i.isalpha()]) # Removes any non-alpha character
        text_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
                     "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] # Initialize the list with shift = 0.
        slice_out = text_list [(self.text_shift):] # Slice out 'shift' characters from end ...
        whats_left = text_list[:(self.text_shift)] # ... and save what's left.
        for item in reversed(slice_out): # Starting with last sliced out item(hence, 'reversed()') ...
            whats_left.insert(0,item) # ... insert them at the beginning of the list.
        keyed_dictionary = dict(zip(text_list,whats_left)) # Create Key Dictionary from list {plaintext:ciphertext}
        output_list = [] # Initialize empty list to store ciphertext.
        for character in self.input_text.upper(): # for each item in plaintext list (converted to UPPER) ...
            output_list.append(keyed_dictionary[character]) # ...append its ciphertext item(from 'keyed_dictionary') to list.
        output_text = "".join(output_list) # Convert ciphertext list back to string. . .
        return output_text # ... and return it.
    def encrypt_raw(self,input_text):
        """ Encrypts the input text leaving ALL non alphabetic
        characters unchanged(including numerals and spaces) and returns a
        string, preserving word breaks, punctuation and capitalization.
        """
        text_list = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G',
        'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O',
        'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W',
        'x', 'X', 'y', 'Y', 'z', 'Z'] # Initialize the list with shift = 0.
        text_list_set = set(text_list) # To get non-alpha characters of input text, make a set from 'text_list' ...
        input_text_set = set(input_text) # ... and from the input text ...
        non_alpha_set = input_text_set - text_list_set # ... and subtract text_list_set from input_text_set.
        text_shift = 2 * self.text_shift # Because our list now contains BOTH upper and lower case, shift must be doubled.
        slice_out = text_list [text_shift:] # Slice out 'shift' characters from end ...
        whats_left = text_list[:text_shift] # ... and save what's left.
        for item in reversed(slice_out): # Starting with last sliced out item(hence, 'reversed()') ...
            whats_left.insert(0,item) # ... insert them at the beginning of the list.
        keyed_dictionary = dict(zip(text_list,whats_left)) # Create Key Dictionary from list {plaintext:ciphertext}
        for item in non_alpha_set: # For each non-alpha item ...
            keyed_dictionary[item] = item # ... add it to the dictionary with key EQUAL TO value.
        output_list = [] # Initialize empty list to store ciphertext.
        for character in input_text: # for each item in plaintext list ...
            output_list.append(keyed_dictionary[character]) # ...append its ciphertext item(from 'keyed_dictionary') to list.
        output_text = "".join(output_list) # Convert ciphertext list back to string. . .
        return output_text # ... and return it.
    def decrypt(self,input_text):
        """
        Decrypts the input text and returns a string with formatting
        based on the input text.
        """
        self.text_shift = (-1 * self.text_shift) # Apply the opposite shift by *(-1) ...
        output_text = self.encrypt_raw(input_text) # ... then call the encrypt again with new shift.
        return output_text
i = 1
while i <= 26:
    caesar_cipher3 = CaesarCipher(i)
    plain_text = caesar_cipher3.decrypt("TRDC")
    print("Shift ",i," ",plain_text)
    i += 1