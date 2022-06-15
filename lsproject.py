from cProfile import label
from tkinter import *

everyfood = (
    "Pasta",25,"\n",
    "French Fries",9,"\n",
    "Ice Cream",5,"\n",
    "Bread",5,"\n",
    "Fried Rice",10,"\n",
    "Pancakes",15,"\n",
    "Burger",10,"\n",
    "Pizza",25,"\n",
    "Pumpkin Pie",20,"\n",
    "Chicken Pot Pie",15,"\n",
    "Banana",3,"\n",
    "Apple Pie",15,"\n",
    "Bagel",5,"\n",
    "Muffin",2,"\n",
    "Alfredo Sauce",7,"\n",
    "Ice Cream Cake",30,"\n",
    "Cheese cake",30,"\n",
    "cheese",5,"\n",
    "Banana Bread",7,"\n",
    "Potato Chips",3,"\n",
    "Cheetos",5,"\n",
    "Doritos",5,"\n",
    "Tacos",10,"\n",
    "Burritos",7,"\n",
    "Salsa",9,"\n",
    "Marinara Sauce",15,"\n",
    "Broccoli",2,"\n",
    "Chocolate Covered Strawberries",5,"\n",
    "Kiwi",6,"\n",
    "Tomato",3,"\n",
    "Salad",24,"\n",
    "Steak",20,"\n",
    "Chicken Tenders",10,"\n",
    "Grilled Chicken",15,"\n",
    "Ribs",9,"\n",
    "Biscuts and Gravy",8,"\n",
    "Hot dogs",6,"\n",
    "Fried Chicken",10,"\n",
    "Roasted Chicken and Garlic",30,"\n",
    "Eggs",20,"\n",
    "Bacon",10,"\n",
    "Sausage",9,"\n",
    "Mashed Potatoes",10,"\n",
    "Brownies",5,"\n",
    "Cookies",5,"\n",
    "Donuts",3,"\n",
    "Turkey",8,"\n",
    "Chicken",20,"\n",
    "Mac and Cheese",9,"\n"
)
root = Tk()
print(len(everyfood))
def OptionsMenu():
    optionmen = Toplevel()
    # optionmen.geometry("800x500")
    scrollbar = Scrollbar(optionmen)
    scrollbar.pack( side = RIGHT, fill = Y )

    mylist = Listbox(optionmen, yscrollcommand = scrollbar.set )
    for line in range(147):
        mylist.insert(END, everyfood[line])

    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
        
    optionmen.mainloop()
def page5():
    pg5 = Toplevel()
    Label(pg5,text="Barter Trade Checker",font=("Helvetica","20","bold")).pack()
    Frame1 = Frame(pg5)
    for i in range(0,len(everyfood),3):
        cfood = everyfood[i]
        if Etr1.get() == cfood:
            Ist = everyfood[i+1]
        if Etr2.get() == cfood:
            Tst = everyfood[i+1]
    if Ist == Tst:
        Label(pg5,text="Fair Trade").pack()
    elif Ist < Tst:
        Label(pg5,text="Good Trade").pack()
    elif Ist > Tst:
        Label(pg5,text="Bad Trade").pack()
            

    pg5.geometry("800x500")
    

    pg5.mainloop()
def page4():
    global Etr4
    pg4 = Toplevel()
    
    pg4.geometry("800x500")
    Label(pg4,text="Barter Trade Checker",font=("Helvetica","20","bold")).pack()
    Label(pg4,text="Enter how hard it is to get what you are getting(1-10)").pack()

    Etr4 = Entry(pg4)
    Etr4.pack()
    Button(pg4,text="Submit",command=page5).pack()
    pg4.mainloop()
def page3():
    pg3 = Toplevel()
    global Etr3
    pg3.geometry("800x500")
    Label(pg3,text="Barter Trade Checker",font=("Helvetica","20","bold")).pack()
    Label(pg3,text="Enter how hard it is to get what you are giving(1-10)").pack()

    Etr3 = Entry(pg3)
    Etr3.pack()
    Button(pg3,text="Submit",command=page4).pack()
    pg3.mainloop()
def page2():
    global pg2
    global Etr2
    pg2 = Toplevel()
    pg2.geometry("800x500")
    Label(pg2,text="Barter Trade Checker",font=("Helvetica","20","bold")).pack()
    Label(pg2,text="Enter the item you are getting").pack()

    Etr2 = Entry(pg2)
    Etr2.pack()
    Button(pg2,text="Submit",command=page5).pack()

    pg2.mainloop()

root.geometry("800x500")

Label(root,text="Barter Trade Checker",font=("Helvetica","20","bold")).pack()
Label(root,text="Enter the item you are giving").pack()

Etr1 = Entry(root)
Etr1.pack()
Button(root,text="Submit",command=page2).pack()
Button(root,text="Show Options",command=OptionsMenu).pack()
root.mainloop()