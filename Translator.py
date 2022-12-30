from tkinter import ttk, messagebox
import urllib.request
from tkinter import *
import googletrans
import textblob

def is_connected():
  try:
    urllib.request.urlopen("https://www.google.com", timeout=5)
    return True
  except urllib.request.URLError:
    return False

# Window Settings

window = Tk()
window.title('Translator')
window.geometry("800x550")
window.config(background='#023050')
title_bar_image = PhotoImage(file='./Icons/TB_Icon.png')
window.iconphoto(False, title_bar_image)
window.resizable(height=False, width=False)

# Translate Function

def translate_now():
	if is_connected():
		trans_lang_text.delete(1.0, END)

		try:
			for key, value in languages.items():
				if (value == source_combo.get()):
					from_language_key = key

			for key, value in languages.items():
				if (value == trans_lang_combo.get()):
					to_language_key = key

			words = textblob.TextBlob(source_text.get(1.0, END))
			words = words.translate(from_lang=from_language_key , to=to_language_key)
			trans_lang_text.insert(1.0, words)

		except:
			messagebox.showerror("Translator", 'Not Found')
	
	else:
		messagebox.showerror("Translator", 'Please Check Your Internet Connection')

# Clear Function

def clear():
	source_text.delete(1.0, END)
	trans_lang_text.delete(1.0, END)

# Translate Languages

languages = googletrans.LANGUAGES
language_list = list(languages.values())

# Translator Lable

translator_lable = Label(window, text='TRANSLATOR', font=('Calibri', 28, 'bold'), background='#023050', foreground='White')
translator_lable.place(x=295, y=15)

# Source Text Lable

source_lable = Label(window, text='SOURCE TEXT', font=('Calibri', 20, 'bold'), background='#023050', foreground='White')
source_lable.place(x=125, y=75)

# Source ComboBox

source_combo = ttk.Combobox(window, width=50, value=language_list, font=('Calibri', 14, 'bold'))
source_combo.current(21)
source_combo.place(x=25, y=125, width=350)

# Source Text Box

source_text = Text(window, font=('Calibri', 14, 'bold'), border=0)
source_text.place(x=25, y=170, width=350, height=300)

# #-#-#-#-#

# Translate Text Lable

translang_lable = Label(window, text='TRANSLATED TEXT', font=('Calibri', 20, 'bold'), background='#023050', foreground='White')
translang_lable.place(x=500, y=75)

# Translate ComboBox

trans_lang_combo = ttk.Combobox(window, value=language_list, font=('Calibri', 14, 'bold'))
trans_lang_combo.current(8)
trans_lang_combo.place(x=425, y=125, width=350)

# Translate Text Box

trans_lang_text = Text(window,font=('Calibri', 14, 'bold'), border=0)
trans_lang_text.place(x=425, y=170, width=350, height=300)

# Buttons

btn_1 = PhotoImage(file='./Icons/BTN_1.png')
translate_button = Button(window,image=btn_1, font=('Calibri', 12, 'bold'), cursor='hand2', border=0, background='#023050' ,activebackground='#023050', command=translate_now)
translate_button.place(x=270, y=485)

btn_2 = PhotoImage(file='./Icons/BTN_2.png')
clear_button = Button(window, image=btn_2, font=('Calibri', 12, 'bold'), cursor='hand2', border=0, background='#023050' ,activebackground='#023050', command=clear)
clear_button.place(x=410, y=485)

window.mainloop()

