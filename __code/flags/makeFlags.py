from PIL import Image
import os
import shutil
import re
import numpy as np
from multiprocessing import Pool

ideologyArray = np.array(
        ["fascism", "neutrality", "democratic", "communism" ])

class tag:
    def __init__(self, tagThis: str):
        self.tag = tagThis
        self.flags = np.array(["", "", "", ""])

    def loadFlag(self, flagDirectory: str, flagIdeology: str):
        pass


def main():
    #Get the directories
    currentDirectory = os.getcwd()
    modDirectory = os.path.dirname(os.path.dirname(currentDirectory))

    #Get a numpy array of files in flags/

    flagsArray = [f for f in os.listdir("flags") if os.path.isfile(os.path.join("flags", f))]
    tagsCount = 0
    tagsMap = {}
    tagsArray = []

    for directory in flagsArray:
        flag = directory.split(".")
        ideology = "default"
        for i in ideologyArray:
            if flag[0].endswith(i):
                ideology = i
                ideologyNameLength = (len(i) + 1) * -1
                flag[0] = flag[0][:ideologyNameLength]
                break

        #flag[0] is the tag (regular or cosmetic), ideology is the ideology
        print (flag[0], ideology)

        if flag[0] in tagsMap:
            print ("Y")
            pass
        else:
            #Create new entry into the tags array
            tagsMap[flag[0]] = tagsCount
            tagsArray.append(tag(flag[0]))
            tagsCount += 1

    pass

if __name__ == "__main__":
    main()