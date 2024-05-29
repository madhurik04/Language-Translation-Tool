from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

#MAIN CODE 
def change(text="type", src="English", dest="Hindi"):
    '''text1 = text
    src1 = src
    dest1 = dest'''
    trans = Translator()
    trans1 = trans.translate(text,src=src,dest=dest)
    return trans1.text  
    #.text - show only text form of data 
    #will be displayed instead of pronounciations

def data(): #to get the data
    s = combo_src.get() #gets source from combobox
    d = combo_dest.get() #gets dest
    mssg = Source_txt.get("1.0", END).strip()  #changed the .get
    textget = change(text=mssg, src=s, dest=d)
    dest_txt.delete("1.0", END)
    dest_txt.insert(END, textget)  #---> this function will run after clicking translate button


#DESIGN SECTION - VISUALS
root = Tk()
root.title("Language Translator")
root.geometry("500x700")
root.config(bg='white')

#Heading
lab_txt = Label(root, text="Translator", font=("Times New Roman", 30,"bold"), bg='white')
lab_txt.place(x=100,y=40, height=50, width=300)

#frame
frame = Frame(root).pack(side=BOTTOM)

#Source text label
lab_txt = Label(root, text="Source Text", font=("Times New Roman", 20,"bold"),fg='black', bg='white')
lab_txt.place(x=100,y=100, height=20, width=300)#placement


#Entering the text into textbox
Source_txt = Text(frame,font=("Times New Roman", 20,"bold"), wrap = WORD)
Source_txt.place(x=10,y=130, height=150, width=480)#placement

#List of languages
list_text = list(LANGUAGES.values())

#A box to choose the lang 
combo_src = ttk.Combobox(frame, value=list_text)
combo_src.place(x=70,y=300, height=30, width=100)#placement
combo_src.set("English")

#A button to begin the translation
button_change = Button(frame, text="Translate", relief=RAISED, command=data) #fetch data 
button_change.place(x=200,y=300,height=30,width=120)

#A box to generate the output
combo_dest = ttk.Combobox(frame, value=list_text)
combo_dest.place(x=350,y=300, height=30, width=100)#placement
combo_dest.set("English")

#Dest text heading
lab_txt = Label(root, text="Destination Text", font=("Times New Roman", 20,"bold"),fg='black', bg='white')
lab_txt.place(x=100,y=350, height=20, width=300)#placement

#Displaying text to user
dest_txt = Text(frame,font=("Times New Roman", 20,"bold"), wrap = WORD)
dest_txt.place(x=10,y=380, height=150, width=480)#placement


root.mainloop()