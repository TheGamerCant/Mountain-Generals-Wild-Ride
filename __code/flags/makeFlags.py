from PIL import Image
import os
import shutil
import re
import numpy as np
from multiprocessing import Pool

#Define ideologies here
ideologyArray = np.array(["fascism", "neutrality", "democratic", "communism"])

#Define these globally, just makes life easier

#Creates a map
ideologyMap = {}
for index, ideology in enumerate(ideologyArray):
    ideologyMap[ideology] = index

#Get the directories
currentDirectory = os.getcwd()
modDirectory = os.path.dirname(os.path.dirname(currentDirectory))

class tag:
    def __init__(self, tagThis: str, flagDirectory: str, flagIdeology: str):
        #Define a str tag and an array of ideologies, all initialised to ""
        self.tag = tagThis
        self.flags = np.full(len(ideologyArray), "", dtype="<U256")     #Max directory size of 256 characters

        self.loadFlag(flagDirectory, flagIdeology)
    
    def loadFlag(self, flagDirectory: str, flagIdeology: str):
        if flagIdeology == "default":
            for i in range(len(self.flags)):
                if self.flags[i] == "":
                    self.flags[i] = flagDirectory
        else:
            index = ideologyMap[flagIdeology]
            self.flags[index] = flagDirectory

    def printFlags(self):
        print(f"{self.tag}:")
        for index, flag in enumerate(self.flags):
            print (index, flag)

    def getTag(self) -> str:
        return self.tag

    def getDirectories(self):
        return self.flags

    def getDirectory(self, index: int):
        return self.flags[index]


def loadTags():
    #Get a numpy array of files in flags/
    flagsArray = [f for f in os.listdir("flags") if os.path.isfile(os.path.join("flags", f))]
    tagsCount = 0
    tagsMap = {}
    tagsArray = []

    for directory in flagsArray:
        flag = directory.split(".")
        ideology = "default"
        for i in ideologyArray:
            if flag[0].endswith(i):     #Need to do endswith instead of a map, ideologies might be defined with multiple underscores for example
                ideology = i
                ideologyNameLength = (len(i) + 1) * -1
                flag[0] = flag[0][:ideologyNameLength]
                break

        #flag[0] is the tag (regular or cosmetic), ideology is the ideology
        if flag[0] in tagsMap:
            index = tagsMap[flag[0]]
            tagsArray[index].loadFlag(directory, ideology)
            
        else:
            #Create new entry into the tags array
            tagsMap[flag[0]] = tagsCount
            tagsArray.append(tag(flag[0], directory, ideology))
            tagsCount += 1

    return tagsMap, tagsArray

def printFlags(tagType) -> str:
    for index, ideology in enumerate(ideologyArray):
        #Load flag and resize it so we have three Image types
        flagDirectory = os.path.join(currentDirectory, "flags", tagType.getDirectory(index))
        flagLarge = Image.open(flagDirectory).convert('RGBA')
        flagLarge = flagLarge.resize((82, 52))
        flagMedium = flagLarge.resize((41, 26))
        flagSmall = flagLarge.resize((10, 7))

        #Create strings / paths to save to
        flagNameString = tagType.getTag() + "_" + ideology + ".tga"
        flagsSaveDirectory = os.path.join(modDirectory, "gfx", "flags")

        flagLarge.save(os.path.join(flagsSaveDirectory, flagNameString), format='TGA', rle=False)
        flagMedium.save(os.path.join(flagsSaveDirectory, "medium", flagNameString), format='TGA', rle=False)
        flagSmall.save(os.path.join(flagsSaveDirectory, "small", flagNameString), format='TGA', rle=False)
        
    
    return tagType.getTag()
    

def main():
    #Get an array of tags, containing their flags
    tagsMap, tagsArray = loadTags()

    #Load flag directories
    gfxFlagsLargeDirectory = os.path.join(modDirectory, "gfx", "flags")
    gfxFlagsMediumDirectory = os.path.join(gfxFlagsLargeDirectory, "medium")
    gfxFlagsSmallDirectory = os.path.join(gfxFlagsLargeDirectory, "small")

    #Delete gfx/flags and make new empty folders
    shutil.rmtree(gfxFlagsLargeDirectory, ignore_errors=True)
    os.makedirs(gfxFlagsMediumDirectory)
    os.makedirs(gfxFlagsSmallDirectory)

    with Pool() as pool:
        results = pool.imap_unordered(printFlags, tagsArray)
        for tag in results:
            print(f"Successfully made flags for {tag}")


if __name__ == "__main__":   
    main()
