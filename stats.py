def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_counts(char_count):
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list