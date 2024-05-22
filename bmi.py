from tkinter import *
window=Tk()

# add widgets here
def calculate():
    w=int(weight.get())
    h=int(height.get())/100
    bmi=w/(h*h)
    bmi=round(bmi,1)
    name=username.get()
    result_label.destroy()
    msg=""
    if bmi < 18.5:
        msg = "You are Underweight"
    elif bmi > 18.5 and bmi <= 24.9:
        msg = "You are Normal"
    elif bmi > 25 and bmi <= 29.9:
        msg = "You are Overweght"
    elif bmi > 30:
        msg = "You are Obese"
    else:
        msg="something went wrong :("
    output=Label(result_frame, text=name+", your BMI is "+str(bmi)+"and "+msg, bg = "lightcyan", font=("Calibri", 12))
    output.place(x=20, y=40)
    output.pack()

window.title('BMI Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')


app_label=Label(window, text="BMI CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

height_label=Label(window, text="Your Height (cm)", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
height_label.place(x=20, y=120)

height=Entry(window, text="", bd=2, width=22)
height.place(x=150, y=120)

weight_label=Label(window, text="Your Weight (kg)", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
weight_label.place(x=20, y=150)

weight=Entry(window, text="", bd=2, width=22)
weight.place(x=150, y=150)

btn=Button(window, text="Calculate" , fg = "black", bg = "blue", font=("Calibri", 12),bd=4, command = calculate)
btn.place(x=20, y=250)


result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()
