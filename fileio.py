from exception import FileFormatError
from colour import Color
from shutil import copyfile

#checks to see if the file has a ##colors## and ##end colors## statement
def checkFile(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    lineNum = 1
    colorStart = 0
    for line in lines:
        if line.strip() == "##colors##" and colorStart == 0:
            colorStart = lineNum
        elif line.strip()== "##end colors##" and colorStart > 0:
            return True
        lineNum += 1
    
    if colorStart > 0:
        raise FileFormatError("##colors## statement opened in output file at line {0} with no associated ##end colors## statement.".format(str(colorStart)))
    else:
        raise FileFormatError("No ##colors## statement in output file")

#checks the format of the color file
def checkColorFile(filename):
    return True
    #f = open(filename)
    #lines = f.readlines()
    #f.close()
    #for line in lines:
    #    stripped = line.strip()
    #    length = len(stripped)
       

#saves a backup of the file, then replaces the colors block with the given 
#colors
def writeFile(filename, color_string):
    checkFile(filename)
    copyfile(filename, filename + ".bak")
    f = open(filename, 'r+')
    lines = f.readlines()
    f.seek(0)
    f.truncate()
    cont = 0
    for line in lines:
        if cont and line.strip() != "##end colors##":
            continue
        elif cont and line.strip() == "##end colors##":
            cont = 0
        if line.strip() != "##colors##":
            f.write(line)
        else:
            f.write(line)
            f.write(color_string)
            cont = 1
    f.close()

#checks format of color file
#raises exception if values are formatted incorrectly, and if the an incorrect
#amount of semicolons are used. doesn't care about bogus keys, as they won't be
#used anyway
#needs to be implemented
def checkColorFile(filename):
    return True

def writeColorFile(filename, colors_dict):
    f = open(filename, 'w')
    f.seek(0)
    f.truncate()
    f.write("!If this is the randomly generated temp theme file, it probably shouldn't be\n!edited in place. Save it first, make your edits, then reload it.\n") 
    
    for key, value in colors_dict.items():
        f.write(key + ":\t{0}\n".format(value))
    f.close()

#I guess bogus keys could be written too, but they won't be used
#File size will be checked too (in final imp), so huge files can't be read
def readColorFile(filename):
    color_dict = {}
    if checkColorFile(filename):
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            if line.strip()[0] == '!' or len(line.strip()) == 0:
                continue
            split_line = line.split(':')
key = split_line[0].strip()
            value = split_line[1].strip()
            color_dict[key] = value
        return color_dict
    else:
        return False

