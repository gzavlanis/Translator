import pandas as pd

def importRegions(filename):
    data = pd.read_csv(f'{filename}', index_col = False, usecols = ['name'])
    return data.to_numpy()

def importCompetitions(filename):
    data = pd.read_csv(f'{filename}', index_col = False, usecols = ['name'])
    return data.to_numpy()

def importParticipants(filename):
    data = pd.read_csv(f'{filename}', index_col = False, usecols = ['name'])
    return data.to_numpy()
