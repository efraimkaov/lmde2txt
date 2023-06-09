#!/bin/python3

import os
import argparse
from modules.lmde2txtMain import lmde2txt_func

# program arguments
installationDir = os.path.dirname(__file__)
programVersionRead = open(installationDir+'/version', 'r')
programVersion = programVersionRead.read()
programVersionRead.close()
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', action='version', version='%(prog)s '+programVersion)
parser.add_argument('-d', '--directory', help='select the full path for the input directory')
args = parser.parse_args()

directory = ''

if args.directory != None:
    directory = args.directory

guiCheck = False

lmde2txt_func(guiCheck, directory)