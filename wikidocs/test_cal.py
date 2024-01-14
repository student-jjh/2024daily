import calendar
import tkinter as tk

c = calendar.TextCalendar()

# print(help(c))
m = c.formatmonth(2021, 2)
print(m)



s = "Life is short\nUse Python"

root = tk.Tk()
t = tk.Text(root, height=10, width=30)
t.insert(tk.END, m)
t.pack()
tk.mainloop()