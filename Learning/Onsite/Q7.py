def rebuild_message(parts):
    first_char_map = {}
    for part in parts:
        first_char_map[part[0]] = part

    # Start with 'A'
    sentence = first_char_map.pop('A')

    while first_char_map:
        next_part = first_char_map.pop(sentence[-1])
        sentence += next_part[1:]


    return sentence


print(rebuild_message(['ABESE FSDFDSF C', 'B SSFDFDF E', 'C CDFDSFSD B', 'E sdfdsfds Z']))
