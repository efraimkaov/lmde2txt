#!/bin/python3

import os
from natsort import natsorted
from tkinter import messagebox

def lmde2txt_func(guiCheck, directory):
    if guiCheck == True and '/' not in directory:
        messagebox.showerror('Error', 'You must select a valid directory!')
    elif guiCheck == False and '/' not in directory:
        print('\033[31m'+'You must select a valid directory!'+'\033[0m')
        quit()
    # Getting the lmde files from given location
    listDirectory = natsorted(os.listdir(directory))
    lenDirectory = len(listDirectory)
    lenDirectoryCount = 0
    lmdeFilesString = ''
    while lenDirectoryCount < lenDirectory:
        if '.txt' in listDirectory[lenDirectoryCount]:
            print('\033[31m'+'txt files are not allowed in '+directory+'\033[0m')
            if guiCheck == True:
                messagebox.showerror('Error', 'txt files are not allowed in '+directory)
                return
            else:
                quit()
        if '.lmde' in listDirectory[lenDirectoryCount]:
            lmdeList = listDirectory[lenDirectoryCount]
            lmdeListName = listDirectory[lenDirectoryCount].replace('.lmde', '')
            lmdeFilesString += lmdeListName+'#&#'
        lenDirectoryCount += 1
    lmdeFilesList = list(lmdeFilesString.split('#&#'))
    lmdeFilesLen = len(lmdeFilesList) - 1
    if lmdeFilesLen < 1:
        print('\033[31m'+'No lmde files found in '+directory+'\033[0m')
        if guiCheck == True:
            messagebox.showerror('Error', 'No lmde files found in '+directory)
        else:
            quit()

    print('\033[33m'+'Converting lmde to txt'+'\033[0m')

    lmdeName = ''
    lmdeFilesLenCount = 0
    while lmdeFilesLenCount < lmdeFilesLen:
        lmdeName = lmdeFilesList[lmdeFilesLenCount]

        # Counting pages for current lmde file
        contentLmdeFilesDefaultStyle = open(directory+'/'+lmdeName+'.lmde', 'r')
        contentDefaultStyleLen = len(contentLmdeFilesDefaultStyle.readlines())
        contentLmdeFilesDefaultStyle.close()

        # Converting and copy the text from current lmde file
        defaultStyleCount = 0
        while defaultStyleCount < contentDefaultStyleLen:
            defaultStyleCountCheck = 0

            contentLmdeFilesDefaultStyle = open(directory+'/'+lmdeName+'.lmde', 'r')
            contentDefaultStyleAll = contentLmdeFilesDefaultStyle.readlines()[defaultStyleCount]
            contentDefaultStyleVar = contentDefaultStyleAll.split(' ')[0]

            contentXml = open(directory+'/'+lmdeName+'.txt', 'a')

            # Removing h1 tag
            if '#' == contentDefaultStyleVar:
                contentTag = ''
                contentTag = contentDefaultStyleAll.replace('# ', '', 1)
                boldCount = 1
                boldCountLen = contentDefaultStyleAll.count('**') + 1
                while boldCount < boldCountLen:
                    contentTag = contentTag.replace('**', '', 1)
                    boldCount += 1
                italicCount = 1
                italicCountLen = contentDefaultStyleAll.count('__') + 1
                while italicCount < italicCountLen:
                    contentTag = contentTag.replace('__', '', 1)
                    italicCount += 1
                redCount = 1
                redCountLen = contentDefaultStyleAll.count('``') + 1
                while redCount < redCountLen:
                    contentTag = contentTag.replace('``', '', 1)
                    redCount += 1
                footnoteCount = 1
                footnoteCountLen = contentDefaultStyleAll.count('[^]') + 1
                while footnoteCount < footnoteCountLen:
                    if '[^]' in contentTag:
                        footnoteText = contentTag.split('[^][(')[1].split(')]')[0]
                        contentTag = contentTag.replace('[^][('+footnoteText+')]', '', 1)
                    footnoteCount += 1
                contentXml.write(contentTag)

            # Removing h2 tag
            if '##' == contentDefaultStyleVar:
                contentTag = ''
                contentTag = contentDefaultStyleAll.replace('## ', '', 1)
                boldCount = 1
                boldCountLen = contentDefaultStyleAll.count('**') + 1
                while boldCount < boldCountLen:
                    contentTag = contentTag.replace('**', '', 1)
                    boldCount += 1
                italicCount = 1
                italicCountLen = contentDefaultStyleAll.count('__') + 1
                while italicCount < italicCountLen:
                    contentTag = contentTag.replace('__', '', 1)
                    italicCount += 1
                redCount = 1
                redCountLen = contentDefaultStyleAll.count('``') + 1
                while redCount < redCountLen:
                    contentTag = contentTag.replace('``', '', 1)
                    redCount += 1
                footnoteCount = 1
                footnoteCountLen = contentDefaultStyleAll.count('[^]') + 1
                while footnoteCount < footnoteCountLen:
                    if '[^]' in contentTag:
                        footnoteText = contentTag.split('[^][(')[1].split(')]')[0]
                        contentTag = contentTag.replace('[^][('+footnoteText+')]', '', 1)
                    footnoteCount += 1
                contentXml.write(contentTag)

            # Removing h3 tag
            if '###' == contentDefaultStyleVar:
                contentTag = ''
                contentTag = contentDefaultStyleAll.replace('### ', '', 1)
                boldCount = 1
                boldCountLen = contentDefaultStyleAll.count('**') + 1
                while boldCount < boldCountLen:
                    contentTag = contentTag.replace('**', '', 1)
                    boldCount += 1
                italicCount = 1
                italicCountLen = contentDefaultStyleAll.count('__') + 1
                while italicCount < italicCountLen:
                    contentTag = contentTag.replace('__', '', 1)
                    italicCount += 1
                redCount = 1
                redCountLen = contentDefaultStyleAll.count('``') + 1
                while redCount < redCountLen:
                    contentTag = contentTag.replace('``', '', 1)
                    redCount += 1
                footnoteCount = 1
                footnoteCountLen = contentDefaultStyleAll.count('[^]') + 1
                while footnoteCount < footnoteCountLen:
                    if '[^]' in contentTag:
                        footnoteText = contentTag.split('[^][(')[1].split(')]')[0]
                        contentTag = contentTag.replace('[^][('+footnoteText+')]', '', 1)
                    footnoteCount += 1
                contentXml.write(contentTag)

            # Removing p1 tag
            if '$' == contentDefaultStyleVar:
                contentTag = ''
                contentTag = contentDefaultStyleAll.replace('$ ', '', 1)
                boldCount = 1
                boldCountLen = contentDefaultStyleAll.count('**') + 1
                while boldCount < boldCountLen:
                    contentTag = contentTag.replace('**', '', 1)
                    boldCount += 1
                italicCount = 1
                italicCountLen = contentDefaultStyleAll.count('__') + 1
                while italicCount < italicCountLen:
                    contentTag = contentTag.replace('__', '', 1)
                    italicCount += 1
                redCount = 1
                redCountLen = contentDefaultStyleAll.count('``') + 1
                while redCount < redCountLen:
                    contentTag = contentTag.replace('``', '', 1)
                    redCount += 1
                footnoteCount = 1
                footnoteCountLen = contentDefaultStyleAll.count('[^]') + 1
                while footnoteCount < footnoteCountLen:
                    if '[^]' in contentTag:
                        footnoteText = contentTag.split('[^][(')[1].split(')]')[0]
                        contentTag = contentTag.replace('[^][('+footnoteText+')]', '', 1)
                    footnoteCount += 1
                contentXml.write(contentTag)

            # Removing p1dc tag
            if '$^' == contentDefaultStyleVar:
                contentTag = ''
                contentTag = contentDefaultStyleAll.replace('$^ ', '', 1)
                boldCount = 1
                boldCountLen = contentDefaultStyleAll.count('**') + 1
                while boldCount < boldCountLen:
                    contentTag = contentTag.replace('**', '', 1)
                    boldCount += 1
                italicCount = 1
                italicCountLen = contentDefaultStyleAll.count('__') + 1
                while italicCount < italicCountLen:
                    contentTag = contentTag.replace('__', '', 1)
                    italicCount += 1
                redCount = 1
                redCountLen = contentDefaultStyleAll.count('``') + 1
                while redCount < redCountLen:
                    contentTag = contentTag.replace('``', '', 1)
                    redCount += 1
                footnoteCount = 1
                footnoteCountLen = contentDefaultStyleAll.count('[^]') + 1
                while footnoteCount < footnoteCountLen:
                    if '[^]' in contentTag:
                        footnoteText = contentTag.split('[^][(')[1].split(')]')[0]
                        contentTag = contentTag.replace('[^][('+footnoteText+')]', '', 1)
                    footnoteCount += 1
                contentXml.write(contentTag)

            # Removing p2 tag
            if '$$' == contentDefaultStyleVar:
                contentTag = ''
                contentTag = contentDefaultStyleAll.replace('$$ ', '', 1)
                boldCount = 1
                boldCountLen = contentDefaultStyleAll.count('**') + 1
                while boldCount < boldCountLen:
                    contentTag = contentTag.replace('**', '', 1)
                    boldCount += 1
                italicCount = 1
                italicCountLen = contentDefaultStyleAll.count('__') + 1
                while italicCount < italicCountLen:
                    contentTag = contentTag.replace('__', '', 1)
                    italicCount += 1
                redCount = 1
                redCountLen = contentDefaultStyleAll.count('``') + 1
                while redCount < redCountLen:
                    contentTag = contentTag.replace('``', '', 1)
                    redCount += 1
                footnoteCount = 1
                footnoteCountLen = contentDefaultStyleAll.count('[^]') + 1
                while footnoteCount < footnoteCountLen:
                    if '[^]' in contentTag:
                        footnoteText = contentTag.split('[^][(')[1].split(')]')[0]
                        contentTag = contentTag.replace('[^][('+footnoteText+')]', '', 1)
                    footnoteCount += 1
                contentXml.write(contentTag)

            contentXml.close()
            defaultStyleCount += 1
        contentLmdeFilesDefaultStyle.close()

        lmdeFilesLenCount += 1

    # Printing All done!
    if lmdeFilesLen > 0:
        print('\033[32m'+'All done!'+'\033[0m')
        if guiCheck == True:
            messagebox.showinfo('Info', 'All done!')