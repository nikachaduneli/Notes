TO_CODE = {'!': 'Iok', '"': '|A}W', ' ':'%*h^>',
           '#': '-RO', '$': '+A$/','%': 'e.', '&': 'jZj',
           "'": 'Du', '(': 'C?-',')': 'Pi', '*': '"Q',
           '+': '=_^K', ',': 'F|~','-': '7L', '.': '7mnb',
           '/': 'tB^', '0': '|u%','1': 'p8', '2': '-s37',
           '3': '^ax(', '4': 'OK0','5': "`'", '6': 'U(2`',
           '7': '`{c', '8': 'f4','9': 'Ulw', ':': 'F3}V',
           ';': '-[&0', '<': 'P3','=': ',33', '>': '!S$;',
           '?': 'qF7', '@': 'hs','A': '5v', 'B': '<}u(',
           'C': 'S(x_', 'D': '1/2','E': 'WcF', 'F': 'AH',
           'G': 'B6F', 'H': 'l,]@','I': '$edU', 'J': ']1',
           'K': '0R[', 'L': ']9','M': ';F', 'N': 'Lt^',
           'O': '3@uP', 'P': 'Mp','Q': 'Fo];', 'R': 'Q/',
           'S': 't0r6', 'T': '1E','U': 'kX', 'V': '5y]',
           'W': 'c_7,', 'X': '#ht','Y': 'S4', 'Z': 'rVkJ',
           '[': 'a?%_', '\\': 'w9p8',']': 'Yi', '^': ']&',
           '_': 'Up>%', '`': 'itQM', 'a': ';4Ar', 'b': '6s"a',
           'c': '\\[H', 'd': '&;0Y','e': 'gm', 'f': 'Vq',
           'g': '*8', 'h': '|,by','i': ',TT', 'j': 'CL',
           'k': '%cP=', 'l': '%<t{','m': "Q+'7", 'n': 'GdT',
           'o': 'b*', 'p': 'Tpt','q': 'dUbi', 'r': '3K',
           's': "#'5", 't': '3v`^','u': '+6', 'v': 'F_>u',
           'w': 'mv', 'x': '~M','y': 'FB', 'z': 'I?A',
           '{': '%rL', '|': 'C}','}': '>/S', '~': 'L{X'}

FROM_CODE = dict()

for i in TO_CODE:
    FROM_CODE[TO_CODE.get(i)] = i




def to_code(inpt):
    d = [i for i in inpt]
    l = []
    for i in d:
        l.append(TO_CODE.get(i,'{} not found'.format(i)))
    str1 = "{~@#".join(l)

    return str1




def from_code(inpt):

    d = inpt.split("{~@#")
    l = []
    for i in d:
        l.append(FROM_CODE.get(i,'{} not found'.format(i)))
    str1 = "".join(l)


    return str1
