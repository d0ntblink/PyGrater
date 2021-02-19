
# input:  a string that has potentially bad characters
# return: a cleaned (safe) string
def inputCleanser(dirtyString):
    cleanString = ''
    for c in dirtyString.strip():
        if c.isalnum or c.isspace:
            cleanString += c
        elif c == '?':
            cleanString += c
        else:
            cleanString += ' '

    return cleanString


# don't run this file on its own
if __name__ == "__main__":
    print('This is not the file you are looking for.')