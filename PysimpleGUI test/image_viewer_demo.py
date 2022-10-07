import  PySimpleGUI as sg
import os.path

# window layout of two columns

file_list_coplum =[
    [
        sg.Text("Image viewer"),
        sg.In(size=(25,1), enable_events=True, key="-Foulder-"),
        sg.FolderBrowse()
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40,20),
            key="-File List-"                                                   # Key = referenzpunkt für späteren Code
        )
    ],
]

# for now will only show the name of the chosen file
image_viewer_colum = [
    [sg.Text("Choose an image from the list on the left: ")],
    [sg.Text(size=(40,1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

# --------- layout -------
layout = [
    [
        sg.Column(file_list_coplum),
        sg.VSeparator(),
        sg.Column(image_viewer_colum),
    ]
]

window = sg.Window("Image Viwer", layout)

# event loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # folder name was filled in, so make list of files
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            #get file of files in folder
            file_list = os.listdir(folder)
        except:
            file_list=[]
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith(".png", ".gif", ".txt")
        ]
        window["-FILE LIST-"].update(fnames)
window.close()


