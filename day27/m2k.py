from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)


#Entries
entry = Entry(width=20)
#Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.grid(column=2, row=3, padx=10, pady=10)

# Label for miles
miles_txt = Label(text="miles", font=("Arial",10, "bold"))
miles_txt.grid(column=4, row=3)

# Label for equals
equals_txt = Label(text="equals to", font=("Arial",10, "bold"))
equals_txt.grid(column=3, row=6)

# Label for result
result = Label(text="0", font=("Arial",10, "bold"))
result.grid(column=4, row=6, padx=10, pady=10)

# Label for result
km_label = Label(text="Km", font=("Arial",10, "bold"))
km_label.grid(column=5, row=6, padx=10, pady=10)


def button_click():
    print("I got clicked!")
    converted_result = 1000 * int(entry.get())
    result.config(text=converted_result)




button = Button(text="Calculate", command=button_click)
button.grid(column=5, row=7, padx=10, pady=10)















window.mainloop()