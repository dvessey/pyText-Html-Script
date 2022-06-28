#!/usr/bin/python3
import re
import sys

inputArgs = sys.argv[1:]
pathToFile = inputArgs[1]
htmlFileName = inputArgs[2]

patternHeader = re.compile("[A-Z ]+")
patternList = re.compile("^-")

myLines = []
isFirstHeader = True
isFirstListItem = True

needul = 1
hasli = 0 # since we are in a loop in patternList.search(element) we need a flag to to print the closing </ul> tag only once


with open(pathToFile, 'r') as fileToConvert:
    with open(htmlFileName, "w") as convertedHtml:
        convertedHtml.write("<pre>")
        for myLine in fileToConvert:
            myLines.append(myLine.strip())
        for element in myLines:
            if not element.strip():
                continue

            if patternHeader.fullmatch(element): # patternHeader = re.compile("[A-Z ]+") fullmatch checks the entire line of the file is uppercase letters
                if isFirstHeader:
                    convertedHtml.write('<h1>' + element + '</h1>\n')
                    convertedHtml.write('<p>\n')
                    isFirstHeader = False
                else:
                    convertedHtml.write('</p>\n')
                    convertedHtml.write('<h1>' + element + '</h1>\n')
                    convertedHtml.write('<p>\n')

            elif patternList.search(element):
                hasli = 1
                if needul:
                    convertedHtml.write("<ul>\n")

                convertedHtml.write("<li>" + element.strip().replace('-', "") + "</li>\n")
                needul = 0

            else:
                needul = 1
                if hasli == 1:
                    convertedHtml.write("</ul>\n")
                    hasli = 0
                convertedHtml.write(element + "\n")

        convertedHtml.write('</p>\n')
        convertedHtml.write('</pre>')
