""" This model is using GPT-3.5 as a translator """

import openai
from configparser import ConfigParser
import numpy as np
import pandas as pd

description = """
    In this session I am going to send you data that will include countries and regions.\n
    I will also send you data that will include competitions from all over the world in common sports.\n 
    Finally, I will send you data with names from athletes and athletic teams on these sports.\n
    What I want you to do, is to translate these data from English to the language that I will write to you in my message.\n
    It is possible to be included competitions in a different language than English. In this case I want you to write the translation from the language you read in the language I ask you to.\n
    It is also possible to be included countries with the abbreviation of their names, for example 'UAE'. In this case I want you to write the full country name translated in the language I ask you to.\n
"""
model_engine = "text-davinci-003"
tokens = 1200
temperature = 0.4

# take api key from .ini file
config = ConfigParser()
config.read('openai.ini')
openai.api_key = config.get('openai', 'api_key')

def translator(text, target_language):
    prompt = f"Translate '{text}' to {target_language}"
    response = openai.Completion.create(engine = model_engine, prompt = prompt, max_tokens = tokens, n = 1, stop = None, temperature = temperature)
    return response.choices[0].text.strip() # extract translation

def engine(data, target_language):
    translations = np.array([])
    for i in data:
        translation = translator(i, target_language)
        translations = np.append(translations, translation)

    return pd.DataFrame(translations, columns = ['Region'])
