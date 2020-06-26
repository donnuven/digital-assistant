import pyttsx3
import speech_recognition as sr
import wikipedia
import urllib.parse
import re
import urllib.request
import yfinance as yf
import pyfiglet
import sys
import wolframalpha
import webbrowser
import os
import smtplib
import time
import datetime
import random
import subprocess
import pyautogui as pyg
from pyfiglet import Figlet
from termcolor import colored, cprint
from googletrans import Translator
from playsound import playsound
from assistant import *
from config import *


client = wolframalpha.Client(data['WOLFRAM_ID'])


def on_startup_sound():
    interface_sound = 'path/to/your/digital_assistant/sound_file/interface.wav'
    playsound(interface_sound)


def on_startup_print():
    assistant_writer = AssistantWriter(data['chat_log'])
    custom_fig = Figlet(font='smkeyboard')
    application_name = custom_fig.renderText("EMMA")
    color_font = 'cyan'
    iteration = "v.0.1.0 - Extension Management Machine Assistant -Home Operation System"
    on_queue = "Initializing...I have been uploaded."
    introductions = [application_name + '\n' + iteration + '\n' + on_queue]
    for introduction in introductions:
        cprint(introduction, color_font)
    with assistant_writer.open_file() as file:
        for introduction in introductions:
            file.write(introduction)


