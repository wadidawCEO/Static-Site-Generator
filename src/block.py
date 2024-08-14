import re

def markdown_to_blocks(markdown):
    splitted = markdown.split("\n\n") # Separate different blocks

    for index, string in enumerate(splitted):
        splitted[index] = re.sub(r"\n\s+", "\n", splitted[index].strip()) # Remove any extra whitespaces, regex is used here to remove spaces in the same block after \n
        splitted[index] = re.sub(r"\s+\n", "\n", splitted[index].strip()) # Same as above, but different order
        if string == "":
            splitted.pop(index)
    if splitted == [""]: # Tackle edge cases where the string is only spaces
        return []

    return splitted