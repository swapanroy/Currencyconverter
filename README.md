# Currencyconverter
Python code to pull live currency data 

*Concept:* 
1.	Create a space for user input ( in our case USD is the base currency that needs to be converted into other currencies)
2.	Use API to fetch data and parse it.
3.	Present the data on the UI screen. 

Below is the process that I followed 
1.	Using Python 3.9 (Latest version) -download [here](https://www.python.org/downloads/windows/)
2.	Use  tkinter library for UI (pip install tkinter )
3.	Use request library to pull data via API
4. Create buttons like “Convert” to fetch data and Clear to erase the content

#Final Output 
![When the program starts](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nwaow9b3zy2uyhpqan8x.GIF)

![When user inputs numeric value and convert button is hit](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/v05h03x96w5cx4ib2t6b.GIF)


    #Code Snippet 
    #Laying out the labels on the tkinter grid.
	  # Create a Label widget with "USD" as label
        l0 =Label(window,text="USD")
        l0.grid(row=0,column=0) # The Label is placed in 
        position 0, 0 in the window

       l1 = Label(window,text="INR")
       l1.grid(row=1,column=0) # The Label is placed in position 
       1, 0 in the window
       l2 = Label(window,text="GBP")
       l2.grid(row=1,column=1)
       1, 1 in the window

      ……

      e2 = Entry(window,textvariable=e2_value)  # Create an Entry box for users to enter  value
      e2.grid(row=0,column=1)


      # Create a button widget
      # The from_currency() function is called when the button 
       is pushed
      b1 = Button(window,text="Convert",command=from_currency)
      b1.grid(row=0,column=2)

      # The delete function is called when the button is pushed
       b2 = Button(window,text="Clear",command=delete)
       b2.grid(row=0,column=3)


       # Create four empty text boxes, t1, t2, t3 and t4 for 
       values to show up
      t1 = Text(window,height=1,width=20)
      t1.grid(row=2,column=0)

	Fetch Data via URL 
      # Where USD is the base currency you want to use
      url = 'https://v6.exchangerate-api.com/v6/KEY/latest/USD/'

      # Making our request
      response = requests.get(url)
      data = response.json()

     # Your JSON object
     print(data['conversion_rates']['USD'])

Functions 

    def from_currency():
    # Get user value from input box and multiply by today's  conversion rate to 	get INR and round it to 2 decimals
    	rupees = round(float(e2_value.get()) * 
      data['conversion_rates']['INR'],2)
 
    # Get user value from input box and multiply by today's conversion rate to get GBP
    	pound = round(float(e2_value.get())*data['conversion_rates']['GBP'],2)

    # Empty the Text boxes if they had text from the previous use and fill them again
    	t1.delete("1.0", END)  # Deletes the content of the Text 
        box from start to END

        ……
	
	def delete():
       # Deletes content from t1 Text box
      t1.delete("1.0", END)

      # Deletes content from t2 Text box
      t2.delete("1.0", END)


Updated code to include Bitcoin
![When the program starts](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tes7869le53smji0q39v.GIF)

For collaboration or suggestion, reach me on my  [LinkedIn](www.linkedin.com/in/swapanroy/) [Twitter](www.twitter.com/royswapan)


