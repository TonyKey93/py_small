def emoticon_find(text):
    result = [text[i] + text[i+1] for i in range(len(text)) if text[i] == ':']
    print('\n'.join(result))

my_data = input()
emoticon_find(my_data)