# import pandas as pd
import numpy as np

firstFilepath = "/mnt/files/coding/python/captions_parsing/caption_files/captions_basic_orbits_srb_eng.kdenlive.srt"
fullFilepath = "/mnt/files/coding/python/captions_parsing/caption_files/captions_basic_orbits_full.tsv"


with open(firstFilepath, 'r') as file:
    content = file.readlines()

columnsTuple = (
    'number',   #0
    'time',     #1
    'srb',      #2
    '-',        #3
    'eng',      #4
    'empty'     #5
)

contentLen = len(content)
columnsLen = len(columnsTuple)
rowsLen = contentLen//columnsLen + 1

lineNum = 0
for line in content:
    content[lineNum] = line.strip('\n')
    lineNum += 1

content.append('')
contentNP = np.array(content)
captions = contentNP.reshape(rowsLen, columnsLen)
# captionsT = captions.T

a = captions[0]
b = captions[1]

resultFile = open(fullFilepath, 'w')

for raw in range(rowsLen):
    resultData = [
        captions[raw][1], # time
        captions[raw][2], # srb
        captions[raw][4]  # eng
    ]
    resultLine = '\t'.join(resultData)
    resultFile.write(resultLine + '\n')

