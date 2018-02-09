def geni3Out(colors):
    ret = ""
    ret += "set $background\t{0!s}\n".format(colors[0])
    ret += "set $foreground\t{0!s}\n".format(colors[1])

    for i in range(1, 17):
        ret += "set color{0}:\t{1!s}\n".format(i, colors[i + 1])

    return ret
