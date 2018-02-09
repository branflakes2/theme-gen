from xres import genXresOut
from i3wm import geni3Out
from rand_col import generateRandomColors
from subprocess import call
import fileio

def main():
    colors = generateRandomColors()
    fileio.writeFile("/home/brian/.Xresources", genXresOut(colors))
    fileio.writeFile("/home/brian/.config/i3/config", geni3Out(colors)) 
    fileio.writeColorFile("color_out.th", colors)
    call(["xrdb", "/home/brian/.Xresources"])
    call(["i3-msg", "reload"])
main()
