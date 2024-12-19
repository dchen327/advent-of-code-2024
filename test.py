s = '''
0b101111011001101000100100000010101000101010
0b101111011001101000100100000010101000101101
0b101111011001101000100100000010101000101111
0b101111101000101000100100000010101000101010
0b101111101000101000100100000010101000101101
0b101111101000101000100100000010101000101111
0b101111101001101000100100000010101000101010
0b101111101001101000100100000010101000101101
0b101111101001101000100100000010101000101111
0b101111111000101000100100000010101000101010
0b101111111000101000100100000010101000101101
0b101111111000101000100100000010101000101111
0b101111111001101000100100000010101000101010
0b101111111001101000100100000010101000101101
0b101111111001101000100100000010101000101111
0b110000001000101000100100000010101000101010
0b110000001000101000100100000010101000101101
0b110000001000101000100100000010101000101111
0b110000001001101000100100000010101000101010
0b110000001001101000100100000010101000101101
0b110000001001101000100100000010101000101111
0b110000011000101000100100000010101000101010
0b110000011000101000100100000010101000101101
0b110000011000101000100100000010101000101111
0b110000011001101000100100000010101000101010
0b110000011001101000100100000010101000101101
0b110000011001101000100100000010101000101111
0b110000101000101000100100000010101000101010
0b110000101000101000100100000010101000101101
0b110000101000101000100100000010101000101111
0b110000101001101000100100000010101000101010
0b110000101001101000100100000010101000101101
0b110000101001101000100100000010101000101111
0b110000111000101000100100000010101000101010
0b110000111000101000100100000010101000101101
0b110000111000101000100100000010101000101111
0b110000111001101000100100000010101000101010
0b110000111001101000100100000010101000101101
0b110000111001101000100100000010101000101111
0b110001001000101000100100000010101000101010
0b110001001000101000100100000010101000101101
0b110001001000101000100100000010101000101111
0b110001001001101000100100000010101000101010
0b110001001001101000100100000010101000101101
0b110001001001101000100100000010101000101111
0b110001011000101000100100000010101000101010
0b110001011000101000100100000010101000101101
0b110001011000101000100100000010101000101111
0b110001011001101000100100000010101000101010
0b110001011001101000100100000010101000101101
0b110001011001101000100100000010101000101111
0b110001101000101000100100000010101000101010
0b110001101000101000100100000010101000101101
0b110001101000101000100100000010101000101111
0b110001101001101000100100000010101000101010
0b110001101001101000100100000010101000101101
0b110001101001101000100100000010101000101111
0b110001111000101000100100000010101000101010
0b110001111000101000100100000010101000101101
0b110001111000101000100100000010101000101111
0b110001111001101000100100000010101000101010
0b110001111001101000100100000010101000101101
0b110001111001101000100100000010101000101111
0b110010001000101000100100000010101000101010
0b110010001000101000100100000010101000101101
0b110010001000101000100100000010101000101111
0b110010001001101000100100000010101000101010
0b110010001001101000100100000010101000101101
0b110010001001101000100100000010101000101111
0b110010011000101000100100000010101000101010
0b110010011000101000100100000010101000101101
0b110010011000101000100100000010101000101111
0b110010011001101000100100000010101000101010
0b110010011001101000100100000010101000101101
0b110010011001101000100100000010101000101111
0b110010101000101000100100000010101000101010
0b110010101000101000100100000010101000101101
0b110010101000101000100100000010101000101111
0b110010101001101000100100000010101000101010
0b110010101001101000100100000010101000101101
0b110010101001101000100100000010101000101111
0b110010111000101000100100000010101000101010
0b110010111000101000100100000010101000101101
0b110010111000101000100100000010101000101111
0b110010111001101000100100000010101000101010
0b110010111001101000100100000010101000101101
0b110010111001101000100100000010101000101111
0b110011001000101000100100000010101000101010
0b110011001000101000100100000010101000101101
0b110011001000101000100100000010101000101111
0b110011001001101000100100000010101000101010
0b110011001001101000100100000010101000101101
0b110011001001101000100100000010101000101111
0b110011011000101000100100000010101000101010
0b110011011000101000100100000010101000101101
0b110011011000101000100100000010101000101111
0b110011011001101000100100000010101000101010
0b110011011001101000100100000010101000101101
0b110011011001101000100100000010101000101111
0b110011101000101000100100000010101000101010
0b110011101000101000100100000010101000101101
0b110011101000101000100100000010101000101111
0b110011101001101000100100000010101000101010
0b110011101001101000100100000010101000101101
0b110011101001101000100100000010101000101111
0b110011111000101000100100000010101000101010
0b110011111000101000100100000010101000101101
0b110011111000101000100100000010101000101111
0b110011111001101000100100000010101000101010
0b110011111001101000100100000010101000101101
0b110011111001101000100100000010101000101111
0b110100001000101000100100000010101000101010
0b110100001000101000100100000010101000101101
0b110100001000101000100100000010101000101111
0b110100001001101000100100000010101000101010
0b110100001001101000100100000010101000101101
0b110100001001101000100100000010101000101111
0b110100011000101000100100000010101000101010
0b110100011000101000100100000010101000101101
0b110100011000101000100100000010101000101111
0b110100011001101000100100000010101000101010
0b110100011001101000100100000010101000101101
0b110100011001101000100100000010101000101111
0b110100101000101000100100000010101000101010
0b110100101000101000100100000010101000101101
0b110100101000101000100100000010101000101111
0b110100101001101000100100000010101000101010
0b110100101001101000100100000010101000101101
0b110100101001101000100100000010101000101111
0b110100111000101000100100000010101000101010
0b110100111000101000100100000010101000101101
0b110100111000101000100100000010101000101111
0b110100111001101000100100000010101000101010
0b110100111001101000100100000010101000101101
0b110100111001101000100100000010101000101111
0b110101001000101000100100000010101000101010
0b110101001000101000100100000010101000101101
0b110101001000101000100100000010101000101111
0b110101001001101000100100000010101000101010
0b110101001001101000100100000010101000101101
0b110101001001101000100100000010101000101111
0b110101011000101000100100000010101000101010
0b110101011000101000100100000010101000101101
0b110101011000101000100100000010101000101111
0b110101011001101000100100000010101000101010
0b110101011001101000100100000010101000101101
0b110101011001101000100100000010101000101111
0b110101101000101000100100000010101000101010
0b110101101000101000100100000010101000101101
0b110101101000101000100100000010101000101111
0b110101101001101000100100000010101000101010
0b110101101001101000100100000010101000101101
0b110101101001101000100100000010101000101111
0b110101111000101000100100000010101000101010
0b110101111000101000100100000010101000101101
0b110101111000101000100100000010101000101111
0b110101111001101000100100000010101000101010
0b110101111001101000100100000010101000101101
0b110101111001101000100100000010101000101111
0b110110001000101000100100000010101000101010
0b110110001000101000100100000010101000101101
0b110110001000101000100100000010101000101111
0b110110001001101000100100000010101000101010
0b110110001001101000100100000010101000101101
0b110110001001101000100100000010101000101111
0b110110011000101000100100000010101000101010
0b110110011000101000100100000010101000101101
0b110110011000101000100100000010101000101111
0b110110011001101000100100000010101000101010
0b110110011001101000100100000010101000101101
0b110110011001101000100100000010101000101111
0b110110101000101000100100000010101000101010
0b110110101000101000100100000010101000101101
0b110110101000101000100100000010101000101111
0b110110101001101000100100000010101000101010
0b110110101001101000100100000010101000101101
0b110110101001101000100100000010101000101111
0b110110111000101000100100000010101000101010
0b110110111000101000100100000010101000101101
0b110110111000101000100100000010101000101111
0b110110111001101000100100000010101000101010
0b110110111001101000100100000010101000101101
0b110110111001101000100100000010101000101111
0b110111001000101000100100000010101000101010
0b110111001000101000100100000010101000101101
0b110111001000101000100100000010101000101111
0b110111001001101000100100000010101000101010
0b110111001001101000100100000010101000101101
0b110111001001101000100100000010101000101111
0b110111011000101000100100000010101000101010
0b110111011000101000100100000010101000101101
0b110111011000101000100100000010101000101111
0b110111011001101000100100000010101000101010
0b110111011001101000100100000010101000101101
0b110111011001101000100100000010101000101111
0b110111101000101000100100000010101000101010
0b110111101000101000100100000010101000101101
0b110111101000101000100100000010101000101111
0b110111101001101000100100000010101000101010
0b110111101001101000100100000010101000101101
0b110111101001101000100100000010101000101111
0b110111111000101000100100000010101000101010
0b110111111000101000100100000010101000101101
0b110111111000101000100100000010101000101111
0b110111111001101000100100000010101000101010
0b110111111001101000100100000010101000101101
0b110111111001101000100100000010101000101111
0b111000001000101000100100000010101000101010
0b111000001000101000100100000010101000101101
0b111000001000101000100100000010101000101111
0b111000001001101000100100000010101000101010
0b111000001001101000100100000010101000101101
0b111000001001101000100100000010101000101111
0b111000011000101000100100000010101000101010
0b111000011000101000100100000010101000101101
0b111000011000101000100100000010101000101111
0b111000011001101000100100000010101000101010
0b111000011001101000100100000010101000101101
0b111000011001101000100100000010101000101111
0b111000101000101000100100000010101000101010
0b111000101000101000100100000010101000101101
0b111000101000101000100100000010101000101111
0b111000101001101000100100000010101000101010
0b111000101001101000100100000010101000101101
0b111000101001101000100100000010101000101111
0b111000111000101000100100000010101000101010
0b111000111000101000100100000010101000101101
0b111000111000101000100100000010101000101111
0b111000111001101000100100000010101000101010
0b111000111001101000100100000010101000101101
0b111000111001101000100100000010101000101111
0b111001001000101000100100000010101000101010
0b111001001000101000100100000010101000101101
0b111001001000101000100100000010101000101111
0b111001001001101000100100000010101000101010
0b111001001001101000100100000010101000101101
0b111001001001101000100100000010101000101111
0b111001011000101000100100000010101000101010
0b111001011000101000100100000010101000101101
0b111001011000101000100100000010101000101111
0b111001011001101000100100000010101000101010
0b111001011001101000100100000010101000101101
0b111001011001101000100100000010101000101111
0b111001101000101000100100000010101000101010
0b111001101000101000100100000010101000101101
0b111001101000101000100100000010101000101111
0b111001101001101000100100000010101000101010
0b111001101001101000100100000010101000101101
0b111001101001101000100100000010101000101111
0b111001111000101000100100000010101000101010
0b111001111000101000100100000010101000101101
0b111001111000101000100100000010101000101111
0b111001111001101000100100000010101000101010
0b111001111001101000100100000010101000101101
0b111001111001101000100100000010101000101111
0b111010001000101000100100000010101000101010
0b111010001000101000100100000010101000101101
0b111010001000101000100100000010101000101111
0b111010001001101000100100000010101000101010
0b111010001001101000100100000010101000101101
0b111010001001101000100100000010101000101111
0b111010011000101000100100000010101000101010
0b111010011000101000100100000010101000101101
0b111010011000101000100100000010101000101111
0b111010011001101000100100000010101000101010
0b111010011001101000100100000010101000101101
0b111010011001101000100100000010101000101111
0b111010101000101000100100000010101000101010
0b111010101000101000100100000010101000101101
0b111010101000101000100100000010101000101111
0b111010101001101000100100000010101000101010
0b111010101001101000100100000010101000101101
0b111010101001101000100100000010101000101111
0b111010111000101000100100000010101000101010
0b111010111000101000100100000010101000101101
0b111010111000101000100100000010101000101111
0b111010111001101000100100000010101000101010
0b111010111001101000100100000010101000101101
0b111010111001101000100100000010101000101111
0b111011001000101000100100000010101000101010
'''

for l in s.strip().splitlines():
    # print in chunks of 3 space sep
    l = l[2:]
    print(' '.join(l[i:i+3] for i in range(0, len(l), 3)))
    # print(l, int(l, 2))

'''

100100000010101000101010 9447978
100100000010101000101101 9447981
100100000010101000101111 9447983
101100000010101000101010 11545130
101100000010101000101101 11545133
101100000010101000101111 11545135
111010000010101000101010 15215146
111010000010101000101101 15215149
111010000010101000101111 15215151
111100000010101000101010 15739434
111100000010101000101101 15739437
111100000010101000101111 15739439


xxx 100 000 010 101 000 101 xxx
-------------------------------
100 100 000 010 101 000 101 010
100 100 000 010 101 000 101 101
100 100 000 010 101 000 101 111
101 100 000 010 101 000 101 010
101 100 000 010 101 000 101 101
101 100 000 010 101 000 101 111
111 010 000 010 101 000 101 010
111 010 000 010 101 000 101 101
111 010 000 010 101 000 101 111
111 100 000 010 101 000 101 010
111 100 000 010 101 000 101 101
111 100 000 010 101 000 101 111
'''