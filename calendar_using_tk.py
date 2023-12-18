from tkinter import *
import calendar

root = Tk()


def submit():
    newRoot = Tk()
    newRoot.title("calendar")
    newRoot.geometry("550x600")

    fetch_year = int(year.get())

    cal_content = calendar.calendar(fetch_year)
    cal_lbl = Label(newRoot, text=cal_content, font="Consolas 10 bold").grid(
        row=5, column=1, padx=20)

    newRoot.mainloop()


titl = Label(root, text="CALENDER", bg="gray", fg="white",
             font=28).grid(row=1, column=1)

labl = Label(root, text="Enter year", font=19).grid(row=2, column=1)
year = Entry(root, width=30)
year.grid(row=3, column=1, padx=20, pady=20)

btn = Button(root, text="Show calendar", bg="lightgray", command=submit).grid(
    row=4, column=1)
exit = Button(root, text="Exit", bg="lightgray", command=root.quit).grid(
    row=5, column=1)


root.mainloop()
