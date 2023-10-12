import json
from tkinter import *
from tkinter import messagebox
from password_gen import passwordGenerator
import pyperclip

# NOTE: External Module Used: Pyperclip (pip install pyperclip)

password_generator = passwordGenerator()

DEFAULT_EMAIL = "hey@moumit.in"
FONT_CONFIG = ("Inter", 10, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    password_tb.delete(0, END)
    final_pass = password_generator.generate_password()
    password_tb.insert(0, final_pass)
    pyperclip.copy(final_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_tb.get()
    email = email_tb.get()
    password = password_tb.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }  # a dictionary to pass in as information to json

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Empty String", message="Please fill all the fields"
        )
    else:
        # working with json files
        # this is how you open json files
        try:
            with open(file="data.json", mode="r") as data_file:
                # reading from json
                data = json.load(data_file)

        except (
            json.JSONDecodeError
        ):  # checking if file has something to read i.e. not empty
            # JSONDecodeError is the error thrown when the file has nothing to read from
            # basically empty json
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        except FileNotFoundError:
            with open(file="data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # updating json data
            data.update(new_data)

            # this is how we can write something
            with open("data.json", mode="w") as data_file:
                json.dump(
                    data, data_file, indent=4
                )  # data saved to data.json (data_file)
                # indent is so that it can be more readable

        website_tb.delete(0, END)
        pyperclip.copy(password)
        password_tb.delete(0, END)


# ---------------------------- READ FROM JSON ------------------------------- #


def find_data():
    req_website = website_tb.get()
    try:
        with open(file="data.json", mode="r") as data_file:
            data = json.load(data_file)

    # check if the file is empty
    except json.JSONDecodeError:
        # JSONDecodeError is the error thrown when the file has nothing to read from
        messagebox.showwarning(
            title="No Password Saved",
            message="You have not saved any passwords so far",
        )

    # check if the file is available
    except FileNotFoundError:
        messagebox.showwarning(
            title="No Password Saved",
            message="No Data File Found. You have not saved any passwords",
        )
    else:
        data_found = False
        for website_name in data:
            if req_website.lower() == website_name.lower():
                data_found = True
                user_name = data[website_name]["email"]
                password = data[website_name]["password"]
                # data found
                messagebox.showwarning(
                    title=f"{req_website}",
                    message=f"Details Found.\nWebsite: {req_website}\nUsername: {user_name}\nPassword: {password}",
                )
        if data_found == False:
            messagebox.showwarning(
                title=f"{req_website}",
                message=f"No data found for {req_website}",
            )


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=45, pady=45)

logo_img = PhotoImage(file="logo.png")
logo_canvas = Canvas(width=200, height=200)
logo_canvas.create_image(100, 100, image=logo_img)
logo_canvas.grid(column=1, row=0)

# label
website_label = Label(text="Website:", font=FONT_CONFIG)
website_label.grid(column=0, row=1, sticky="E")

email_label = Label(text="Email/Username:", font=FONT_CONFIG)
email_label.grid(column=0, row=2, sticky="E")

password_label = Label(text="Password:", font=FONT_CONFIG)
password_label.grid(column=0, row=3, sticky="E")

# text box
website_tb = Entry(width=21, font=FONT_CONFIG)
website_tb.grid(column=1, row=1, sticky="EW")
website_tb.focus()

email_tb = Entry(width=35, font=FONT_CONFIG)
email_tb.grid(column=1, row=2, columnspan=2, sticky="EW")
# default value so that the password generator is automatically filled
email_tb.insert(0, DEFAULT_EMAIL)

password_tb = Entry(width=21, font=FONT_CONFIG)
password_tb.grid(column=1, row=3, sticky="EW")

# buttons
pass_gen_button = Button(
    text="Generate Password", font=FONT_CONFIG, command=gen_password
)
pass_gen_button.grid(column=2, row=3, sticky="EW")

add_details_button = Button(
    text="Add", width=36, command=save_password, font=FONT_CONFIG
)
add_details_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(text="Search", font=FONT_CONFIG, command=find_data)
search_button.grid(column=2, row=1, sticky="EW")


window.mainloop()
