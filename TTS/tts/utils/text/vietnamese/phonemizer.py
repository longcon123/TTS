from viphoneme import vi2IPA


def vietnamese_text_to_phonemes(text: str, separator: str = "|") -> str:
    delimit = "/"
    text = vi2IPA(text)
    new_text = ''
    for i in range(len(text)-1):
        new_text = new_text + text[i] + separator
    return new_text[0:-1]

print(vietnamese_text_to_phonemes('Tiếng Việt, cũng gọi là tiếng Việt Nam hay Việt ngữ là ngôn ngữ của người Việt'))