# read the string filename
filename = input()
output_filename = 'gifs_' + filename

result = set()

with open(filename) as f:
    content = f.readlines()

    for line in content:
        log = line.split(' ')

        if log[8] == '200' and log[5] == '"GET':
            get_file_name = log[6]
            if get_file_name.endswith('.gif') or get_file_name.endswith('.GIF'):
                real_file_name = get_file_name[get_file_name.rfind('/')+1:]
                result.add(real_file_name)

with open(output_filename, 'a') as out_file:
    for row in result:
        out_file.write(row)
        out_file.write('\n')

