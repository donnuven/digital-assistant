import PySimpleGUI as sg
import webbrowser


sg.theme('Dark Purple 6')


class twitch_user_gui:
    '''
    This is an twitch user GUI to search up any twitch user.

    '''

    def __init__(self):
        self.layout = [[sg.Text('Twitch User Search')],
                       [sg.InputText()],
                       [sg.Button('Ok'), sg.Button('Cancel')]]
        self.window = sg.Window('Twitch User Search', self.layout)

    def twitch_user_search(self):
        while True:
            event, values = self.window.read()
            if event in (None, 'Cancel'):
                break

            twitch_user = values[0]
            twitch_url = 'https://www.twitch.tv/' + twitch_user
            webbrowser.get("windows-default").open(twitch_url)


if __name__ == '__main__':
    twitch_gui = twitch_user_gui()
    twitch_gui.twitch_user_search()
