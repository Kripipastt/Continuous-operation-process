LETTER = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
          "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
          "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
          "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
          "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
          "б": "b", "ю": "ju", "ё": "jo"}


def coder(line=""):
    result = ""
    for i in line:
        if i.lower() in LETTER.keys():
            result += (LETTER[i.lower()].capitalize() if i.isupper() else LETTER[i])
        else:
            result += i
    return result


if __name__ == "__main__":
    print(coder("абвг"))
