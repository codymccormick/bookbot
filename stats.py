def word_count(string):
    return len(string.split())

def char_count(string):
    chars = list(string.lower())
    char_list = {}
    for char in chars:
        if char in char_list:
            char_list[char] += 1
        else:
            char_list[char] = 1
    return char_list

def sort_on(items):
    return items["num"]

def sorted_chars(char_list):
    dict_list = []
    for char, count in char_list.items():
        dict_list.append({"char": char, "num": count})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

