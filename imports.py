import pandas as pd

def importRegions(filename):
    data = pd.read_csv(f'{filename}', index_col = False, usecols = ['name']) # import data from csv
    parts = [ data.loc[i:i + 10 - 1,:] for i in range(0, len(data), 10) ] # split every 10 rows
    jsons = []
    for _, frame in enumerate(parts):
        jsons.append(frame.to_json(orient = 'columns')) # convert to json and create a list of json strings
    return jsons

def importCompetitions(filename):
    data = pd.read_csv(f'{filename}', index_col = False, usecols = ['name'])
    parts = [ data.loc[i:i + 10 - 1,:] for i in range(0, len(data), 10) ]
    jsons = []
    for _, frame in enumerate(parts):
        jsons.append(frame.to_json(orient = 'columns'))
    return jsons

def importParticipants(filename):
    data = pd.read_csv(f'{filename}', index_col = False, usecols = ['name'])
    parts = [ data.loc[i:i + 10 - 1,:] for i in range(0, len(data), 10) ]
    jsons = []
    for _, frame in enumerate(parts):
        jsons.append(frame.to_json(orient = 'columns'))
    return jsons
