def genXresOut(colors):
    ret = ""
    ret += "*.background:\t{0!s}\n".format(colors[0])
    ret += "*.foreground:\t{0!s}\n".format(colors[1])
    ret += "*.cursorColor:\t{0!s}\n".format(colors[1])
    
    for i in range (1, 17):
        ret += "*.color{0}:\t{1!s}\n".format(i, colors[i+1])

    return ret
