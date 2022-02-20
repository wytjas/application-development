import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
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

def englishToFrench(englishText):
    frenchTranslation = language_translator.translate(
        text=input('Please input English'),
        model_id='en-fr').get_result()
    frenchText = frenchTranslation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    englishTranslation = language_translator.translate(
        text=input('Please input French'),
        model_id='fr-en').get_result()
    englishText = englishTranslation['translations'][0]['translation']
    return englishText
