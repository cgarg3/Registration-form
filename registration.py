# pip install tkinter

from tkinter import *
root = Tk()
root.geometry("500x300")

#heading
Label(root, text="Python Registration Form", font="ar 15 bold").grid(row=0, column=3)

#field name
name= Label(root, text="Name")
phone= Label(root, text="Phone")
gender= Label(root, text="Gender")
emergency= Label(root, text="Emergency")
payment-mode= Label(root, text="Payment Mode")

def getvals():
print("Accepted")

#packing fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment-mode.grid(row=5, column=2)

#variables for storing data
name-value = StringVar
phone-value = StringVar
gender-value = StringVar
emergency-value = StringVar
payment-mode-value = IntVar
check-value = IntVar

#creating entry field
nameEntry = Entry(root, textVariable=name-value)
phoneEntry = Entry(root, textVariable=phone-value)
genderEntry = Entry(root, textVariable=gender-value)
emergencyEntry = Entry(root, textVariable=emergency-value)
payment-modeEntry = Entry(root, textVariable=payment-mode-value)

#packing entry fields
nameEntry.grid(row=1, column=3)
phoneEntry.grid(row=2, column=3)
genderEntry.grid(row=3, column=3)
emergencyEntry.grid(row=4, column=3)
payment-modeEntry.grid(row=5, column=3)

#creating checkbox
checkbtn = CheckButton(text="remember me?", variable = check-value)
checkbtn.grid(row=6, column=3)

Button(text="Submit", command=getvals).grid(row=7, column=3)


root.mainloop()
