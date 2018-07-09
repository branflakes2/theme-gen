from xres import genXresOut
from i3wm import geni3Out
from rand_col import generateRandomColors
from subprocess import call
from refresh_urxvt import refresh_urxvt
import os.path as path
import fileio

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
    print(home)
    if path.isfile(home + "/.config/theme-gen/config"):
        print("asdasdf")
        filename = home + "/.config/theme-gen/config"
    #else:
        #other config locations
    print(filename)
    if filename != "":
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        print(lines)
        for line in lines:
            if line.strip()[0] == '!' or len(line.strip()) == 0:
                continue
            split_line = line.split(':')
            key = split_line[0].strip()
            value = split_line[1].strip()
            print(key)
            print(value)
            config[key] = value
    return config

#returns true on successful load, false otherwise
def load_theme(config, theme_file):
    colors = {}
    theme_dir = config["theme_dir"]
    color_config_files = config["color_config_files"]
    if path.isfile(theme_dir + "/" + theme_file + ".th"):
        colors = fileio.readColorFile(theme_dir + "/" + theme_file + ".th")
    elif path.isfile(theme_dir + "/" + theme_file):
        colors = fileio.readColorFile(theme_dir + "/" + theme_file)
    elif path.isfile(theme_file):
        colors = fileio.readColorFile(theme_file)
    else:
        #file doesn't exist
        return False
    
    writeColorFile(config["ld_file"], colors)
    refresh(config)

def refresh(config):
    colors = fileio.readColorFile(config["ld_file"])
    if config["Xresources"] != "false":
        fileio.writeFile(config["Xresources"], genXresOut(colors))
        call(["xrdb", config["Xresources"]])
    if config["i3config"] != "false":
        fileio.writeFile(config["i3config"], geni3Out(colors))
        call(["i3-msg", "reload"])
    if config["urxvt"] == "true":
        refresh_urxvt()

def main():
    config = ld_config()
    print(config["Xresources"] + "\n" + config["i3config"])
    refresh(config)

main()
