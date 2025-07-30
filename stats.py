def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict:
    char_count = {}
    for char in text:
        char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    return char_count


def sorted_char_counts(char_count: dict) -> list:
    char_count_list = []
    for key, val in char_count.items():
        char_count_list.append({
            "char": key,
            "count": val
        })
    
    char_count_list.sort(key=lambda x: x["count"], reverse=True)
    return char_count_list