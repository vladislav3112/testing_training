import doctest, pytest

"""Morse Code Translator"""

LETTER_TO_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": " ",
}

MORSE_TO_LETTER = {morse: letter for letter, morse in LETTER_TO_MORSE.items()}


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе
    >>> encode('SOS')
    '... --- ...'
    >>> encode('12%')
    Traceback (most recent call last):
    ...
    KeyError: '%'
    """
    encoded_signs = [LETTER_TO_MORSE[letter] for letter in message]

    return " ".join(encoded_signs)


def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    >>> decode('... --- ...')
    'SOS'
    >>> decode('--. --- --- -.. -....- -.. .- -.--')
    'GOOD-DAY'
    >>> decode('.-1')
    Traceback (most recent call last):
    ...
    KeyError: '.-1'
    """
    decoded_letters = [MORSE_TO_LETTER[letter] for letter in morse_message.split()]

    return "".join(decoded_letters)


# pytests:
@pytest.mark.parametrize(
    "message,expected",
    [
        ("SOS", "... --- ..."),
        ("GOOD-DAY", "--. --- --- -.. -....- -.. .- -.--"),
        ("1", ".----"),
    ],
)
def test_encode(message: str, expected: str):
    assert encode(message) == expected


@pytest.mark.parametrize(
    "message,expected",
    [
        ("... --- ...", "SOS"),
        ("--. --- --- -.. -....- -.. .- -.--", "GOOD-DAY"),
        (".----", "1"),
    ],
)
def test_decode(message: str, expected: str):
    assert decode(message) == expected


if __name__ == "__main__":
    doctest.testmod()
