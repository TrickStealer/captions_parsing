import numpy as np
from src import firstFilepath, fullFilepath, columnsLen
import functions as fn


content = fn.input_lines_from_file(firstFilepath, 1)

contentLen = len(content)
rowsLen = contentLen//columnsLen

captions = content.reshape(rowsLen, columnsLen)
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

