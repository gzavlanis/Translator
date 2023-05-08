""" This model is using GPT-3.5 as a translator """

import openai
from configparser import ConfigParser

model_engine = "text-davinci-003"
tokens = 3100
temperature = 0.3

# take api key from .ini file
config = ConfigParser()
config.read('openai.ini')
openai.api_key = config.get('openai', 'api_key')

def regions_translator(json_strings, target_language):
    description = """
        In this session I am going to send you JSON data that will include countries and regions.
        What I want you to do, is to translate these data to the language that I will write to you in my message.
        I need the actual translation of the country name in the requested language.
    """
    translated_jsons = []
    for json_string in json_strings:
        message = f"Translate the following JSON data'{json_string}' to {target_language}. Your response will be in JSON format."
        prompt = f'\n'.join([description, message])
        response = openai.Completion.create(engine = model_engine, prompt = prompt, max_tokens = tokens, n = 1, stop = None, temperature = temperature)
        translated_jsons.append(response.choices[0].text.strip())
        print(translated_jsons)
    return translated_jsons

def competitions_translator(json_strings, target_language):
    translated_jsons = []
    for json_string in json_strings:
        description = "I will send you a JSON string with sport competitions and championships in English."
        message_1 = f"I want you to send me the phonetic transcription using the {target_language} alphabet. Your response will be in JSON format."
        message_2 = f"{json_string}"
        orders = [description, message_1, message_2]
        prompt = "\n".join(orders)
        response = openai.Completion.create(engine = model_engine, prompt = prompt, max_tokens = tokens, n = 1, stop = None, temperature = temperature)
        translated_jsons.append(response.choices[0].text.strip())
        print(translated_jsons)
    return translated_jsons

def participants_translator(json_strings, target_language):
    translated_jsons = []
    for json_string in json_strings:
        description = "I will send you a JSON string with sport Teams and athletes' names in English."
        message_1 = f"I want you to send me their Phonetic translation in {target_language}. You are allowed to send me only a JSON string without anything else."
        message_2 = f"{json_string}"
        orders = [description, message_1, message_2]
        prompt = "\n".join(orders)
        response = openai.Completion.create(engine = model_engine, prompt = prompt, max_tokens = tokens, n = 1, stop = None, temperature = temperature)
        translated_jsons.append(response.choices[0].text.strip())
        print(translated_jsons)
    return translated_jsons
