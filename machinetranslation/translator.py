"""
    Translator module
"""

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.api_exception import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(
    'API_KEY'
)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'API_URL'
)

def englishtofrench(sentence):
    """
    Returns the translation from english to french of a given sentence
    """
    try:
        translation = language_translator.translate(
            text=sentence,
            model_id='en-fr'
        ).get_result()['translations'][0]['translation']

        return translation
    except (ApiException, ValueError):
        return ""

def englishtogerman(sentence):
    """
    Returns the translation from english to german of a given sentence
    """
    try:
        translation = language_translator.translate(
            text=sentence,
            model_id='en-de'
        ).get_result()['translations'][0]['translation']

        return translation
    except (ApiException, ValueError):
        return ""
