import spacy
import customtkinter as Ctk

def openhelp():
    help_window = Ctk.CTk()
    help_window.geometry("240x200")
    help_window.title("Help")

    txt = "This tool allows you to extract all subjects and important nouns from a string of text. This produces a string of text that is usable for data analytics."

    lbl_title = Ctk.CTkLabel(help_window,text="Instructions",font=("Arial",12,"bold"),wraplength=200)
    lbl_title.pack()

    lbl_title = Ctk.CTkLabel(help_window,text=txt,font=("Arial",10),wraplength=200,justify="left")
    lbl_title.pack()

    help_window.mainloop()

def parsetext():
    txt = txt_input.get("1.0","end")
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(txt)
    stk = []

    for w in doc:
        if w.pos_ == "NOUN" or w.pos_ == "PROPN":
            stk.append(w.text)

    lbl_result.configure(text=stk)

Ctk.set_appearance_mode("Dark")
Ctk.set_default_color_theme("blue")

root = Ctk.CTk()
root.title("Text Parser App")
root.geometry("400x600")

## Set the header.

lbl_title = Ctk.CTkLabel(root,text="Text Parser",font=("Arial",20,"bold"),anchor="w")
lbl_title.pack()

lbl_subtitle = Ctk.CTkLabel(root,text="Created with Python, Tkinter, Customtkinter",font=("Arial",9,"italic"))
lbl_subtitle.pack()

## Set the input frame.

frm_input = Ctk.CTkFrame(root)
frm_input.pack(padx=5,pady=5)

lbl_input = Ctk.CTkLabel(frm_input,text="Provide your text",font=("Arial",12),text_color="white")
lbl_input.grid(row=0,column=0,sticky="w",padx=5)

txt_input = Ctk.CTkTextbox(frm_input,width=400)
txt_input.grid(row=1,column=0,sticky="w")

btn_parse = Ctk.CTkButton(frm_input,width=400,text="Parse Text",fg_color="gray",command=parsetext)
btn_parse.grid(row=2,column=0,pady=5)

## Set the ouput frame

frm_output = Ctk.CTkFrame(root,width=400)
frm_output.pack(padx=5,pady=5)

lbl_output = Ctk.CTkLabel(frm_output,text="Output",font=("Arial",12),text_color="white",anchor="w",width=400)
lbl_output.grid(row=0,column=0,sticky="w",padx=5)

lbl_result = Ctk.CTkLabel(frm_output,text="Results will be displayed here",font=("Arial",10),width=400,height=200,wraplength=200,justify="left")
lbl_result.grid(row=1,column=0,sticky="w",padx=5)

## Set the help/instructions button.

btn_help = Ctk.CTkButton(root,text="Help",fg_color="skyblue",text_color="black",height=30,width=20,font=("Arial",10),command=openhelp)
btn_help.pack(pady=5,anchor="e",padx=5)

root.mainloop()