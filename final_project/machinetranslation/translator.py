import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    '''Takes in the english text, returns the french translation'''
    french_text = ''
    if english_text != '':
        res = language_translator.translate(text=english_text, model_id='en-fr').get_result()
        french_text = res['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    '''Takes in the french text, returns the english translation'''
    english_text = ''
    if french_text != '':
        res = language_translator.translate(text=french_text, model_id='fr-en').get_result()
        english_text = res['translations'][0]['translation']
    return english_text
