from tkinter import *
from PIL import Image, ImageTk, ImageSequence
from time import sleep
import random
import pygame

window = Tk()


def animation():
    global img
    global lbl_bg
    global art_keys
    window.geometry("960x539")
    img = Image.open("gen.gif")
    play_1()
    button_st.place_forget()
    for img in ImageSequence.Iterator(img):
        img = ImageTk.PhotoImage(img)
        lbl_bg.config(image=img)
        window.update()
        sleep(0.025)
    sleep(2)
    window.geometry("1920x1080")
    lbl_bg.config(image=art_keys)
    button_st.place(relx=0.1, rely=0.6)


pygame.mixer.init()


def play_1():
    pygame.mixer.music.load("2106a8a8258c14f.mp3")
    pygame.mixer.music.play()


def play_2():
    pygame.mixer.music.load("12_-ending.mp3")
    pygame.mixer.music.play(loops=0)


window.title("Genshin impact")
c = Canvas(window, width=100, height=10)

bg = ImageTk.PhotoImage(file="image_1.png")

window.geometry("1920x1080")
art_keys = PhotoImage(file="keys.png")
c.pack()

lbl_bg = Label(window, image=bg)
lbl_bg.pack()

alph_vit = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alph_vit_bukv = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U',
                 'V', 'W', 'X', 'Y', 'Z']

alph_vit_digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def random_symb(a):
    global alph_vit_bukv
    global alph_vit_digit
    bukv_count = 0
    digit_count = 0
    for i in range(4):
        if a[i] in alph_vit_bukv:
            bukv_count += 1
        else:
            digit_count += 1
    if bukv_count == 3 and digit_count == 1:
        return True
    else:
        return False


keys_end = []
for i in range(4):
    keys = []
    for i in range(4):
        keys.append("".join(random.choices(alph_vit)))
    while random_symb(keys) == False:
        keys = []
        for i in range(4):
            keys.append("".join(random.choices(alph_vit)))
    for i in range(4):
        keys_end.append(keys[i])
    keys_end.append("-")

keys_end.pop(-1)
keys_end = "".join(keys_end)


def keys_enry():
    global keys_end
    entry = Entry(window, width=40)
    entry.place(relx=0.3, rely=0.63)
    entry.insert(3, keys_end)


def button_conf():
    button_st.configure(text="Cгенерировать ключ", command=lambda: [keys_enry(), play_2()])


button_st = Button(window, text="Запустить", fg="white", bg="cyan", font=("Arrial", 20),
                   command=lambda: [animation(), button_conf()])
button_st.place(x=700, y=380)
window.mainloop()
