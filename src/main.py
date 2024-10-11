import pandas as pd

first_filepath = "/mnt/files/coding/python/captions_parsing/caption_files/captions_basic_orbits_srb_eng.kdenlive.srt"

file = open(first_filepath, "r")
content = file.read()

modeTuple = (
    'number',
    'time',
    'srb',
    '-',
    'eng',
    'empty'
)

modeNum = 0
modeLen = len(modeTuple)

