#generates an i3 config friendly string

def geni3Out(colors):
    ret = ""
    ret += "set $background\t{0!s}\n".format(colors['background'])
    ret += "set $foreground\t{0!s}\n".format(colors['foreground'])
    
    for i in range(1, 17):
        ret += "set $color{0}\t{1!s}\n".format(i, colors['color{0}'.format(i)])

    return ret
