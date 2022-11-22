from tkinter import (Tk, PhotoImage, Label, Text,
StringVar, Entry, Button, Toplevel, messagebox)

import base64
import os

def main_screen():
    def reset():
        code.set("")
        text1.delete("1.0" , "end")
    
    def encrypt():
        password = code.get()
        if password == "1234":
            screen1 = Toplevel(screen)
            screen1.title("Encryption")
            screen1.geometry("500x100")
            screen1.configure(bg = "#E31C25")

            message=text1.get(1.0,"end")
            encode_message = message.encode("ascii")
            base64_bytes = base64.b64encode(encode_message)
            encrypt = base64_bytes.decode("ascii")

            Label(screen1, text = "ENCRYPT", font ="arial" , fg = "white" , bg = "#140b4c").place(x = 220 , y = 0)
            text2 = Text(screen1, font = "Robote 10", bg = "white" , relief = "groove" , wrap = 'word' , bd = 0)
            text2.place(x = 190 , y = 30 , width = 150 , height = 50)
            text2.insert("end", encrypt)

        elif password =="":
            messagebox.showerror("Encryption", "Password is Empty, please input Password")
        elif password != "1234":
            messagebox.showerror("Ecryption", "Invalid Password! Try Again")

    def decrypt():
        password = code.get()
        if password == "1234":
            screen2 = Toplevel(screen)
            screen2.title("Decryption")
            screen2.geometry("500x100")
            screen2.configure(bg = "#98FB98")

            message=text1.get(1.0,"end")
            decode_message = message.encode("ascii")
            base64_bytes = base64.b64decode(decode_message)
            decrypt = base64_bytes.decode("ascii")

            Label(screen2, text = "DECRYPT", font ="arial" , fg = "white" , bg = "#98FB98").place(x = 220 , y = 0)
            text2 = Text(screen2, font = "Robote 10", bg = "white" , relief = "groove" , wrap = 'word' , bd = 0)
            text2.place(x = 190 , y = 30 , width = 150 , height = 50)
            text2.insert("end", decrypt)


    screen = Tk()
    screen.geometry("375x398")

    #icon
    image_icon = PhotoImage( file = "./padlock.png" )
    screen.iconphoto(False, image_icon) 

    #title
    screen.title("PctApp")
    
    # Text Box to enter text encryption
    Label_EnterEncryption = Label(text = "Enter text for encryption and decryption" , fg= "black" , font = ("calibri, 13"))
    Label_EnterEncryption.place(x=10,y=10)
    text1 = Text(font = "Robote 20", bg="white" , relief = "groove", wrap = "word", bd = 0)
    text1.place(x = 10, y = 50, width = 355, height=100)

    # textbox to enter key encryption
    Label_EnterKeyEncryption = Label(text = "Enter secret key encryption and decription" , fg = "black" , font = ("calibri",13))
    Label_EnterKeyEncryption.place(x = 10, y = 170)

    code = StringVar()
    entry = Entry(textvariable = code, width = 19, bd = 0, show = "*", font = ("arial", 25))
    entry.place(x = 10 , y = 200)

    # Encrypt and Decrypt Buttons
    Button(text = "ENCRYPT",  height = 2 , width = 23 , bg = '#140b4c' , fg = "white" ,bd = 0, command= encrypt).place(x = 10 , y = 250)
    Button(text = "DENCRYPT", height = 2 , width = 23 , bg = '#8372f6' , fg = "white" ,bd = 0, command= decrypt).place(x = 200 , y = 250)
    Button(text = "RESET", height = 2 , width = 50, bg = "#8F1600" , fg = "white" , bd = 0 , command=reset).place(x = 10 , y = 300 )


    screen.mainloop()

main_screen()

