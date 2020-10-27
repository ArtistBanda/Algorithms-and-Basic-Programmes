def reverseStringWoSpecialChars(string):
    string = list(string)

    startPtr = 0
    endPtr = len(string) - 1

    while (startPtr < endPtr):
        if not string[startPtr].isalpha():
            startPtr += 1
        elif not string[endPtr].isalpha():
            endPtr -= 1
        else:
            string[startPtr], string[endPtr] = string[endPtr], string[startPtr]
            startPtr += 1
            endPtr -= 1

    return "".join(string)

# Test Code


string = "a!!!b.c.d,e'f,ghi"
print("Original String : " + string)
rev_string = reverseStringWoSpecialChars(string)
print("Reversed String w/o affecting special chars : " + rev_string)
