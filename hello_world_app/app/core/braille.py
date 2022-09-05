mapping = {
    ' ': '000000',
    'A': '100000',
    'B': '110000',
    'C': '100100',
    'D': '100110',
    'E': '100010',
    'F': '110100',
    'G': '110110',
    'H': '110010',
    'I': '010100',
    'J': '010110',
    'K': '101000',
    'L': '111000',
    'M': '101100',
    'N': '101110',
    'O': '101010',
    'P': '111100',
    'Q': '111110',
    'R': '111010',
    'S': '011100',
    'T': '011110',
    'U': '101001',
    'V': '111001',
    'W': '010111',
    'X': '101101',
    'Y': '101111',
    'Z': '101011'
}


def solution(st):
    output = [f'{"000001" if c.isupper() else ""}{mapping[c.upper()]}' for c in st]
    return ''.join(output)


a = [

    ("Braille", '000001110000111010100000010100111000111000100010'),

    ("The quick brown fox jumps over the lazy dog",
     "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110")
]

b = (solution(a[0][0]) == a[0][1], solution(a[1][0]) == a[1][1])

print()