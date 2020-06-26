import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voice_type = engine.setProperty('voices', voices[0].id)


data = {
    "chrome_path": "windows-default",
    "youtube": "https://www.youtube.com/",
    "google_search": "https://google.com/search?q=",
    "WOLFRAM_ID": "WOLFRAM_ID",
    "play_directory": "path/to/your/play_directory",
    "chat_log": "path/to/your/rain_meter_skin/chat.txt",
    "root_user": "your_name",
    "code":
    "path/to/your/code_editor",
    "username": "yourusername@gmail.com",
    "password": "your_password",
    "shutdown": "path/to/your/sound_file/shutdown.wav"
}
