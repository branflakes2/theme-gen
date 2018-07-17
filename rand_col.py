#Converted from javascript taken from the terminal.sexy project
#http://terminal.sexy
#https://github.com/stayradiated/terminal.sexy/blob/master/lib/stores/random.js

import os
import struct as s
from colour import Color
from math import pow

def random(start, end):
    return s.unpack(">L", os.urandom(4))[0] % (end - start) + start

#order of return value:
#[bg, fg, col1, col2, ... , col16]
def generateRandomColors():

    #6 base hues
    baseHue = s.unpack(">L", os.urandom(4))[0] % 99996
    hues = [0, 16666, 33332, 49998, 66664, 83330]
    for i in range(0, len(hues)):
        hues[i] = float((hues[i] + baseHue) % 99996)/99996

    baseSat = float(random(5, 40))/100
    baseLight = float(random(0, 10))/100
    rangeLight = float(90 - baseLight)/100

    colors = {}
    
    #fg bg and cursor
    colors['background'] = Color(hsl=(hues[0], baseSat, baseLight)).get_hex_l() 
    colors['foreground'] = Color(hsl=(hues[0], baseSat, rangeLight)).get_hex_l()
    
    #8 low saturation shades
    for i in range(0, 8):
        colors['color{0}'.format(str(i))] = Color(hsl=(hues[0], baseSat, (baseLight + (rangeLight * pow(i/7, 1.5))))).get_hex_l()

    #8 random shades
    minSat = float(random(30, 70))/100
    maxSat = float(minSat + 30)/100
    minLight = float(random(50, 70))/100
    maxLight = float(minLight*100 + 20)/100

    for i in range(0, 8):
        a = random(minLight * 100, maxLight*100)/100
        colors['color{0}'.format(str(i + 8))] = Color(hsl=(hues[random(0, 5)], random(minSat * 100, maxSat * 100)/100, a)).get_hex_l()

    return colors
