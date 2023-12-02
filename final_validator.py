import tkinter as tk
from tkinter import messagebox
import re
import schwifty
from tkinter import PhotoImage


def validate_card_provider():
    card_number = card_entry.get()
    color = 'green'
    if re.match(r'^4[0-2]([\d]{14}|[\d]{12})', card_number):
        result = 'Company card name: Visa Card'
    elif re.match(r'^5[1|5][\d]{14}', card_number):
        result = 'Company card name: Master Card'
    elif re.match(r'^37[0-9]{13}', card_number):
        result = 'Company card name: American Express Card'
    elif re.match(r'^56[\d]{14}', card_number):
        result = 'Company card name: Australian Bank Card'
    elif re.match(r'^3[0|8][\d]{12}', card_number):
        result = 'Company card name: Diners Club Card'
    elif re.match(r'^60[\d]{14}', card_number):
        result = 'Company card name: Discover Card'
    elif re.match(r'^35[\d]{14}', card_number):
        result = 'Company card name: JCB Card'
    else:
        color = 'red'
        result = 'Company card name: Unknown'

    card_type_result.delete(0, tk.END)
    card_type_result.insert(0, result)
    card_type_result.config(fg=color)


def validate_card_number():
    try:
        # Double every second digit from right to left
        sum_ = 0
        crd_no = card_entry.get()[::-1]
        for i in range(len(crd_no)):
            if i % 2 == 1:
                double_it = int(crd_no[i]) * 2
                sum_ += sum(map(int, str(double_it))) if len(str(double_it)) == 2 else double_it
            else:
                sum_ += int(crd_no[i])

        if sum_ != 0 and sum_ % 10 == 0:
            result = 'Valid Card'
            color = 'green'
        else:
            result = 'Invalid Card'
            color = 'red'

        validity_result.delete(0, tk.END)
        validity_result.insert(0, result)
        validity_result.config(fg=color)

    except ValueError:
        return messagebox.showerror(title='Error', message='Card can contain only numbers!')


def iban_check():
    iban = iban_entry.get()
    try:
        iban = schwifty.IBAN(iban)
        result = f'Valid IBAN with BIC: {iban.bic}'
        color = 'green'

        iban_validity_result.delete(0, tk.END)
        iban_validity_result.insert(0, result)
        iban_validity_result.config(fg=color)

    except Exception as e:
        return messagebox.showerror(title='Error', message=e)


root = tk.Tk()
root.geometry('500x350')
root.title('Bank Info Validator')
img = PhotoImage(file='icon.png')
root.iconphoto(False, img)

background_image = PhotoImage(file="background.png")  # Replace with your image file
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
background_label.image = background_image


label_instructions = tk.Label(root, text="Enter a credit card number below:", width=42, bg='yellow')
label_instructions.pack(pady=10)

card_entry = tk.Entry(root, width=50)
card_entry.pack()
card_entry.delete(0, tk.END)

button_card_type = tk.Button(root, text="Check credit card provider", width=42,
                             command=validate_card_provider)
button_card_type.pack(pady=10)

card_type_result = tk.Entry(root, width=50)
card_type_result.pack()
card_type_result.delete(0, tk.END)

button_valid_number = tk.Button(root, text="Check number validity", width=42,
                                command=validate_card_number)
button_valid_number.pack(pady=10)

validity_result = tk.Entry(root, width=50)
validity_result.pack(padx=10)
validity_result.delete(0, tk.END)

iban_label = tk.Label(root, text="Enter an IBAN below:", width=42, bg='yellow')
iban_label.pack(pady=10)

iban_entry = tk.Entry(root, width=50)
iban_entry.pack()
iban_entry.delete(0, tk.END)

button_iban_check = tk.Button(root, text="Check IBAN", width=42, command=iban_check)
button_iban_check.pack(pady=10)

iban_validity_result = tk.Entry(root, width=50)
iban_validity_result.pack(padx=10)
iban_validity_result.delete(0, tk.END)



root.mainloop()