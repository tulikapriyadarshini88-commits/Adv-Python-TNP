from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Student Form")
root.iconbitmap("pixel2.ico")

root.geometry('500x500+0+0')
root.configure(background="#004E70")

# image
img = Image.open('star.png')
resize_img = img.resize((100,70))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root,image = img)
img_label.pack(pady=10,padx=20)

# text label
text_label = Label(root,text="Giet Bucks",font=('Arial', 18,'bold'),bg="#004B70",fg='white')
text_label.pack(pady=10,padx=20)

email_label = Label(root,text="Email",font=('Arial', 18,'bold'),bg="#701600",fg='white')
email_label.pack(pady=(20,5))

email_entry = Entry(root,font=('Arial', 18,'bold'),fg='white',bg='grey')
email_entry.pack(pady=(5,10))

password_label = Label(root,text="Password",font=('Arial', 18,'bold'),bg="#610070",fg='white')
password_label.pack(pady=(20,5))

password_entry = Entry(root,font=('Arial', 18,'bold'),fg='white',bg='grey')
password_entry.pack(pady=(5,10))

login_btn = Button(root,text="Login",font=('Arial', 18,'bold'),bg='#00704A',fg='white')
login_btn.pack(pady=(5,10))

root.mainloop()