given an array of huffman code mappings, find the decoded string.

# construct code map
huff_map = {}
for code in codes:
    character, bitcode = code.split('\t')
    if character == '[newline]':
        character = '\n'
    huff_map[bitcode] = character

print(huff_map)

i = 0
temp = ''
result = ''

while i < len(encoded):
    temp += encoded[i]

    val = 