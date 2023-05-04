import json
import pandas as pd
import numpy as np

def converter(data_list):
    frames = []
    for data in data_list:
        dictionary = json.loads(data)
        frames.append(pd.json_normalize(dictionary)) # convert jsons to dataframes
    df = pd.DataFrame(np.concatenate([frame.values for frame in frames]), columns = frames[0].columns, axis = None) # merge to one dataframe
    print(df.transpose())
    return df.transpose()

def generator(data1_list, data2_list, data3_list, filename):
    frame_1 = converter(data1_list)
    frame_2 = converter(data2_list)
    frame_3 = converter(data3_list)

    print(frame_2)
    df = pd.concat([ frame_1, frame_2, frame_3 ], axis = 1) # put original data and translations side by side
    df.to_csv(f'{filename}', index = False, header = False, encoding = 'utf-8')
