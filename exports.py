import pandas as pd

# merge original dataframes and translation dataframes and export as CSV file
def merger(df1, df2, filename):
    # change original data from array to dataframe
    df1 = df1.transpose()
    df1 = pd.DataFrame({'name': df1[0]})
    
    # concatenate original data and translated data
    df = pd.concat([ df1, df2 ], axis = 1, ignore_index = True)
    return df.to_csv(f'{filename}', index = False, encoding = 'utf-8')
