from api.language_translation import LanguageTranslation
from api.text_to_speech import TextToSpeech
from api.text_insight import TextInsight


class Api:
    def __init__(self):
        self.language_translation = LanguageTranslation()
        self.text_to_speech = TextToSpeech()
        self.text_insight = TextInsight()
