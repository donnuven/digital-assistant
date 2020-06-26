import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voice_type = engine.setProperty('voices', voices[0].id)


data = {
    "chrome_path": "windows-default",
    "youtube": "https://www.youtube.com/",
    "google_search": "https://google.com/search?q=",
    "WOLFRAM_ID": "8UWWG7-TJJXUY3EWQ",
    "play_directory": "C:\\Users\\danie\\Desktop\\music-genre",
    "chat_log": "C:\\Users\\danie\\Desktop\\aris_chatlog\\chat.txt",
    "root_user": "Daniel",
    "code":
    "C:\\Users\\danie\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "username": "daniel.tsang19@gmail.com",
    "password": "dT181290",
    "shutdown": "C:\\Users\\danie\\pythonprojects\\digital_assistant\\sound_files\\shutdown.wav"
}
