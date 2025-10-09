import tkinter as tk
import random as rand
from tkinter import messagebox
import json
# ---------------------------- Function SETUP ------------------------------- #
def save_pass():
    website = entry_website.get()
    email_user = entry_email_uname.get()
    password = entry_password.get()

    if website == "":
        messagebox.showerror(message="Please Enter a Website")
        return
    if email_user == "":
        messagebox.showerror(message="Please Enter an Email/Username")
        return
    if password == "":
        messagebox.showerror(message="Please Enter a Password")
        return

    new_data = {
        website:{
            "email":email_user, 
            "password":password
        }
    }

    is_ok = messagebox.askokcancel(message="You entered: \n\nWebsite: {} \nEmail/Username: {} \nPassword: {}".format(website,email_user,password))
    if is_ok:
        try:
            with open("password_starge.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            with open("password_starge.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("password_starge.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            entry_website.delete(0, tk.END)
            entry_password.delete(0, tk.END)

def generate_pass():
    letters = ['a','b','c','d','e','f','g','h','i','j','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    symbols = ['!','#','$','%','&','(',')','*','+']
    numbers = ['0', '1','2','3','4','5','6','7','8','9']

    our_chars = []

    for i in range(4):
        our_chars.append(numbers[rand.randint(0, len(numbers)-1)])
    for i in range(4):
        our_chars.append(symbols[rand.randint(0, len(symbols)-1)])
    for i in range(4):
        our_chars.append(letters[rand.randint(0, len(letters)-1)])

    password = ""
    rand.shuffle(our_chars)
    for i in our_chars:
        password += i
    entry_password.delete(0, tk.END)
    entry_password.insert(0,password)

def search_for_pass():
    try:
        with open("password_starge.json", "r") as f:
            data = json.load(f)
            website_data = data[entry_website.get()]
    except FileNotFoundError:
        messagebox.showerror(title="No File Found", message="There are no passwords stored on this device")
    except KeyError:
        messagebox.showerror(title="Website Not Found", message="We do no have a password saved for that site")
    else:
        messagebox.showinfo(title=entry_website.get(), message="Email: {}\nPassword: {}".format(website_data["email"], website_data["password"]))

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# ---------------------------- Canvas ------------------------------- #
canvas = tk.Canvas(width=200, height=200)
lock_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# ---------------------------- Grid SETUP ------------------------------- #
label_website=tk.Label(text="Website:")
label_website.grid(column=0, row=1)

entry_website = tk.Entry()
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")
entry_website.focus() # make the cursor automatically start at this entry
# =================================================================================
search_btn = tk.Button(text="Search", command=search_for_pass)
search_btn.grid(column=2, row=1, sticky="EW")
# =================================================================================
label_email_uname = tk.Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2)

entry_email_uname = tk.Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email_uname.insert(0, "hassunaBazuna02@gmail.com")
# =================================================================================
label_password = tk.Label(text="Password:")
label_password.grid(column=0, row=3)

entry_password = tk.Entry()
entry_password.grid(column=1, row=3, sticky="EW")
# =================================================================================
generate_btn = tk.Button(text="Generate Password", command=generate_pass)
generate_btn.grid(column=2, row=3, sticky="EW")
 
add_btn = tk.Button(text="Add", width=35, command=save_pass)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")
# =================================================================================
window.mainloop()
