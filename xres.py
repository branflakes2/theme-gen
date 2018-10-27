#generates a .Xresources friendly string

def genXresOut(colors):
    ret = ""
    ret += "*.background:\t[85]{0!s}\n".format(colors['background'])
    ret += "*.foreground:\t{0!s}\n".format(colors['foreground'])
    ret += "*.cursorColor:\t{0!s}\n".format(colors['foreground'])
    ret += "URxvt.border:\t[85]{0!s}\n".format(colors['background'])
    
    for i in range (0, 16):
        ret += "*.color{0}:\t{1!s}\n".format(i, colors['color{0}'.format(i)])

    return ret
