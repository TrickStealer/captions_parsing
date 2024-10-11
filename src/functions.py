import numpy as np

def input_lines_from_file(filepath, appendNum):
    with open(filepath, 'r') as file:
        content = file.readlines()

    lineNum = 0
    for line in content:
        content[lineNum] = line.strip('\n')
        lineNum += 1

    for i in range(appendNum):
        content.append('')

    return np.array(content)

def create_array(content, columns):
    contentLen = len(content)
    rowsLen = contentLen // columns
    return content.reshape(rowsLen, columns)


def write_data_to_tsv(filepath, array, columns):
    file = open(filepath, 'w')
    rowsLen = array.shape[0]

    for raw in range(rowsLen):
        resultData = []
        for col in columns:
            resultData.append(array[raw][col])

        resultLine = '\t'.join(resultData)
        file.write(resultLine + '\n')

def write_data_to_captions(filepath, array, column):
    file = open(filepath, 'w')
    rowsLen = array.shape[0]

    num = 1
    for raw in range(rowsLen):
        file.write(str(num) + '\n')
        num += 1

        file.write(array[raw][1] + '\n')
        file.write(array[raw][column] + '\n\n')
