from tkinter import *
from tkinter import ttk
import requests

def data_get():
  city = city_name.get()
  data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=82c24ac4a14d953060569acdc691da6b").json()
  w_label1.config(text=data["weather"][0]["main"])
  wd_label1.config(text=data["weather"][0]["description"])
  t_label1.config(text="{:.2f}".format(float(data["main"]["temp"])-273.15))
  p_label1.config(text=data["main"]["pressure"])

win = Tk ()

win.title("Weather Forcaste")
win.config(bg="light blue")
win.geometry("500x570")

name_label = Label(win,text= "Weather Forcaste",
                  font=("Times New Roman",30,"bold"),)
name_label.place(x=25,y=50,height=50,width=450)


city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

#combobox(state box)

com = ttk.Combobox(win,text="Select City", values= list_name ,font=("Times New Roman",20), textvariable= city_name)
com.place(x=25,y=120,height=50,width=450)

#Forcaste (details of the weather)

w_label = Label(win,text= "Weather",
  font=("Times New Roman",15),)
w_label.place(x=25,y=260,height=50,width=210)
w_label1 = Label(win,text= "",
  font=("Times New Roman",15),)
w_label1.place(x=260,y=260,height=50,width=210)

wd_label = Label(win,text= "Weather Description",
  font=("Times New Roman",15),)
wd_label.place(x=25,y=330,height=50,width=210)
wd_label1 = Label(win,text= "",
  font=("Times New Roman",15),)
wd_label1.place(x=260,y=330,height=50,width=210)

t_label = Label(win,text= "Tempreture",
  font=("Times New Roman",15),)
t_label.place(x=25,y=400,height=50,width=210)
t_label1 = Label(win,text= "",
  font=("Times New Roman",15),)
t_label1.place(x=260,y=400,height=50,width=210)

p_label = Label(win,text= "Pressure",
  font=("Times New Roman",15),)
p_label.place(x=25,y=470,height=50,width=210)
p_label1 = Label(win,text= "",
  font=("Times New Roman",15),)
p_label1.place(x=260,y=470,height=50,width=210)

#Done button

done_button = Button(win,text="Done",font=("Times New Roman",15), command=data_get)
done_button.place(x=200,y=190,height=50,width=100)

win.mainloop()
