# Solve in one line
import unittest


def decode_morse(morse_code):

    morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', 'SOS': '...---...', '!': '-.-.--',
        '.': '.-.-.-'}

    code = {value: key for key, value in morse.items()}

    return ' '.join(''.join(code[letter] for letter in word.split(' ')) for word in morse_code.strip().split('   '))


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(decode_morse('.... . -.--   .--- ..- -.. .'),
                         'HEY JUDE')
        self.assertEqual(decode_morse('.-'), 'A')
        self.assertEqual(decode_morse('.'), 'E')
        self.assertEqual(decode_morse('..'), 'I')
        self.assertEqual(decode_morse('. .'), 'EE')
        self.assertEqual(decode_morse('.   .'), 'E E')
        self.assertEqual(decode_morse('...---...'), 'SOS')
        self.assertEqual(decode_morse('... --- ...'), 'SOS')
        self.assertEqual(decode_morse('...   ---   ...'), 'S O S')
        self.assertEqual(decode_morse(' . '), 'E')
        self.assertEqual(decode_morse('   .   . '), 'E E')
        self.assertEqual(decode_morse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '), 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')


if __name__ == '__main__':
    unittest.main()
