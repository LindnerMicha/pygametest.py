import PySimpleGUI as sg

layout =[
    [sg.Text("Hello from PySimpleGUI")],
    [sg.Button("OK")]
]

#create the window
window = sg.Window("Demo", layout, margins=(300,300))

#create event loop
while True:
    event, values = window.read()
    #End program if user closes Window or
    #press the ok Button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()