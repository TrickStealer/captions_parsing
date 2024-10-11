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