class EMMA:
    def __init__(self):
        self.color_text = color_text = "cyan"
        self.engine = engine
        self.voices = voices
        self.voice_type = voice_type

    def speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def greetings(self):
        time = datetime.datetime.now().hour

        if time >= 0 and time < 12:
            EMMA.speech("Good morning" + data['root_user'])
        elif time >= 12 and time < 17:
            EMMA.speech("Good afternoon" + data['root_user'])
        else:
            EMMA.speech("Good evening" + data['root_user'])

        EMMA.speech("I am EMMA, how may I help you?")

    def send_email(self, to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(data['username'], data['password'])
        server.sendemail(data['username'], to, content)
        server.close()

    def editor_helper(self):
        pyg.hotkey('ctrl', 'a')
        time.sleep(0.1)
        pyg.hotkey('ctrl', 'c')
        time.sleep(0.1)
        pyg.press('end')

    def set_data(self):
        time.sleep(0.1)
        pyg.hotkey('ctrl', 'v')

    def close_tab(self):
        pyg.hotkey('ctrl', 'w')

    def command_protocol(self):
        recognize = sr.Recognizer()
        with sr.Microphone() as source:
            cprint("Listening now...", self.color_text)
            audio = recognize.listen(source)
            recognize.adjust_for_ambient_noise(source, duration=1)
        try:
            cprint("Recognizing...", self.color_text)
            query = recognize.recognize_google(audio, language='en-gb')
            cprint(f"user said: {query}\n", self.color_text)
        except sr.UnknownValueError as e:
            EMMA.speech("Can you please repeat that?")
            query = str(input('input: '))
        return query

    def inquiry_tree(self):
        query = EMMA.command_protocol()
        assistant_writer = AssistantWriter(data['chat_log'])

        if 'open' in query.lower():
            key_site = query.lower().split(" ")[-1]
            new_url = 'https://' + key_site + '.com'
            EMMA.speech(f'Of course sir, opening up {key_site}')
            webbrowser.get(data['chrome_path']).open(new_url)
            with assistant_writer.open_file() as file:
                file.write(f'Of course sir, opening up {key_site}')

        elif 'translate this in' in query.lower():
            translator = Translator()
            lang = query.lower().split("in")[-1].strip()
            lang_choice = {
                "french": "fr",
                "german": "de",
                "spanish": "es",
                "portuguese": "pt",
                "english": "en"
            }
            language = lang_choice[lang]
            sentence = str(input('translation: '))
            translation = translator.translate(sentence, dest=language)
            EMMA.speech(
                f'Translation complete, here is something to say:{translation.text}'
                + '\n'
                f'Original translation came from:{translation.origin}')
            with assistant_writer.open_file() as file:
                file.write(
                    f'Translation complete, here is something to say: {translation.text}'
                    + '\n'
                    f'Original translation came from:{translation.origin}')

        elif 'view subreddit' in query.lower():
            sub_url = query.lower().split("subreddit")[-1].strip()
            new_sub_url = 'https://www.reddit.com/r/' + sub_url
            EMMA.speech(f'Opening subreddit of {sub_url}')
            webbrowser.get(data['chrome_path']).open(new_sub_url)
            with assistant_writer.open_file() as file:
                file.write(f'Opening subreddit of {sub_url}')

        elif 'hello' in query.lower() or 'hey' in query.lower():
            greetings = [
                f'Hello.', f'Hey.', f'Greetings.', f'How are you doing?'
            ]
            greeting = greetings[random.randint(0, len(greetings)) - 1]
            EMMA.speech(greeting)
            with assistant_writer.open_file() as file:
                file.write(greeting)

        elif 'youtube' in query.lower():
            video = query.lower().split("me")[-1]
            video_query = urllib.parse.urlencode({"search_query": video})
            result = urllib.request.urlopen(
                "https://www.youtube.com/results?" + video_query)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})',
                                        result.read().decode())
            youtube_url = "https://www.youtube.com/watch?v=" + \
                search_results[0]
            EMMA.speech("Here is your song, sir.")
            with assistant_writer.open_file() as file:
                file.write("Here is your song, sir.")
            webbrowser.get(data['chrome_path']).open(youtube_url)

        elif 'google map' in query.lower():
            location = query.lower().split("me")[-1]
            google_map_url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get(data['chrome_path']).open(google_map_url)
            EMMA.speech(f'Here is the location of {location}')

        elif 'can you send me an email' in query.lower():
            try:
                EMMA.speech("What should I say?")
                content = EMMA.command_protocol()
                to = str(input('recipient: '))
                send_email(to, content)
                EMMA.speech("Email has been sent successfully.")
            except Exception as e:
                cprint(e, self.color_text)

        elif 'copy this' in query.lower():
            EMMA.speech("Editor mode enabled.")
            EMMA.editor_helper()
            with assistant_writer.open_file() as file:
                file.write("Editor mode enabled.")
        elif 'notepad' in query.lower():
            EMMA.speech("Opening up a text file.")
            text_editor = 'C:\\WINDOWS\\system32\\notepad.exe'
            os.startfile(text_editor)

        elif 'set this' in query.lower():
            EMMA.speech("All right, sir.")
            EMMA.set_data()
            with assistant_writer.open_file() as file:
                file.writer("All right, sir.")

        elif 'set up a new environment' in query.lower():
            os.startfile(data['code'])
            EMMA.speech("Starting a new project, sir?")
            with assistant_writer.open_file() as file:
                file.write("Starting a new project, sir?")

        elif 'instagram' in query.lower():
            instagram_url = [
                "python", "GUI/instagram_gui.py"]
            subprocess.call(instagram_url)
            EMMA.speech('Ok sir, here is an instagram profile')

        elif 'twitch' in query.lower():
            twitch_url = ["python", "GUI/twitch_gui.py"]
            subprocess.call(twitch_url)
            EMMA.speech("Here is something to watch, sir.")

        elif 'close tab' in query.lower():
            EMMA.speech("No problem sir, closing tab.")
            EMMA.close_tab()
            with assistant_writer.open_file() as file:
                file.write("No problem sir, closing tab.")

        elif 'play some music' in query.lower():
            EMMA.speech("Presenting some good vibes...")
            songs = os.listdir(data['play_directory'])
            os.startfile(os.path.join(data['play_directory'], songs[2]))

        elif "price of" in query.lower():
            stock = str(input("stock input:"))
            stock = yf.Ticker(stock)
            price = stock.info["regularMarketPrice"]
            EMMA.speech(
                f'The current price is :{price}{stock.info["currency"]}')
            with assistant_writer.open_file() as file:
                file.write(
                    f'The current price is :{price}{stock.info["currency"]}')

        elif 'later' in query.lower() or 'bye' in query.lower(
        ) or 'quit' in query.lower():
            goodbyes = [
                f'Going offline.', f'Enjoy yourself.', f'You have a good one.'
            ]
            goodbye = goodbyes[random.randint(0, len(goodbyes)) - 1]
            EMMA.speech(goodbye)
            playsound(data['shutdown'])
            with assistant_writer.open_file() as file:
                file.write(goodbye)
            sys.exit()
        else:
            EMMA.speech(
                'Initializing search...I will get back to you on that.')
            try:
                try:
                    res = client.query(query)
                    wolfram_result = next(res.results).text
                    EMMA.speech(
                        f'According to what the WOLFRAM database states - {wolfram_result}'
                    )
                    print("wolfram results: ", wolfram_result)
                    with assistant_writer.open_file() as file:
                        file.write(
                            f'According to what the WOLFRAM database states- {wolfram_result}'
                        )

                except:
                    wikipedia_result = wikipedia.summary(query, sentences=2)
                    EMMA.speech(
                        f'According to what wikipedia states -{wikipedia_result}'
                    )
                    print("wikipedia results: ", wikipedia_result)
                    with assistant_writer.open_file() as file:
                        file.write(
                            f'According to what wikipedia states- {wikipedia_result}'
                        )

            except:
                EMMA.speech('Here is what I found for ' + query)
                webbrowser.open(data['google_search'] + query)


if __name__ == '__main__':
    on_startup_sound()
    on_startup_print()
    EMMA = EMMA()
    EMMA.speech("Initializing... I have indeed been uploaded.")
    EMMA.greetings()

    while True:
        EMMA.inquiry_tree()
