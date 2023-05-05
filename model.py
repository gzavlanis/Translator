""" This model is using GPT-3.5 as a translator """

import openai
from configparser import ConfigParser

description_regions = """
    In this session I am going to send you JSON data that will include countries and regions.
    What I want you to do, is to translate these data to the language that I will write to you in my message.
    I need the actual translation of the country name in the requested language.
"""
model_engine = "text-davinci-003"
tokens = 3100
temperature = 0.3

# take api key from .ini file
config = ConfigParser()
config.read('openai.ini')
openai.api_key = config.get('openai', 'api_key')

def regions_translator(json_strings, target_language):
    translated_jsons = []
    for json_string in json_strings:
        message = f"Translate the following JSON data'{json_string}' to {target_language}. Your response will be in JSON format."
        prompt = f'\n'.join([description_regions, message])
        response = openai.Completion.create(engine = model_engine, prompt = prompt, max_tokens = tokens, n = 1, stop = None, temperature = temperature)
        translated_jsons.append(response.choices[0].text.strip())
    return translated_jsons

def competitions_translator(json_strings, target_language):
    translated_jsons = []
    for json_string in json_strings:
        prompt = f"Translate these JSON data'{json_string}' to {target_language}, using the alphabetical phonetic translation system. Write only the phonetic representation of the words. Not the actual translation. Your response will be in JSON format."
        response = openai.Completion.create(engine = model_engine, prompt = prompt, max_tokens = tokens, n = 1, stop = None, temperature = temperature)
        translated_jsons.append(response.choices[0].text.strip())
        print(translated_jsons)
    return translated_jsons

def participants_translator(json_strings, target_language):
    translated_jsons = []
    for json_string in json_strings:
        prompt = f"Translate these JSON data'{json_string}' to {target_language}, using the alphabetical phonetic translation system. Write only the phonetic representation of the words. Not the actual translation. Your response will be in JSON format."
        response = openai.Completion.create(engine = model_engine, prompt = prompt, max_tokens = tokens, n = 1, stop = None, temperature = temperature)
        translated_jsons.append(response.choices[0].text.strip())
        print(translated_jsons)
    return translated_jsons
