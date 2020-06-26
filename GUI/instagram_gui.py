import PySimpleGUI as sg
import webbrowser

sg.theme('DarkPurple ')


class instagram_user_gui:
    '''
     This is an instagram GUI to search up any instagram user.

    '''

    def __init__(self):
        self.layout = [[sg.Text('Instagram User Search')],
                       [sg.InputText()],
                       [sg.Button('Ok'), sg.Button('Cancel')]]
        self.window = sg.Window('Instagram User Search', self.layout)

    def instagram_user_search(self):
        while True:
            event, values = self.window.read()
            if event in (None, 'Cancel'):
                break

            instagram_user = values[0]
            instagram_url = 'https://www.instagram.com/' + instagram_user
            webbrowser.get("windows-default").open(instagram_url)


if __name__ == '__main__':
    instagram_gui = instagram_user_gui()
    instagram_gui.instagram_user_search()
