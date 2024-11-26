def remove_white_space(text):
    removed_str = text.replace(" ", "")
    return removed_str

print(remove_white_space("hello  world "))

def rem_spc(text):
    text = list(text)
    if not text:
        return False
    if text:

        for i in range(len(text)):
            if text[i] == " ":
                text[i] = ""
    return "".join(text)

text="kjhu khg wyq   oun"
print(rem_spc(text))