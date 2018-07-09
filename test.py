#!/bin/python

from xres import genXresOut
from i3wm import geni3Out
from rand_col import generateRandomColors
from subprocess import call
from refresh_urxvt import refresh_urxvt
import os.path as path
import os
import fileio
import sys

#options:
#   -load [name]                |   loads theme from a file
#   -gen                        |   generate a new random theme
#   -save [name]                |   save the temp file as a new theme
#   -rename [name] [new-name]   |   rename a theme file
#   -delete [name]              |   delete a theme file

#fixed config locations in order at:
#~/.config/theme-gen/config
def ld_config():
    #defaults
    home = path.expanduser("~")
    config = {"theme_dir":home + "/.config/theme-gen/themes",\
              "ld_file":home + "/.config/theme-gen/theme.th",\
              "Xresources":"false",\
              "i3config":"false",\
              "urxvt":"false"}
    filename = ""
    if path.isfile(home + "/.config/theme-gen/config"):
        filename = home + "/.config/theme-gen/config"
    #else:
        #other config locations
    if filename != "":
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            if line.strip()[0] == '!' or len(line.strip()) == 0:
                continue
            split_line = line.split(':')
            key = split_line[0].strip()
            value = split_line[1].strip()
            config[key] = value
    return config   

#returns true on successful load, false otherwise
def load_theme(config, theme_file):
    colors = {}
    if path.exists(config["theme_dir"] + "/.unsaved"):
        i = input("Current theme is unsaved, generate anyway? (Y/n): ")
        if not (i == "y" or i == "Y"):
            print("Not generating new theme\n")
            return
    if path.exists(config["theme_dir"] + "/.unsaved"):
        os.rmdir(config["theme_dir"] + "/.unsaved")
    theme_dir = config["theme_dir"]
    if path.isfile(theme_dir + "/" + theme_file + ".th"):
        colors = fileio.readColorFile(theme_dir + "/" + theme_file + ".th")
    elif path.isfile(theme_dir + "/" + theme_file):
        colors = fileio.readColorFile(theme_dir + "/" + theme_file)
    elif path.isfile(theme_file):
        colors = fileio.readColorFile(theme_file)
    else:
        #file doesn't exist
        return False
    
    fileio.writeColorFile(config["ld_file"], colors)
    refresh(config)

def save_theme(config, theme_name):
    theme_dir = config["theme_dir"]
    colors = fileio.readColorFile(config["ld_file"])
    if path.isfile(theme_dir + "/" + theme_name + ".th"):
        i = input("Color file exists, overwrite? (Y/n):") 
        if(not (i == "y" or i == "Y")):
            return
        else:
            print("Overwriting...")
    fileio.writeColorFile(config["theme_dir"] + "/" + theme_name + ".th", colors)
    if path.exists(config["theme_dir"] + "/.unsaved"):
        os.rmdir(config["theme_dir"] + "/.unsaved")

def gen_theme(config):
    colors = generateRandomColors()
    if path.exists(config["theme_dir"] + "/.unsaved"):
        i = input("Current theme is unsaved, generate anyway? (Y/n): ")
        if not (i == "y" or i == "Y"):
            print("Not generating new theme\n")
            return
    else:
        os.mkdir(config["theme_dir"] + "/.unsaved")
    fileio.writeColorFile(config["ld_file"], colors)
    refresh(config)

def refresh(config):
    devnull = open(os.devnull, 'w')
    colors = fileio.readColorFile(config["ld_file"])
    if config["Xresources"] != "false":
        fileio.writeFile(config["Xresources"], genXresOut(colors))
        call(["xrdb", config["Xresources"]], stdout=devnull, stderr=devnull)
    if config["i3config"] != "false":
        fileio.writeFile(config["i3config"], geni3Out(colors))
        call(["i3-msg", "reload"], stdout=devnull)
    if config["urxvt"] == "true":
        refresh_urxvt()

def main():
    config = ld_config()
    if sys.argv[1] == "-load":
        load_theme(config, sys.argv[2])
    elif sys.argv[1] ==  "-gen":
        gen_theme(config)             
    elif sys.argv[1] == "-save":
        save_theme(config, sys.argv[2])
    #case "-rename":
    #    print("Not Implemented")
    #case "-delete":
    #    print("Not Implemented")
    #case "-setcolor":
    #    print("Not Implemented")
    #case "-showcolor":
    #    print("Not Implemented")
    #case "-showtheme":
    #    print("Not Implemented")
    #}

main()
