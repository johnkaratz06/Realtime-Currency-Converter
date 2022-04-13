from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import requests, json

root = Tk()
root.title("Realtime Currency Exchange")
root.resizable(False,False)
variable1 = StringVar(root)
variable2 = StringVar(root)
variable1.set("currency")
variable2.set("currency")
x2 = ""
pre = 1

def RealTimeCurrencyConversion():
    global base_url
    global main_url
    global variable1
    global variable2
    global x1
    global x2
    global cha
    x1 = Amount1_field.get()
    if x1=="":
        label7.config(text=">>empty field", font=("Arial",15))
    elif x1.isnumeric()==False:
        label7.config(text=">>only numbers", font=("Arial", 15))
    elif x1==x2 and cha==0:
        label7.config(text=">>same number", font=("Arial", 15))
    else:
        label7.config(text="", font=("Arial",15))
        Amount2_field.config(state="normal")
        Amount2_field.delete(0,END)
        Amount2_field.config(state="readonly")
        FromCurrency_option.config(state="disabled")
        ToCurrency_option.config(state="disabled")
        button1.config(state="disabled")
        button2.config(state="disabled")
        amount = float(Amount1_field.get())
        Amount1_field.config(state="readonly")
        root.update()
        from_currency = variable1.get()
        to_currency = variable2.get()
        api_key = "K3MQO5ISZGAYC6NI"
        base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
        main_url = base_url + "&from_currency="+from_currency+"&to_currency="+to_currency+"&apikey="+api_key #url that will give data
        print(main_url)
        req_ob = requests.get(main_url) #takes data from url
        result = req_ob.json() #turns data to json
        print(result)
        Exchange_Rate = float(result['Realtime Currency Exchange Rate']['5. Exchange Rate']) #gets specific info from json
        new_amount = round(amount*Exchange_Rate,3)
        Amount2_field.config(state="normal")
        Amount2_field.insert(0,str(new_amount))
        Amount2_field.config(state="readonly")
        FromCurrency_option.config(state="normal")
        ToCurrency_option.config(state="normal")
        Amount1_field.config(state="normal")
        button1.config(state="normal")
        button2.config(state="normal")
        x2=x1
        cha=0

def clear_all():
    Amount1_field.delete(0,END)
    Amount2_field.config(state="normal")
    Amount2_field.delete(0,END)
    Amount2_field.config(state="readonly")
    button2.config(state="disabled")
    label7.config(text="", font=("Arial",15))

def checko(*args):
    global CurrencyCode_list
    global CC
    global cha
    global pre
    cha=1
    ch1=variable1.get()
    ch2=variable2.get()
    if ch1!="currency" and ch2!="currency" and pre==1:
        button1.config(state="normal")
        pre = 0
    if ch1==ch2:
        x=CurrencyCode_list.index(ch2)+1
        if x==7:x=1
        ch2=CurrencyCode_list[x]
        variable2.set(ch2)

    if ch1=="currency": label8.config(text="")
    else:
        a = CurrencyCode_list.index(ch1)
        b = CC[a]
        label8.config(text=b)
    if ch2=="currency": label9.config(text="")
    else:
        a = CurrencyCode_list.index(ch2)
        b = CC[a]
        label9.config(text=b)

def on_closing():
    if messagebox.askokcancel("ALERT", "Do you want to quit?"):
        root.destroy()

if __name__=="__main__":
    root.geometry("400x210")
    label1 = Label(root, text="Amount:",font=("Arial",15))
    label2 = Label(root, text="From currency:",font=("Arial",15))
    label3 = Label(root,text="To currency:",font=("Arial",15))
    label4 = Label(root, text="Converted:",font=("Arial",15))
    label5 = Label(root, text="↓",font=("Arial",50))
    label6 = Label(root, text="⤷", font=("Arial", 20))
    label7 = Label(root, font=("Arial",15), foreground="red")
    label8 = Label(root, font=("Arial",10), foreground="blue")
    label9 = Label(root, font=("Arial", 10), foreground="blue")
    label1.place(x=10,y=10)
    label2.place(x=10,y=50)
    label3.place(x=10,y=90)
    label4.place(x=10,y=130)
    label5.place(x=330,y=35)
    label6.place(x=20,y=165)
    label7.place(x=230,y=167)
    label8.place(x=225,y=51)
    label9.place(x=225,y=91)
    Amount1_field = Entry(root,font=(15),justify="right")
    Amount2_field = Entry(root,font=(15),state="readonly",justify="right")
    Amount1_field.place(x=160,y=10)
    Amount2_field.place(x=160,y=130)
    CurrencyCode_list = ["","INR","USD","CAD","CNY","DKK","EUR"]
    CC = ["","Indian Rupee","US Dollar","Canadian Dollar","Chinese Yuan","Danish Krone","Euro"]
    FromCurrency_option = OptionMenu(root,variable1,*CurrencyCode_list,command=checko)
    ToCurrency_option = OptionMenu(root, variable2, *CurrencyCode_list,command=checko)
    FromCurrency_option.place(x=160,y=50)
    ToCurrency_option.place(x=160,y=90)
    button1 = Button(root, text=" ~CONVERT~ ",command=RealTimeCurrencyConversion,state="disabled")
    button1.place(x=50,y=170)
    button2 = Button(root,text=" ~CLEAR~ ",command=clear_all,state="disabled")
    button2.place(x=140,y=170)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()