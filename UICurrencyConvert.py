from tkinter import *
#from CurrencyConvetor import *
 
import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/e777cb6748ae2bf9355079c5/latest/USD/'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data['conversion_rates']['USD'])

# Create an empty Tkinter window
window = Tk()

# Addimg my custom logo :) 
img=PhotoImage(file='C:\Swapan\Research\PlaywithPython\Tinker Section\SwapanRoy-logo.gif')
img = img.zoom(3, 3) 
window.iconphoto(True, img)


def from_currency():
    # Get user value from input box and multiply by today's conversion rate to get INR
    rupees = round(float(e2_value.get()) * data['conversion_rates']['INR'],2)
 
    # Get user value from input box and multiply by today's conversion rate to get GBP
    pound = round(float(e2_value.get())*data['conversion_rates']['GBP'],2)
 
    # Get user value from input box and multiply by today's conversion rate to get EUR
    eur = round(float(e2_value.get())*data['conversion_rates']['EUR'],2)

    # Get user value from input box and multiply by today's conversion rate to get JPY
    jpy  = round(float(e2_value.get())*data['conversion_rates']['JPY'],2)

    # Get user value from input box and multiply by today's conversion rate to get QAR
    qar  = round(float(e2_value.get())*data['conversion_rates']['QAR'],2)
 
    # Get user value from input box and multiply by today's conversion rate to get AWD
    aed  = round(float(e2_value.get())*data['conversion_rates']['AED'],2)


    # Empty the Text boxes if they had text from the previous use and fill them again
    t1.delete("1.0", END)  # Deletes the content of the Text box from start to END
    t1.insert(END,rupees)  # Fill in the text box with the value of gram variable
    t2.delete("1.0", END)
    t2.insert(END,pound)
    t3.delete("1.0", END)
    t3.insert(END,eur)
    t4.delete("1.0", END)
    t4.insert(END,jpy)
    t5.delete("1.0", END)
    t5.insert(END,qar)
    t6.delete("1.0", END)
    t6.insert(END,aed)


def delete():
    # Deletes content from t1 Text box
    t1.delete("1.0", END)

    # Deletes content from t2 Text box
    t2.delete("1.0", END)

    # Deletes content from t3 Text box
    t3.delete("1.0", END)

    # Deletes content from t4 Text box
    t4.delete("1.0", END)

    # Deletes content from t4 Text box
    t5.delete("1.0", END)

    # Deletes content from t4 Text box
    t6.delete("1.0", END)


    # Deletes content from e2 Entry 
    e2.delete(0, END)
    


# Create a Label widget with "Kg" as label
l0 =Label(window,text="USD")
l0.grid(row=0,column=0) # The Label is placed in position 0, 0 in the window

l1 = Label(window,text="INR")
l1.grid(row=1,column=0) # The Label is placed in position 1, 0 in the window

l2 = Label(window,text="GBP")
l2.grid(row=1,column=1) # The Label is placed in position 1, 1 in the window

l3 = Label(window,text="EUR")
l3.grid(row=1,column=2) # The Label is placed in position 1, 2 in the window

l4 = Label(window,text="JPY")
l4.grid(row=1,column=3) # The Label is placed in position 1, 2 in the window

l5 = Label(window,text="QAR")
l5.grid(row=1,column=4) # The Label is placed in position 1, 2 in the window

l6 = Label(window,text="AED")
l6.grid(row=1,column=5) # The Label is placed in position 1, 2 in the window
 
e2_value=StringVar()  # Create a special StringVar object
e2 = Entry(window,textvariable=e2_value)  # Create an Entry box for users to enter the value
e2.grid(row=0,column=1)
 
# Create a button widget
# The from_currency() function is called when the button is pushed
b1 = Button(window,text="Convert",command=from_currency)
b1.grid(row=0,column=2)

# The delete function is called when the button is pushed
b2 = Button(window,text="Clear",command=delete)
b2.grid(row=0,column=3)


# Create four empty text boxes, t1, t2, t3 and t4
t1 = Text(window,height=1,width=20)
t1.grid(row=2,column=0)
 
t2 = Text(window,height=1,width=20)
t2.grid(row=2,column=1)


t3 = Text(window,height=1,width=20)
t3.grid(row=2,column=2)

t4 = Text(window,height=1,width=20)
t4.grid(row=2,column=3)

t5 = Text(window,height=1,width=20)
t5.grid(row=2,column=4)

t6 = Text(window,height=1,width=20)
t6.grid(row=2,column=5)

# Keeps connection window open
window.mainloop()


