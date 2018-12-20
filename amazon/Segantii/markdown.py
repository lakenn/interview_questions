import re

def replace_hashtag(markdown, num_hash_tag):
    hashtag = ' ' + '#' * num_hash_tag + ' '

    result = re.search(hashtag, markdown)
    if result:
        if len(markdown[(result.end()+1):]):
            markdown = markdown[:(result.start())] + ' <h%d>' % num_hash_tag +  markdown[(result.end()+1):] + '</h%d>' % num_hash_tag
            return markdown

    return None

def markdownparser(markdown):
    print(re.findall('[^\n]+ # [^\n]+', markdown))

    for i in range(6, 0, -1):
        result = replace_hashtag(markdown, i)
        if result:
            return result

    return markdown

print(markdownparser('# '))