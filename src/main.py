import numpy as np
from src import (firstFilepath, fullFilepath, engFilepath,
                 columnsTuple, columnsLen)
import functions as fn

MODE_TO_TSV = 0
MODE_TO_ENG = 1
MODE_TO_SRB = 2

mode = MODE_TO_ENG

content = fn.input_lines_from_file(firstFilepath, 1)
captions = fn.create_array(content, columnsLen)

if mode == MODE_TO_TSV:
    fn.write_data_to_tsv(fullFilepath, captions, [1,2,4])
elif mode == MODE_TO_ENG:
    fn.write_data_to_captions(engFilepath, captions, 4)
