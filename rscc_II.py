from tkinter import *

root = Tk()
root.title('RSCC PROJ II')
root.geometry("400x400")


def selected(event):
    # myLabel = Label(root, text=clicked.get()).pack()
    if clicked.get() == 'Micheal':
        Label(root, text="Name: Micheal Owusu Adjei"
                         "Workplace: RSCC"
                         "Role: NSS").pack()
    else:
        Label(root, text=clicked.get()).pack()

    if clicked.get() == 'Israel':
        Label(root, text="Name: Israel Sarpong-Adu"
                         "Workplace: RSCC"
                         "Role: NSS").pack()
    else:
        Label(root, text=clicked.get()).pack()

    if clicked.get() == 'Nusrat':
        Label(root, text="Name: Nusrat Hameed Eshun"
                         "Workplace: RSCC"
                         "Role: NSS").pack()
    else:
        Label(root, text=clicked.get()).pack()

    if clicked.get() == 'Kweku':
        Label(root, text="Name: Fidelis Kweku Afful"
                         "Workplace: RSCC"
                         "Role: NSS").pack()
    else:
        Label(root, text=clicked.get()).pack()


options = [
    "Micheal",
    "Israel",
    "Kweku",
    "Nusrat",
]
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack(pady=20)

# myButton = Button(root, text="select from list", command=selected)
# myButton.pack()

root.mainloop()
