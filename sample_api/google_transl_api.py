from googletrans import Translator


def language_translator():

    translator = Translator()
    sentence = str(input('translation: '))
    lang = {
        "German": "de",
        "Russian": "ru",
        "French": "fr",
        "Mandarin": "zh-CN",
        "Korean": "ko",
        "Japanese": "ja",
        "English": "en"
    }
    translation = translator.translate(sentence, dest=lang["Japanese"])

    print(translation.origin, '-->', translation.text)


language_translator()
