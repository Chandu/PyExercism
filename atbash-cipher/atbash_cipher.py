import re
import string

alphas = string.ascii_lowercase


def decode(input_string):
    to_return = map(transform, input_string.replace(" ", ""))
    return "".join(to_return).strip()


def encode(input_string):
    to_return = map(transform, re.sub("[^a-z0-9]", "", input_string.lower()))
    return re.sub("(.{5})", r"\1 ", "".join(to_return)).strip()


def transform(i):
    entry_index = string.ascii_lowercase.find(i)
    if entry_index >= 0:
        return alphas[entry_index * -1 - 1]
    else:
        return i
