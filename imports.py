import pandas as pd

def importRegions(filename):
    data = pd.read_csv(f'{filename}', index_col = False, usecols = ['name'])
    parts = [ data.loc[i:i + 50 - 1,:] for i in range(0, len(data), 50) ]
    jsons = []
    for _, frame in enumerate(parts):
        jsons.append(frame.to_json(orient = 'columns'))
    return jsons

def importCompetitions(filename):
    data = pd.read_csv(f'{filename}', index_col = False, usecols = ['name'])
    parts = [ data.loc[i:i + 50 - 1,:] for i in range(0, len(data), 50) ]
    jsons = []
    for _, frame in enumerate(parts):
        jsons.append(frame.to_json(orient = 'columns'))
    return jsons

def importParticipants(filename):
    data = pd.read_csv(f'{filename}', index_col = False, usecols = ['name'])
    parts = [ data.loc[i:i + 50 - 1,:] for i in range(0, len(data), 50) ]
    jsons = []
    for _, frame in enumerate(parts):
        jsons.append(frame.to_json(orient = 'columns'))
    return jsons
