import re

with open("cracklib-small") as fname:
    lines = fname.readlines()
    i=1
    for line in range(0, len(lines)):
        if (line < int(i)*875):
            filename = "slave" + str(i) + ".txt"
            open(filename, 'a').write(lines[line])
        else:
            i = i + 1
