""" This model is using GPT-3.5 as a translator """

import openai
from configparser import ConfigParser

description = """
    In this session I am going to send you JSON data that will include countries and regions.
    I will also send you JSON data that will include competitions from all over the world in common sports.
    Finally, I will send you JSON data with names from athletes and athletic teams for these sports.
    All the data that I will send to you from now on will concern countries, regions, athletic teams, athletes, sports and sport competitions.
    What I want you to do, is to translate these data to the language that I will write to you in my message.
    If the data you take include competitions and athletes or teams from all over the world, make the phonetic translation of them.
    Use the alphabet of the asked language to rewrite the data if includes competitions, sport teams or athletes' names.
    For countries and regions use the accurate translation in the language I write in my message.
    For example if I send you a competition like 'Primera Division' the translation will be 'Πριμέρα Ντιβιζιόν' if the asked translation language was Greek.
    Use the same logic for each language that you will be asked to translate.
    Be careful with the translation of countries and regions when the name contains only a country name.
    I need the actual translation of the country name in the requested language.
"""

model_engine = "text-davinci-003"
tokens = 3100
temperature = 0.4

# take api key from .ini file
config = ConfigParser()
config.read('openai.ini')
openai.api_key = config.get('openai', 'api_key')

def translator(json_strings, target_language):
    conversation = openai.Completion.create(engine = model_engine, prompt = description, max_tokens = tokens, n = 1, stop = None, temperature = temperature)
    print(conversation.choices[0].text.strip())

    translated_jsons = []
    for json_string in json_strings:
        prompt = f"Translate the following JSON data'{json_string}' to {target_language}. Your response will be in JSON format."
        response = openai.Completion.create(engine = model_engine, prompt = prompt, max_tokens = tokens, n = 1, stop = None, temperature = temperature)
        translated_jsons.append(response.choices[0].text.strip())
    return translated_jsons
