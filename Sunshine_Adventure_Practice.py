import tkinter as tk


#Windows
root = tk.Tk()
root.geometry("800x500")
root.title("Camp Info Storer")
root.resizable(False,False)
root.iconbitmap

#Button 1 (Delete)
button = tk.Button(root, text='Delete')
button.grid(row=3, column=1, padx=5, pady=5)

#Button 2(Add)
button = tk.Button(root, text='Add')
button.grid(row=3, column=2, padx=5, pady=5)

#Button 3(Display)
button = tk.Button(root, text= 'Display')
button.grid(row=3, column=3, padx=5, pady=5)

#button 4 (Continue)
button = tk.Button(root, text='Continue')
button.grid(row=3,column=4, padx=5, pady=5)


location_label = tk.Label(root, text="Group Location:")
location_label.grid(row=1,column=4)
location_entry = tk.Entry(root)
location_entry.grid(row=1, column=5)







label=tk.Label(root, text="Camp Info Storer", font=("times, 20"))
label.grid(row=1, column=10)


root.mainloop()
