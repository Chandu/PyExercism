def detect_anagrams(needle, search_hash):
    to_return = []
    for item in search_hash:
        lower_needle = needle.lower()
        lower_item = item.lower()
        if ''.join(sorted(lower_item)) == ''.join(sorted(lower_needle)) and lower_needle != lower_item:
            to_return.append(item)
    return to_return
