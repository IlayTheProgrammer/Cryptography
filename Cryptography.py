from random import shuffle, random, choice
from copy import deepcopy
from typing import Literal
from os.path import isdir, isfile, realpath
import numpy as np
from PIL import Image
from math import ceil, sqrt

ENG_ALPHABET: tuple[str] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
ENG_ALPHABET_CASE: tuple[str] = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
EXTENDED_ENG_ALPHABET: tuple[str] = (' ', '\n', '!', '?', '"', "'", ':', ';', ',', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
FULL_ENG_ALPHABET: tuple[str] = (' ', '\n', '\t', '#', '№', '~', '`', '$', '^', '&', '<', '>', '|', '/', '\\', '*', '(', ')', '[', ']', '{', '}', '-', '+', '=', '_', '!', '?', '%', '!', '?', '"', "'", ':', ';', ',', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

ALPHABET_OF_SPECIAL_SYMBOLS: tuple[str] = (' ', '\n', '\t', '#', '№', '~', '`', '$', '^', '&', '<', '>', '|', '/', '\\', '*', '(', ')', '[', ']', '{', '}', '-', '+', '=', '_', '!', '?', '%', '!', '?', '"', "'", ':', ';', ',', '.')

RUS_ALPHABET: tuple[str] = ('А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ы', 'Ъ', 'Э', 'Ю', 'Я')
RUS_ALPHABET_CASE: tuple[str] = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ы', 'Ъ', 'Э', 'Ю', 'Я')
EXTENDED_RUS_ALPHABET: tuple[str] = (' ', '\n', '!', '?', '"', "'", ':', ';', ',', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ы', 'Ъ', 'Э', 'Ю', 'Я')
FULL_RUS_ALPHABET: tuple[str] = (' ', '\n', '\t', '#', '№', '~', '`', '$', '^', '&', '<', '>', '|', '/', '\\', '*', '(', ')', '[', ']', '{', '}', '-', '+', '=', '_', '!', '?', '%', '!', '?', '"', "'", ':', ';', ',', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ы', 'Ъ', 'Э', 'Ю', 'Я')



class Systematic_Shuffle:

    def __init__(self, length: int = 'auto', order: list[int]|tuple[int] = 'random_shuffle', warnings: bool = True) -> None:
        """
        <p>A class to shuffle messages' characters in a reversible form</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>length</b>: the size of the messages you are going to shuffle (it's better to set it bigger than needed)
        <p>NOTE:<em> by default it is set to the 'auto' mode, however it will only work if the order is not random. Either set the 'length' parameter to some number, or set order to a list or a tuple of ints</em></p>
        <p>&emsp;<b>order</b>: the order of the shuffled characters. By default set to be random</p>
        <p>&emsp;<b>warnings</b>: when true, shows warning messages that might occur. By default set to be true
        <h2>Used Modules</h2>
        <p>&emsp;<b>copy</b> for the 'deepcopy()' function</p>
        <p>&emsp;<b>random</b> for the 'shuffle()' function</p>
        """

        #Type and validness checks
        #============================================================================================================================================================================
        assert isinstance(length, int) or length == 'auto', f"The 'length' parameter must be of type 'int', not '{type(length)}'!"
        assert isinstance(warnings, bool), f"The 'warnings' parameter must be of type 'bool', not '{type(warnings)}'!"
        assert (length == 'auto' and order != 'random_shuffle') or isinstance(length, int), "The 'length' parameter must only be assigned to 'auto', when the shuffle is non-random!"
        #============================================================================================================================================================================

        #Length assignment if it is set to 'auto'
        #========================================
        if length == 'auto':
            length: int = len(order)
        #========================================

        #If the order is set by the user...
        if order != 'random_shuffle':

            #Various validness checks
            #================================================================================================================================
            assert isinstance(order, (tuple, list)), f"The 'order' parameter must be either of type 'tuple' or 'list', not '{type(order)}'!"

            for element in order:

                if not isinstance(element, int):
                    raise ValueError(f"The 'order' parameter elements must be of type 'int', not '{type(element)}'!")

                elif element < 0:
                    raise ValueError("All the elements of the 'order' parameter must be non-negative!")
                
            assert sorted(list(order)) == list(range(len(order))), "The 'order' parameter sequence is broken!"
            #================================================================================================================================

            self.order: tuple[int] = deepcopy(tuple(order))

        #Otherwise (i.e. when the order is set to be random)...
        else:
            self.order: list[int] = list(range(length))
            shuffle(self.order)
            self.order: tuple[int] = tuple(self.order)

        self.warnings: bool = warnings


    #A system method to format different combinations of messages and orders to a proper form
    def __format_message_and_order(self, message: str) -> tuple[str, tuple[int]]:
        order: tuple[int] = deepcopy(self.order)

        #In case if the message is longer than the order...
        if len(message) > len(self.order):

            #Announcement of the warning
            if self.warnings:
                print(f"WARNING: The length of the 'message' parameter is bigger than the given order. The last {len(message[len(self.order):])} symbols were lost")

            #Formatting of the message
            message: str = message[:len(self.order)]
        
        #Otherwise, if the message is shorter than the order...
        elif len(message) < len(self.order):

            #Announcement of the warning
            if self.warnings:
                print("WARNING: The length of the 'message' parameter is smaller than the given order. The 'order' parameter was adjusted to the length of the message")

            #Formatting of the order
            order: tuple[int] = tuple([i for i in self.order if i < len(message)])

        return (message, order)


    #A method to scramble the message
    def apply(self, message: str) -> str:
        """
        <p>Applies the shuffle to the message</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: the string of characters to scramble</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: shuffled message in the string format</p>
        <h2>Pecularities</h2>
        <p>&emsp;If the length of the message is <b>smaller</b> than expected, the order is adjusted to a proper size</p>
        <p>&emsp;If the length of the message is <b>bigger</b> than expected, the message is cut to a proper size</p>
        <h2>Examples</h2>
        ```python
        >>> ss1: Systematic_Shuffle = Systematic_Shuffle(16, warnings=False)
        >>> ss2: Systematic_Shuffle = Systematic_Shuffle(10, warnings=False)

        >>> ss1.apply("Hello, World!")
        "!Wle rlol,Hdo"

        >>> ss2.apply("Hello, World!")
        " lWlor,oeH"

        >>> shuffled1: str = ss1.apply("Hello, World!")
        >>> shuffled2: str = ss2.apply("Hello, World!")

        >>> len("Hello, World!")
        13

        >>> len(shuffled1)
        13

        >>> len(shuffled2)
        10
        ```
        """

        #Type check
        assert isinstance(message, str), f"The 'message' parameter must be of type 'str', not '{type(phrase)}'!"

        #Formatting of the message and the order
        message, order = self.__format_message_and_order(message)

        #Scramble of the message
        #========================================
        listed_phrase: list[str] = list(message)
        new_phrase: list[str] = ['']*len(message)
        
        for index in order:
            letter: str = listed_phrase.pop(0)
            new_phrase[index] = letter
        #========================================

        del order
        del listed_phrase

        return ''.join(new_phrase)


    #A method to unscramble the message
    def unapply(self, message: str) -> str:
        """
        <p>Unapplies the shuffle</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: the message to unscramble</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: unscrambled message in the string format</p>
        <h2>Pecularities</h2>
        <p>&emsp;If the length of the message is <b>smaller</b> than expected according to the order, the order is adjusted to a proper size</p>
        <p>&emsp;If the length of the message is <b>bigger</b> than expected accroding to the order, the message is cut to a proper size</p>
        <h2>Examples</h2>
        ```python
        >>> ss: Systematic_Shuffle = Systematic_Shuffle(16, warnings=False)
        >>> shuffled: str = ss.apply("Hello, World!")

        >>> shuffled
        "!Wle rlol,Hdo"

        >>> ss.unapply(shuffled)
        "Hello, World!"
        ```
        """

        #Type check
        assert isinstance(message, str), f"The 'message' parameter must be of type 'str', not '{type(phrase)}'!"

        #Formatting of the message and the order
        message, order = self.__format_message_and_order(message)

        #Unscramble of the message
        #========================================
        listed_message: list[str] = list(message)
        result: list[str] = ['']*len(message)
        
        for i, index in enumerate(order):
            letter: str = listed_message[index]
            result[i] = letter
        #========================================

        del listed_message
        del order

        return ''.join(result)


    #Returns the matrix of scrambling
    def __str__(self) -> str:
        result: list[str] = ['']*len(self.order)

        for i, val in enumerate(self.order):
            result[i] = f"[{i}]->[{val}]"

        return ', '.join(result)
    

    #Same as above
    def __repr__(self) -> str:
        result: list[str] = ['']*len(self.order)

        for i, val in enumerate(self.order):
            result[i] = f"[{i}]->[{val}]"

        return ', '.join(result)



class Image_Encipherer:

    def __init__(self, library: str, alphabet: str|list[str]|tuple[str] = EXTENDED_ENG_ALPHABET) -> None:
        """ 
        <p>A class to encipher messages to RGB or B&W images</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>library</b>: a path to a library to save the files to</p>
        <p>&emsp;<b>alphabet</b>: the alphabet to encipher and decipher pictures accordingly</p>
        <h2>Used Modules</h2>
        <p>&emsp;<b>math</b> for the 'ceil()' and 'sqrt()' functions</p>
        <p>&emsp;<b>random</b> for the 'choice()' function</p>
        <p>&emsp;<b>numpy</b> for the class 'ndarray' and its methods, plus the 'full()', 'asarray()', and 'uint8()' functions</p>
        <p>&emsp;<b>PIL</b> for the class 'Image' and its methods</p>
        <p>&emsp;<b>os.path</b> for the 'isdir()', 'realpath()', and 'isfile()' functions</p>
        <h2>Pecularities</h2>
        <p>&emsp;The results might differ from time to time, but they will always be possible to decipher</p>
        """

        #Check if the path is valid
        #========================================================================================================
        assert isinstance(library, str), f"The 'library' parameter must be of type 'str', not '{type(library)}'!"
        assert isdir(realpath(library)), "Invalid path!"
        #========================================================================================================

        #Check if the alphabet is valid
        assert isinstance(alphabet, (str, tuple, list)), f"The 'alphabet' parameter must be either of type 'str', 'tuple[str]' or 'list[str]', not '{type(alphabet)}'!"

        self.path: str = realpath(library)

        #Type check
        #============================================================================================================
        if isinstance(alphabet, (tuple, list)):
            try:
                ''.join(alphabet)
            except TypeError:
                raise TypeError(f"All the elements of the 'alphabet' parameters ({alphabet}) must be of type 'str'!")
        #============================================================================================================
        
        self.alphabet: dict[str:tuple[int]] = dict.fromkeys(alphabet)

        #Binding of the multiple colors to a single character
        #========================================================================================
        ambiguity: int = 1
        while (255 - (len(alphabet)*(ambiguity+1))) > 0:
            ambiguity += 1

        for i, j in enumerate(alphabet, 1):
            self.alphabet[j] = tuple((i + (len(alphabet) * times)) for times in range(ambiguity))
        #========================================================================================

        del ambiguity


    #A system method to calculate the resolution of the image
    def __calculate_resolution(self, message_length: int, rgb: bool) -> tuple[int, int]:
        if rgb:
            return ceil(sqrt(message_length//3)), ceil(sqrt(message_length//3))
        else:
            return ceil(sqrt(message_length)), ceil(sqrt(message_length))
        

    #A system method to encipher the character according to the custom ASCII 
    def __ord(self, character: str) -> int:
        try:
            return choice(self.alphabet[character])
        except KeyError:
            raise KeyError(f"Unable to find the character '{character}' in the alphabet!")
    

    #A system method to decipher the character according to the custom ASCII
    def __chr(self, encoded_character: int) -> str:
        return tuple(self.alphabet.keys())[(int(encoded_character) % len(self.alphabet))-1]
                

    #A system method to format the filename and check, whether it is valid or not
    def __format_filename(self, filename: str) -> str:
        formatted: str = filename.split('/')[-1].split('.')[0]
        assert formatted.replace('_', '').isalnum(), "The 'filename' parameter may only include letters in upper and lower case, numbers and underscores!"

        return formatted
    

    #A system method to shuffle the data, while maintaining the order of the non-empty pixels
    def __shuffle_data_maintaining_order(self, pixels: list[int|tuple[int, int, int]], resolution: tuple[int, int], rgb: bool) -> np.ndarray:
        pixel_zone, extra_pixel_zone = divmod(resolution[0]*resolution[1], len(pixels))

        if not rgb:
            result: list[int] = [0]*(resolution[0]*resolution[1])
            filler: int = 0
        
        else:
            result: list[tuple[int]] = [(0,0,0)]*(resolution[0]*resolution[1])
            filler: tuple[int] = (0,0,0)

        if pixel_zone == 1:
            del result
            del filler

            return [pix for pix in pixels]

        it: int = 0
        matrix: dict[int:int] = dict()

        for i in pixels:

            if extra_pixel_zone != 0:
                result[it] = i
                it += 1
                extra_pixel_zone -= 1

            for _ in range(pixel_zone):
                result[it] = i
                it += 1

            matrix[it] = i

        del pixel_zone
        del extra_pixel_zone

        it = 0
        for k in matrix.keys():
            my_range: list[int] = list(range(it, k, 1))

            ch: int = choice(my_range)
            my_range.remove(ch)

            for i in my_range:
                result[i] = filler

            it = k

        del it
        del matrix

        return result
            

    #A system method to check if user's resolution is valid
    def __resolution_check(self, resolution: tuple[int, int]) -> None:
        assert isinstance(resolution, (tuple, list)), f"The 'resolution' parameter must be either of type 'tuple' or 'list', not '{type(resolution)}'!"
        assert len(resolution) == 2, f"The 'resolution' parameter must be two-dimensional, not '{len(resolution)}'-dimensional!"
        assert isinstance(resolution[0], int) and isinstance(resolution[1], int), f"The 'resolution' parameter must only consist of 'int' values!"
        assert (resolution[0] > 0 and resolution[1] > 0) or (resolution[0] == 0 and resolution[1] == 0), f"The 'resolution' parameter elements must be non-negative!"


    #A method to encipher the message in a numpy array with the shape of (resolution[0], resolution[1], 3)
    def encipher_in_rgb_array(self, message: str, resolution: tuple[int, int]|list[int, int] = (0, 0)) -> np.ndarray:
        """
        <p>Enciphers the message in a numpy array of RGB values</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string to encipher</p>
        <p>&emsp;<b>resolution</b>: width-height proportion of the array (by default it is (0, 0), which is auto)</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: a numpy 3D array with the shape of (resolution[0], resolution[1], 3)</p>
        <h2>Examples</h2>
        ```python
        >>> ie: Image_Encryptor = Image_Encryptor('/home/some_usr/Desktop/My_Lib')
        >>> string: str = "Hello, World"

        >>> ie.encrypt_in_rgb_array(message=string)
        array([[[72, 101, 108], [108, 111, 44]], [[32, 87, 111], [114, 108, 100]]])
        ```
        """

        #Various validness checks
        #=======================================================================================
        assert isinstance(message, str), f"The message must be of type str, not {type(message)}"
        self.__resolution_check(resolution)
        #=======================================================================================

        #A message, translated using custom ASCII table
        listed_message: list[int] = [self.__ord(i) for i in message]

        #Groupping of the string above by triplets
        pixels: list[tuple[int]] = list(zip(listed_message[::3], listed_message[1::3], listed_message[2::3]))

        #Saving of the incomplete pixel
        #==================================================================
        temp: list[int] = listed_message[len(pixels)*3:len(listed_message)]
        temp.extend([0]*(3-len(temp)))

        if temp != [0, 0, 0]:
            pixels.append(tuple(temp))

        del temp
        del listed_message
        #==================================================================

        #Calculation of the resolution and the number of the empty pixels
        #========================================================================================================================================================
        if resolution == (0, 0):
            resolution: tuple[int, int] = self.__calculate_resolution(message_length=len(message), rgb=True)
            
        elif resolution[0]*resolution[1] < len(pixels):
            print(f"WARNING: the given resolution was too small to fit all of the data. Last '{len(pixels[(resolution[0]*resolution[1]):])*3}' symbols got lost")
            pixels: list[tuple[int]] = pixels[:(resolution[0]*resolution[1])]
        #========================================================================================================================================================

        #Addition of the empty pixels
        pixels: list[tuple[int]] = self.__shuffle_data_maintaining_order(pixels=pixels, resolution=resolution, rgb=True)

        return np.uint8(np.reshape(np.array(pixels), (resolution[0], resolution[1], 3)))
    

    #A method to encipher the message in a numpy array with the shape of (resolution[0], resolution[1])
    def encipher_in_bw_array(self, message: str, resolution: tuple[int, int]|list[int, int] = (0, 0)) -> np.ndarray:
        """
        <p>Enciphers the message in a numpy array of B&W values</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string to encipher</p>
        <p>&emsp;<b>resolution</b>: width-height proportion of the picture (by default it is (0, 0), which is auto)
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: a numpy 2D array with the shape of (resolution[0], resolution[1])</p>
        <h2>Examples</h2>
        ```python
        >>> ie: Image_Encryptor = Image_Encryptor('/home/some_usr/Desktop/My_Lib')
        >>> string: str = "Hello, World"

        >>> ie.encrypt_in_bw_array(message=string)
        array([[72, 101, 108, 0], [108, 111, 44, 32], [0, 0, 0, 87], [111, 114, 108, 100]])
        ```
        """

        #Various validness checks
        #=======================================================================================
        assert isinstance(message, str), f"The message must be of type str, not {type(message)}"
        self.__resolution_check(resolution)
        #=======================================================================================

        #A message, translated using custom ASCII table and grouped by triplets
        pixels: list[int] = [self.__ord(i) for i in message]

        #Calculation of the resolution and the number of the empty pixels
        #====================================================================================================================================================
        if resolution == (0, 0):
            resolution: tuple[int, int] = self.__calculate_resolution(message_length=len(message), rgb=False)

        elif resolution[0]*resolution[1] < len(pixels):
            print(f"WARNING: the given resolution was too small to fit all of the data. Last {len(pixels[:(resolution[0]*resolution[1])])} symbols got lost")
            pixels: list[tuple[int]] = pixels[:(resolution[0]*resolution[1])]
        #====================================================================================================================================================

        #Addition of the empty pixels
        pixels: list[int] = self.__shuffle_data_maintaining_order(pixels=pixels, resolution=resolution, rgb=False)

        return np.uint8(np.reshape(np.array(pixels), (resolution[0], resolution[1])))


    #A method to encipher the message in an image
    def encipher(self, message: str, filename: str, rgb: bool = True, resolution: tuple[int, int] = (0, 0)) -> None:
        """
        <p>Enciphers the message in the image format (either RGB or B&W)</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string to encipher</p>
        <p>&emsp;<b>filename</b>: the name of the image</p>
        <p>&emsp;<b>rgb</b>: when true, eciphers image in the RGB format, else applies B&W. By default is set to be true</p>
        <p>&emsp;<b>resolution</b>: width-height proportion of the image (by default it is (0, 0), which is auto)</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: None</p>
        """

        #Various validness checks
        #===========================================================================================================
        assert isinstance(filename, str), f"The 'filename' parameter must be of type 'str', not '{type(filename)}'"
        assert isinstance(rgb, bool), f"The 'rgb' parameter must be of type 'bool', not '{type(rgb)}'"
        #===========================================================================================================

        #Formatted and checked filename
        filename: str = self.__format_filename(filename)

        #Polymorhic encryption
        #=======================================================================
        if rgb:
            result: np.ndarray = self.encipher_in_rgb_array(message, resolution)
            mode: str = 'RGB'
        else:
            result: np.ndarray = self.encipher_in_bw_array(message, resolution)
            mode: str = 'L'
        #=======================================================================

        #Saving of the data as an image
        im: Image = Image.fromarray(np.uint8(result), mode=mode)

        del mode

        #Saving of the image
        im.save(''.join([self.path, '/', filename, '.png']))


    #A method to decipher an RGB or B&W image in text
    def decipher(self, filename_with_ext: str, custom_path: str = '') -> str:
        """
        <p>Deciphers the image in the text format</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>filename_with_ext</b>: the name of the file to read with its extension</p>
        <p>&emsp;<b>custom_path</b>: non-standard path to the file. By default is set to be an empty string</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: deciphered string</p>
        <h2>Examples</h2>
        ```python
        >>> ie: Image_Encryptor = Image_Encryptor('/home/usr/Desktop/My_Lib')

        >>> ie.decrypt('some_pic.png', '/home/usr/Downloads')
        "String with some contents"
        ```
        """

        #Assignment of the path
        #====================================
        if custom_path != '':
            path: str = realpath(custom_path)
        else:
            path: str = self.path
        #====================================

        #Getting the picture extension
        extension: str = ''.join(['.', filename_with_ext.split('.')[-1]])

        #Formatted and checked filename
        filename: str = self.__format_filename(filename_with_ext)

        #Various validness checks
        #===================================================================================================================================================
        assert isinstance(path, str), f"The 'path' parameter must be of type 'str', not '{type(path)}'!"
        assert isfile(''.join([path, '/', filename, extension])), f"There is no such file, located at '{''.join([path, '/', filename, '.png'])}'!"
        assert extension != '.', "The 'filename' parameter must have an extension ('.png', '.jpg', '.jpeg')!"
        assert extension in ['.png', '.jpg', '.jpeg'], f"The 'filename' parameter must either have '.png', '.jpg', or '.jpeg' extension, not '{extension}'!"
        #===================================================================================================================================================

        #Deciphered data
        #==================================================================================================================
        raw_data: np.ndarray = np.reshape(np.asarray(Image.open(''.join([self.path, '/', filename, extension]))), shape=-1)
        return ''.join([self.__chr(i) for i in raw_data if i != 0])
        #==================================================================================================================



class Caesar_Cipher:

    def __init__(self, shift: int, alphabet: str|tuple[str]|list[str] = EXTENDED_ENG_ALPHABET) -> None:
        """
        <p>A class to encipher messages through Caesar's cipher</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>shift</b>: the vector to shift alphabet by</p>
        <p>&emsp;<b>alphabet</b>: the symbols to use for encryption. By default is set to be english alphabet with punctuation marks</p>
        """

        #Various validness checks
        #===========================================================================================================================================
        assert isinstance(shift, int), f"The 'shift' parameter must be of type 'int', not '{type(shift)}'!"
        assert isinstance(alphabet, (str, tuple, list)), f"The 'alphabet' must be either of type 'str', 'list', or 'tuple', not '{type(alphabet)}'!"
        #===========================================================================================================================================

        #Type check
        #===========================================================================================================
        if isinstance(alphabet, (tuple, list)):
            try:
                ''.join(alphabet)
            except TypeError: 
                raise TypeError(f"All the elements of the 'alphabet' parameter ({alphabet}) must be of type 'str'!")
        #===========================================================================================================

        alphabet_copy: list[str] = list(dict.fromkeys(alphabet))

        #Shift of the alphabet
        #=======================================================================
        if shift > 0:
            alphabet_copy: list[str] = alphabet_copy[::-1]

        letters_to_shift: list[str] = alphabet_copy[:(abs(shift)%len(alphabet))]
        alphabet_copy: list[str] = alphabet_copy[(abs(shift)%len(alphabet)):]
        alphabet_copy.extend(letters_to_shift)

        if shift > 0:
            alphabet_copy: list[str] = alphabet_copy[::-1]
        #=======================================================================

        self.alphabet: dict[str:str] = dict(zip(list(dict.fromkeys(alphabet)), alphabet_copy))

        del alphabet_copy


    #Returns comparison of the initial alphabet and the shifted one
    def __str__(self) -> str:
        return '\n'.join([' = '.join(i) for i in self.alphabet.items()])


    #Same as above
    def __repr__(self) -> str:
        return '\n'.join([' = '.join(i) for i in self.alphabet.items()])


    #A method to encipher the message, using shifted alphabet
    def encipher(self, message: str, maintain_special_symbols: bool = True) -> str:
        """
        <p>Enciphers the message, using specified alphabet</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string of characters to encipher</p>
        <p>&emsp;<b>maintain_special_symbols</b>: when true, saves characters that are not specified in the alphabet. By default is set to be true</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: enciphered string</p>
        <h2>Examples</h2>
        ```python
        >>> cc: Caesar_Cipher = Caesar_Cipher(-2)

        >>> cc.encipher('Hello, World!', False)
        "Jgnnq0!Yqtnf\""
        ```
        """

        #Various validness checks
        #=============================================================================================================================================================
        assert isinstance(message, str), f"The 'message' parameter must be of type 'str', not '{type(message)}'!"
        assert isinstance(maintain_special_symbols, bool), f"The 'maintain_special_symbols' parameter must be of type 'bool', not '{type(maintain_special_symbols)}'!"
        #=============================================================================================================================================================

        # #Allocation of the memory for the result
        #==============================================================================
        if not maintain_special_symbols:
            size: int = len([i for i in message if self.alphabet.get(i, None) != None])
        else:
            size: int = len(message)

        result: list[str] = ['']*size
        #==============================================================================

        del size

        #Translation of the message
        #===========================================================
        i: int = 0
        for letter in message:

            if encrypted_letter := self.alphabet.get(letter, False):
                result[i] = encrypted_letter
                i += 1
            elif maintain_special_symbols:
                result[i] = letter
                i += 1
        #===========================================================

        del i

        return ''.join(result)


    #A method to decipher the message, using shifted alphabet
    def decipher(self, message: str) -> str:
        """
        <p>Deciphers the message, using specified alphabet</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string of characters to decipher</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: deciphered string</p>
        <h2>Examples</h2>
        ```python
        >>> ca: Caesar_Cipher = Caesar_Cipher(-2)

        >>> ca.decipher("Jgnnq0!Yqtnf\"")
        "Hello, World!"
        ```
        """

        #Type check
        assert isinstance(message, str), f"The 'message' parameter must be of type 'str', not '{type(message)}'!"

        #Swap of keys and values
        swapped_alphabet: dict[str:str] = {j:i for i, j in self.alphabet.items()}

        #Decryption of the message
        result: list[str] = [swapped_alphabet.get(letter, False) if swapped_alphabet.get(letter, False) else letter for letter in message]

        del swapped_alphabet

        return ''.join(result)



class Homophonic_Substitution:
    
    def __init__(self, new_alphabet: str|tuple[str]|list[str] = 'random_shuffle', former_alphabet: str|tuple[str]|list[str] = ENG_ALPHABET_CASE, case_sensetive: bool = False) -> None:
        """
        <p>A class to encipher messages through homophonic substitution, aka alphabet shuffle</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>new_alphabet</b>: the new alphabet to encipher former alphabet's letters. By default it is set to be a randomly shuffled former alphabet</p>
        <p>&emsp;<b>former_alphabet</b>: initial alphabet. By default is assigned to be the english alphabet with punctuation marks</p>
        <p>&emsp;<b>case_sensetive</b>: when true, maintains the case of the letters. By default is set to be false</p>
        <h2>Used Modules</h2>
        <p>&emsp;<b>random</b> for the 'shuffle()' function</p>
        """

        #Various validness checks
        #==================================================================================================================================================================================================================================================================================================
        assert isinstance(former_alphabet, (str, tuple, list)), f"The 'former_alphabet' parameter must be either of type 'str', 'list', or 'tuple', not '{type(former_alphabet)}'!"
        assert isinstance(new_alphabet, (str, tuple, list)), f"The 'new_alphabet' parameter must be either of type 'str', 'list', or 'tuple', not '{type(new_alphabet)}'!"
        assert len(list(dict.fromkeys(new_alphabet))) == len(list(dict.fromkeys(former_alphabet))) or new_alphabet == 'random_shuffle', f"The length of the 'new_alphabet' parameter must be exact equal to the length of the 'former_alphabet' parameter ({len(new_alphabet)} != {len(former_alphabet)})!"

        if isinstance(former_alphabet, (tuple, list)):
            try:
                ''.join(former_alphabet)
            except TypeError: 
                raise TypeError(f"All the elements of the 'former_alphabet' parameter ({former_alphabet}) must be of type 'str'!")

        if isinstance(new_alphabet, (tuple, list)):
            try:
                ''.join(new_alphabet)
            except TypeError: 
                raise TypeError(f"All the elements of the 'new_alphabet' parameter ({new_alphabet}) must be of type 'str'!")
        #==================================================================================================================================================================================================================================================================================================

        if isinstance(new_alphabet, str) and new_alphabet != 'random_shuffle':
            new_alphabet: list[str] = list(new_alphabet)

        if isinstance(former_alphabet, str):
            former_alphabet: list[str] = list(former_alphabet)

        #Creation of the translational matrix
        #================================================================================================================
        if not case_sensetive:
            former_alphabet: list[str] = [i.upper() if i not in ['\n', '\t'] else i for i in former_alphabet]

        if new_alphabet == 'random_shuffle':
            new_alphabet: list[str] = deepcopy(former_alphabet)
            shuffle(new_alphabet)

        elif not case_sensetive:
            new_alphabet: list[str] = [i.upper() if i not in ['\n', '\t'] else i for i in new_alphabet]

        self.alphabet: dict[str:str] = dict(zip(list(dict.fromkeys(new_alphabet)), list(dict.fromkeys(former_alphabet))))
        #================================================================================================================

        self.maintain_case: bool = case_sensetive

        del former_alphabet
        del new_alphabet


    #Returns the translational matrix
    def __str__(self) -> str:
        return '; '.join([' = '.join(i) for i in self.alphabet.items()])


    #Same as above
    def __repr__(self) -> str:
        return '; '.join([' = '.join(i) for i in self.alphabet.items()])
    

    #A method to encipher the message, using translational matrix
    def encipher(self, message: str, maintain_special_symbols: bool = True) -> str:
        """
        <p>Enciphers the message, using specified translational matrix</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string of characters to encipher</p>
        <p>&emsp;<b>maintain_special_symbols</b>: when true, saves characters that are not specified in the alphabet. By default is set to be true</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: enciphered string</p>
        <h2>Examples</h2>
        ```python
        >>> hs: Homophonic_Substitution = Homophonic_Substitution()

        >>> hs.encipher("Hello, World!")
        "MKPPU, LUAPY!"

        >>> hs.encipher("Hello, World!", False)
        "MKPPULUAPY"
        ```
        """

        #Type checks
        #==============================================================================================================================================================
        assert isinstance(message, str), f"The 'message' parameter must be of type 'str', not '{type(message)}'!"
        assert isinstance(maintain_special_symbols, bool), f"The 'maintain_special_symbols' parameter must be of type 'bool', not '{type(maintain_special_symbols)}'!"
        #==============================================================================================================================================================

        #Determination of whether to save the case or not
        #================================================
        if not self.maintain_case:
            message: str = message.upper()
        #================================================

        #Allocation of the memory for the result
        #===========================================================================================
        if not maintain_special_symbols:
            result: list[str] = ['']*len([i for i in message if self.alphabet.get(i, None) != None])
        else:
            result: list[str] = ['']*len(message)
        #===========================================================================================

        #Encryption of the message
        #============================================================
        i: int = 0
        for letter in message:

            if enciphered_letter := self.alphabet.get(letter, False):
                result[i] = enciphered_letter
                i += 1
            elif maintain_special_symbols:
                result[i] = letter
                i += 1
        #===========================================================

        del i

        return ''.join(result)


    #A method to decipher the message, using translational matrix
    def decipher(self, message: str) -> str:
        """
        <p>Deciphers the message, using specified translational matrix</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string of characters to decipher</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: deciphered string</p>
        <h2>Examples</h2>
        ```python
        >>> hs: Homophonic_Substitution = Homophonic_Substitution()

        >>> hs.decipher("MKPPU, LUAPY!")
        "HELLO, WORLD!"
        ```
        """

        #Type check
        assert isinstance(message, str), f"The 'message' parameter must be of type 'str', not '{type(message)}'!"

        #Determination of whether to save the case or not
        #================================================
        if not self.maintain_case:
            message: str = message.upper()
        #================================================

        #Allocation of the memory for the result
        result: list[str] = ['']*len(message)

        swapped_alphabet: dict[str:str] = {j:i for i, j in self.alphabet.items()}

        #Decryption of the message
        #==============================================================
        for i, letter in enumerate(message):

            if deciphered_letter := swapped_alphabet.get(letter, False):
                result[i] = deciphered_letter
            else:
                result[i] = letter
        #==============================================================

        del swapped_alphabet

        return ''.join(result)



class Distorter:

    def __init__(self, chance_of_distortion: float, element_of_distortion: Literal['random_letters']|str) -> None:
        """
        <p>A class to corrupt the message with specified elements</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>chance_of_distortion</b>: a float number that determines how likely it is to distort a singular piece of data</p>
        <p>&emsp;<b>element_of_distortion</b>: a character or a string to replace characters with. By default picks random values from the message</p>
        <h2>Used Modules</h2>
        <p>&emsp;<b>random</b> for the 'random()' and 'choice()' functions</p>
        <p>&emsp;<b>typing</b> for the class 'Literal'</p>
        <h2>Pecularities</h2>
        <p>&emsp;The distortion is irreversible</p>
        """

        #Various validness checks
        #===================================================================================================================================================
        assert isinstance(chance_of_distortion, float), f"The parameter 'chance_of_corruption' must be of type 'float', not '{type(chance_of_distortion)}'!"
        assert isinstance(element_of_distortion, str), f"The parameter 'element_of_corruption' must be of type 'str', not '{type(element_of_distortion)}'!"
        assert chance_of_distortion >= 0.0 and chance_of_distortion <= 1.0, "The parameter 'chance_of_distoriton' must be in the margin of 1.0-0.0!"
        #===================================================================================================================================================

        self.chance: float = chance_of_distortion
        self.distortion_element: str = element_of_distortion


    #Returns a string, containing the chance and the element
    def __str__(self) -> str:
        return f"Distorts with '{self.distortion_element}' with the chance of {self.chance*100}%"
    

    #Same as above
    def __repr__(self) -> str:
        return f"Distorts with '{self.distortion_element}' with the chance of {self.chance*100}%"
    

    #Distorts the message
    def distort(self, message: str) -> str:
        """
        <p>Distorts the message, by replacing the letters with specified characters</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string to distort</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: a distorted string</p>
        <h2>Examples</h2>
        ```python
        >>> d: Distorter = Distorter(0.3, '#')

        >>> d.distort("Hello, World!")
        "He#lo, ##rld#"
        ```
        """

        #Type check
        assert isinstance(message, str), f"The 'message' parameter must be of type 'str', not '{type(phrase)}'!"

        listed_message: list[str] = list(message)

        #Distortion of the message
        #=======================================================
        for i in range(len(message)):

            if random() < self.chance:

                if self.distortion_element == 'random_letters':
                    listed_message[i] = choice(message)
                else:
                    listed_message[i] = self.distortion_element
        #=======================================================

        return ''.join(listed_message)
    


class Base_Encipherer:

    #A system exception class. Raised when the message cannot be deciphered
    class AmbiguityException(BaseException):
        def __init__(self) -> None:
            super().__init__("You cannot decipher non-separated string!")


    def __init__(self, separator: str = '/') -> None:
        """
        <p>A class to encipher messages in alterantive base systems (1-36)</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>separator</b>: a character or a string of characters, separating pieces of the enciphered data</p>
        <h2>Pecularities</h2>
        <p>&emsp;If the separator is equal to an empty string and the message is not a list or a tuple, the AmbiguityException is raised</p>
        """

        #Type check
        assert isinstance(separator, str), f"The 'separator' parameter must be of type 'str', not '{type(separator)}'!"

        self.separator = separator


    #A system method converting any base number to a decimal
    def __dec(self, number: str, base: int) -> int:
        alphabet: list[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        result: int = 0

        for i, digit in enumerate(number[::-1].upper()):
            try:
                result += (alphabet.index(digit) * (base**i))
            except IndexError:
                raise ValueError("All of the number's elements must be in the margin of 0-Z!")

        return result


    #A system method checking type of the message
    def __typecheck(self, message: str) -> None:
        assert isinstance(message, str), f"The 'message' parameter must be of type 'str', not '{type(phrase)}'!"


    #A system method checking content type
    def __contentcheck(self, message: str|tuple[str]|list[str]) -> None:
        if isinstance(message, (list, tuple)):
            try:
                _ = ''.join(message)
            except TypeError:
                raise TypeError(f"All the elements of the 'message' parameter ({message}) must be of type 'str'!")

        elif not isinstance(message, str):
            raise TypeError(f"The 'message' parameter must be either of type 'str', 'list' or 'tuple', not '{type(message)}'!")


    #A system method to reverse any kind of translation
    def __reverse_translation(self, message: str|tuple[str]|list[str], base: int) -> str:

        if self.separator != '' and not isinstance(message, (tuple, list)):
            return ''.join([chr(self.__dec(i, base)) for i in message.split(self.separator)])
        
        elif isinstance(message, (tuple, list)):
            return ''.join([chr(self.__dec(i, base)) for i in message])
        
        else:
            raise self.AmbiguityException()
        

    #A method that enciphers the message in its binary form
    def to_bin(self, message: str, string_format: bool = True) -> str|list[str]:
        """
        <p>Enciphers the message to its binary form</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string to encipher</p>
        <p>&emsp;<b>string_format</b>: when true, returns a string, else returns a list of strings. By default is set to be true</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: enciphered string or a list of enciphered strings</p>
        <h2>Examples</h2>
        ```python
        >>> be: Base_Encipherer = Base_Encipherer()

        >>> be.to_bin("Hello, World!")
        "1001000/1100101/1101100/1101100/1101111/101100/100000/..."

        >>> be.to_bin("Hello, World!", False)
        ['1001000', '1100101', '1101100', '1101100', '1101111', '101100', '100000'...]
        ```
        """

        #Type check
        self.__typecheck(message)

        #Encryption of the message
        #===============================================================================
        if string_format:
            return self.separator.join([bin(ord(i))[2:].upper() for i in list(message)])
        else: 
            return [bin(ord(i))[2:].upper() for i in list(message)]
        #===============================================================================


    #A method that enciphers the message in its octagonal form
    def to_oct(self, message: str, string_format: bool = True) -> str|list[str]:
        """
        <p>Enciphers the message to its octagonal form</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string to encipher</p>
        <p>&emsp;<b>string_format</b>: when true, returns a string, else returns a list of strings. By default is set to be true</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: enciphered string or a list of enciphered strings</p>
        <h2>Examples</h2>
        ```python
        >>> be: Base_Encipherer = Base_Encipherer()

        >>> be.to_oct("Hello, World!")
        "110/145/154/154/157/54/40/127/157/162/154/144/41"

        >>> be.to_oct("Hello, World!", False)
        ['110', '145', '154', '154', '157', '54', '40', '127', '157', '162', '154', '144', '41']
        ```
        """

        #Type check
        self.__typecheck(message)

        #Encryption of the message
        #===============================================================================
        if string_format:
            return self.separator.join([oct(ord(i))[2:].upper() for i in list(message)])
        else: 
            return [oct(ord(i))[2:].upper() for i in list(message)]
        #===============================================================================


    #A method that enciphers the message in its decimal form
    def to_dec(self, message: str, string_format: bool = True) -> str|list[str]:
        """
        <p>Enciphers the message to its decimal form</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string to encipher</p>
        <p>&emsp;<b>string_format</b>: when true, returns a string, else returns a list of strings. By default is set to be true</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: enciphered string or a list of enciphered strings</p>
        <h2>Examples</h2>
        ```python
        >>> be: Base_Encipherer = Base_Encipherer()

        >>> be.to_dec("Hello, World!")
        "72/101/108/108/111/44/32/87/111/114/108/100/33"

        >>> be.to_dec("Hello, World!", False)
        ['72', '101', '108', '108', '111', '44', '32', '87', '111', '114', '108', '100', '33']
        ```
        """

        #Type check
        self.__typecheck(message)

        #Encryption of the message
        #==========================================================================
        if string_format:
            return self.separator.join([str(ord(i)).upper() for i in list(message)])
        else: 
            return [str(ord(i)).upper() for i in list(message)]
        #==========================================================================


    #A method that enciphers the message in its hexagonal form
    def to_hex(self, message: str, string_format: bool = True) -> str|list[str]:
        """
        <p>Enciphers the message to its hexagonal form</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string to encipher</p>
        <p>&emsp;<b>string_format</b>: when true, returns a string, else returns a list of strings. By default is set to be true</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: enciphered string or a list of enciphered strings</p>
        <h2>Examples</h2>
        ```python
        >>> be: Base_Encipherer = Base_Encipherer()

        >>> be.to_hex("Hello, World!")
        "48/65/6C/6C/6F/2C/20/57/6F/72/6C/64/21"

        >>> be.to_hex("Hello, World!", False)
        ['48', '65', '6C', '6C', '6F', '2C', '20', '57', '6F', '72', '6C', '64', '21']
        ```
        """

        #Type check
        self.__typecheck(message)

        #Encryption of the message
        #===============================================================================
        if string_format:
            return self.separator.join([hex(ord(i))[2:].upper() for i in list(message)])
        else: 
            return [hex(ord(i))[2:].upper() for i in list(message)]
        #===============================================================================
        

    #A method that enciphers the message in its 36 form
    def to_36(self, message: str, string_format: bool = True) -> str|list[str]:
        """
        <p>Enciphers the message to its 36 form</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string to encipher</p>
        <p>&emsp;<b>string_format</b>: when true, returns a string, else returns a list of strings. By default is set to be true</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: enciphered string or a list of enciphered strings</p>
        <h2>Examples</h2>
        ```python
        >>> be: Base_Encipherer = Base_Encipherer()

        >>> be.to_36("Hello, World!")
        "20/2T/30/30/33/18/W/2F/33/36/30/2S/X"

        >>> be.to_36("Hello, World!", False)
        ['20', '2T', '30', '30', '33', '18', 'W', '2F', '33', '36', '30', '2S', 'X']
        ```
        """

        #Type check
        self.__typecheck(message)

        #Encryption of the message
        #=========================================================================================================================================================================================================
        alphabet: list[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        result: list[str] = []

        for char in list(message):
            char36: list[str] = []
            number: int = ord(char)

            while number != 0:
                char36.append(alphabet[number % 36])
                number //= 36

            result.append(''.join(char36[::-1]))

        del alphabet

        if string_format:
            return self.separator.join(result)
        else:
            return result
        #=========================================================================================================================================================================================================


    #A method that enciphers the message in its nbase form
    def to_custom(self, message: str, nbase: int, string_format: bool = True) -> str|list[str]:
        """
        <p>Enciphers the message to its nbase form</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string to encipher</p>
        <p>&emsp;<b>nbase</b>: a base to encipher the message to (must be less than 37 and greater than 1)</p>
        <p>&emsp;<b>string_format</b>: when True, returns string, else returns list of strings</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: enciphered string or a list of enciphered strings</p>
        <h2>Examples</h2>
        ```python
        >>> be: Base_Encipherer = Base_Encipherer()

        >>> be.to_custom("Hello, World!", 19)
        "3F/56/5D/5D/5G/26/1D/4B/5G/60/5D/55/1E"

        >>> be.to_custom("Hello, World!", 19, False)
        ['3F', '56', '5D', '5D', '5G', '26', '1D', '4B', '5G', '60', '5D', '55', '1E']
        ```
        """

        #Type check
        #==================================================================================================
        self.__typecheck(message)
        assert isinstance(nbase, int), f"The 'nbase' parameter must be of type 'int', not '{type(nbase)}'!"
        #==================================================================================================

        #Base check
        assert nbase > 0 and nbase < 37, "The 'nbase' parameter must be in the margin of 1-36!" 

        #Encryption of the message
        #=========================================================================================================================================================================================================
        alphabet: list[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        result: list[str] = []

        for char in list(message):
            chars: list[str] = []
            number: int = ord(char)

            while number != 0:
                chars.append(alphabet[number % nbase])
                number //= nbase

            result.append(''.join(chars[::-1]))

        del alphabet

        if string_format:
            return self.separator.join(result)
        else:
            return result
        #=========================================================================================================================================================================================================


    #A method that deciphers the message from its binary form
    def from_bin(self, message: str|list[str]|tuple[str]) -> str:
        """
        <p>Deciphers the message from its binary form</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string, tuple or list to decipher</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: deciphered string</p>
        <h2>Examples</h2>
        ```python
        >>> be: Base_Encipherer = Base_Encipherer()

        >>> be.from_bin("20/2T/30/30/33/18/W/2F/33/36/30/2S/X")
        "Hello, World!"
        ```
        """
        
        #Type check
        self.__contentcheck(message)

        return self.__reverse_translation(message, 2)


    #A method that deciphers the message from its octagonal form
    def from_oct(self, message: str|list[str]|tuple[str]) -> str:
        """
        <p>Deciphers the message from its octagonal form</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string, tuple or list to decipher</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: deciphered string</p>
        <h2>Examples</h2>
        ```python
        >>> be: Base_Encipherer = Base_Encipherer()

        >>> be.from_oct("110/145/154/154/157/54/40/127/157/162/154/144/41")
        "Hello, World!"
        ```
        """
        
        #Type check
        self.__contentcheck(message)

        return self.__reverse_translation(message, 8)


    #A method that deciphers the message from its decimal form
    def from_dec(self, message: str|list[str]|tuple[str]) -> str:
        """
        <p>Deciphers the message from its decimal form</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string, tuple or list to decipher</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: deciphered string</p>
        <h2>Examples</h2>
        ```python
        >>> be: Base_Encipherer = Base_Encipherer()

        >>> be.from_dec("72/101/108/108/111/44/32/87/111/114/108/100/33")
        "Hello, World!"
        ```
        """
        
        #Type check
        self.__contentcheck(message)

        return self.__reverse_translation(message, 10)


    #Deciphers the message from its hexagonal form
    def from_hex(self, message: str|list[str]|tuple[str]) -> str:
        """
        <p>Deciphers the message from its hexagonal form</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string, tuple or list to decipher</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: deciphered string</p>
        <h2>Examples</h2>
        ```python
        >>> be: Base_Encipherer = Base_Encipherer()

        >>> be.from_hex("48/65/6C/6C/6F/2C/20/57/6F/72/6C/64/21")
        "Hello, World!"
        ```
        """
        
        #Type check
        self.__contentcheck(message)

        return self.__reverse_translation(message, 16)
    

    #A method that deciphers the message from its 36 form
    def from_36(self, message: str|list[str]|tuple[str]) -> str:
        """
        <p>Deciphers the message from its 36 form</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string, tuple or list to decipher</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: deciphered string</p>
        <h2>Examples</h2>
        ```python
        >>> be: Base_Encipherer = Base_Encipherer()

        >>> be.from_hex("20/2T/30/30/33/18/W/2F/33/36/30/2S/X")
        "Hello, World!"
        ```
        """
        
        #Type check
        self.__contentcheck(message)

        return self.__reverse_translation(message, 36)


    #A method that deciphers the message from its nbase form
    def from_custom(self, message: str|list[str]|tuple[str], nbase: int) -> str:
        """
        <p>Deciphers the message from its nbase form</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string, tuple or list to decipher</p>
        <p>&emsp;<b>nbase</b>: a base to decipher the message from (must be less than 37 and greater than 1)</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: deciphered string</p>
        <h2>Examples</h2>
        ```python
        >>> be: Base_Encipherer = Base_Encipherer()

        >>> be.from_custom("3F/56/5D/5D/5G/26/1D/4B/5G/60/5D/55/1E", 19)
        "Hello, World!"
        ```
        """
        
        #Type check
        #==================================================================================================
        self.__contentcheck(message)
        assert isinstance(nbase, int), f"The 'nbase' parameter must be of type 'int', not '{type(nbase)}'!"
        #==================================================================================================

        #Base check
        assert nbase > 0 and nbase < 37, "The 'nbase' parameter must be in the margin of 1-36!" 

        return self.__reverse_translation(message, nbase)
    


class Vigenere_Table:

    def __init__(self, keyword: str = '', alphabet: str|list[str]|tuple[str] = ENG_ALPHABET, case_sensitive: bool = False) -> None:
        """
        <p>A class to encipher messages, using vigenere table</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>keyword</b>: a keyword to add at the beginning of the alphabet (makes it more difficult to decipher without the table). By default it is not applied</p>
        <p>&emsp;<b>alphabet</b>: the characters that will be used for the encryption. By default includes uppercase English alphabet and punctuation marks</p>
        <p>&emsp;<b>case_sensitive</b>: when true, maintains the case of the letters. By default is set to be false
        <h2>Used Modules</h2>
        <p>&emsp;<b>copy</b> for the 'deepcopy()' function</p>
        """

        #Type checks
        #======================================================================================================================================================
        assert isinstance(keyword, str), f"The 'keyword' parameter must be of type 'str', not '{type(keyword)}'!"
        assert isinstance(alphabet, (str, tuple, list)), f"The 'alphabet' parameter must be either of type 'str', 'tuple', or 'list', not '{type(alphabet)}'!"
        assert isinstance(case_sensitive, bool), f"The 'case_sensitive' parameter must be of type 'bool', not '{type(case_sensitive)}'!"
        assert len(alphabet) > 0, "The length of the parameter 'alphabet' must not be equal to zero!"
        #======================================================================================================================================================

        if isinstance(alphabet, str):
            alphabet: list[str] = list(alphabet)

        #To add a keyword if it is a non-empty string
        #=====================================================
        if keyword != '':
            alphabet: list[str] = [*list(keyword), *alphabet]
        #=====================================================

        #To create the translational table
        #======================================================================================
        if not case_sensitive:
            alphabet: list[str] = [i.upper() if i not in ['\n', '\t'] else i for i in alphabet]
        
        self.alphabet: list[str] = list(dict.fromkeys(alphabet))
        alphabet_copy: list[str] = deepcopy(self.alphabet)

        del alphabet

        self.table: dict[str:dict[str:str]] = dict()
        length: int = len(self.alphabet)

        for row in range(length):
            temporary: dict[str:str] = dict()

            for column in range(length):
                temporary[self.alphabet[column]] = alphabet_copy[column]

            self.table[self.alphabet[row]] = temporary
            letter: str = alphabet_copy.pop(0)
            alphabet_copy.append(letter)
        #======================================================================================

        self.maintain_case: bool = case_sensitive

        del length
        del alphabet_copy


    #A system method to adjust keyword's length to the message
    def __format_keyword(self, message: list[str], keyword: list[str]) -> list[str]:
        keyword_copy: list[str] = deepcopy(keyword)
        
        if len(keyword) < len(message):
            iterator: int = 0

            while len(keyword_copy) < len(message):
                keyword_copy.append(keyword[iterator % len(keyword)])
                iterator += 1

        elif len(keyword) > len(message):

            while len(keyword_copy) > len(message):
                keyword_copy.pop(-1)

        return keyword_copy


    #A method to encipher the message, using specified keyword
    def encipher(self, message: str, keyword: str, maintain_special_symbols: bool = True) -> str:
        """
        <p>Enciphers the message, using specified translational table and a keyword</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string of characters to encipher</p>
        <p>&emsp;<b>keyword</b>: a word or a phrase to encipher the message with (do not forget it, since it is necessary for the decryption)</p>
        <p>&emsp;<b>maintain_special_symbols</b>: when true, saves characters that are not specified in the table, By default is set to be true</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: enciphered string</p>
        <h2>Examples</h2>
        ```python
        >>> vt: Vigenere_Table = Vigenere_Table('KRYPTOS')

        >>> vt.encipher("Hello, World!", "random")
        "IMDRD, TXEVY!"

        >>> vt.encipher("Hello, World!", "random", False)
        "IMDRDTXEVY"
        ```
        """
        
        #Type checks
        #=============================================================================================================================================================
        assert isinstance(keyword, str), f"The 'keyword' parameter must be of type 'str', not '{type(keyword)}'!"
        assert isinstance(message, str), f"The 'message' parameter must be of type 'str', not '{type(message)}'!"
        assert isinstance(maintain_special_symbols, bool), f"The 'maintain_special_symbols' parameter must be of type 'bool', not '{type(maintain_special_symbols)}'!"
        #=============================================================================================================================================================

        #To encipher the message
        #==========================================================================================================================
        if not self.maintain_case:
            message: str = message.upper()
            keyword: str = keyword.upper()

        listed_message: list[str] = list(message)
        true_keyword: list[str] = self.__format_keyword(listed_message, list(keyword))
        result: list[str] = []

        for letter in range(len(listed_message)):

            if self.table.get(listed_message[letter], False) and self.table[listed_message[letter]].get(true_keyword[letter], False):
                result.append(self.table[listed_message[letter]][true_keyword[letter]])

            elif maintain_special_symbols:
                result.append(listed_message[letter])
        #==========================================================================================================================

        del listed_message
        del true_keyword

        return ''.join(result)


    #A method to decipher the message, using specified keyword
    def decipher(self, message: str, keyword: str) -> str:
        """
        <p>Deciphers the message, using specified translational table and a keyword</p>
        <h2>Parameters</h2>
        <p>&emsp;<b>message</b>: a string of characters to decipher</p>
        <p>&emsp;<b>keyword</b>: a word or a phrase to decipher the message with</p>
        <h2>Returns</h2>
        <p>&emsp;<b>out</b>: deciphered string</p>
        <h2>Examples</h2>
        ```python
        >>> vt: Vigenere_Table = Vigenere_Table('KRYPTOS')

        >>> vt.decipher("IMDRD, TXEVY!", "random")
        "HELLO, WORLD!"

        #If you forgot the keyword, the result will be significantly different
        # from what you would expect
        >>> vt.decipher("IMDRD, TXEVY!", "randam")
        "JZPEL, ELUPQ!"
        ```
        """

        #Type checks
        #========================================================================================================
        assert isinstance(keyword, str), f"The 'keyword' parameter must be of type 'str', not '{type(keyword)}'!"
        assert isinstance(message, str), f"The 'message' parameter must be of type 'str', not '{type(message)}'!"
        #========================================================================================================

        #To decipher the message
        #=======================================================================================
        if not self.maintain_case:
            message: str = message.upper()
            keyword: str = keyword.upper()

        listed_message: list[str] = list(message)
        true_keyword = self.__format_keyword(listed_message, list(keyword))
        result: list[str] = []

        for i in range(len(listed_message)):

            if not self.table.get(listed_message[i], False):
                result.append(listed_message[i])
                continue
            
            for word_letter, column in self.table.items():

                for keyword_letter, encoded_letter in column.items():

                    if keyword_letter == true_keyword[i] and encoded_letter == listed_message[i]:
                        result.append(word_letter)
                        break
                else:
                    continue

                break
        #=======================================================================================

        del listed_message
        del true_keyword

        return ''.join(result)
    

    #Returns the table
    def __str__(self) -> str:
        table: list[str] = ['']

        for row_lt, column in self.table.items():
            for col_lt, code_lt in column.items():
                table.append(code_lt)

            table.append('\n')

        return ' '.join(table)


    #Same as above
    def __repr__(self) -> str:
        table: list[str] = ['']

        for row_lt, column in self.table.items():
            for col_lt, code_lt in column.items():
                table.append(code_lt)

            table.append('\n')

        return ' '.join(table)

