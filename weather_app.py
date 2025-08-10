import requests
import customtkinter as ctk
from PIL import Image, ImageTk
import os
from dotenv import load_dotenv



def forget_all():
    label_thunderstorm.place_forget()
    label_showerrain.place_forget()
    label_rain.place_forget()
    label_snow.place_forget()
    label_mist.place_forget()
    label_clearsky.place_forget()
    label_fewclouds.place_forget()
    label_scatteredclouds.place_forget()
    label_brokenclouds.place_forget()

def weather_code_check(code):
    forget_all()
    if 200 <= code < 299:
        label_thunderstorm.place(x=470, y=250)
    elif (300 <= code < 399) or (520 <= code < 599):
        label_showerrain.place(x=470, y=250)
    elif 500 <= code <= 504:
        label_rain.place(x=470, y=250)
    elif (code == 511) or (600 <= code < 699):
        label_snow.place(x=470, y=250)
    elif 700 <= code < 799:
        label_mist.place(x=470, y=250)
    elif code == 800:
        label_clearsky.place(x=470, y=250)
    elif code == 801:
        label_fewclouds.place(x=470, y=250)
    elif code == 802:
        label_scatteredclouds.place(x=470, y=250)
    else:
        label_brokenclouds.place(x=470, y=250)

def on_press():
    city = City.get()
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        curr_temp = str(round((data['main']['temp'])-273)) + "°C"
        Temp.set(curr_temp)
        description = f"\n{city.capitalize()}, {data['sys']['country']}"
        description += f"\n{(data['weather'][0]['description']).capitalize()}\nCurrent Temperature: {curr_temp}"
        description += f"\nFeels Like: {str(round((data['main']['feels_like'])-273)) + '°C'}"
        description += f"\nMinimum Temperature: {str(round((data['main']['temp_min'])-273)) + '°C'}"
        description += f"\nMaximum Temperature: {str(round((data['main']['temp_max'])-273)) + '°C'}"
        description += f"\nHumidity: {str(round(data['main']['humidity'])) + '%'}"
        Desc.set(description)
        weather_code_check(data['weather'][0]['id'])
    
    else:
        Temp.set("Error!")
        Desc.set("\nPlease enter a valid city!")
        forget_all()
    
def on_enter_press(event):
    on_press()

load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

window = ctk.CTk()
window.geometry('800x600')
window.minsize(800,600)
window.maxsize(800,600)
window.title('Weather App')

City = ctk.StringVar(value='New York')
Temp = ctk.StringVar()
Desc = ctk.StringVar()

entry = ctk.CTkEntry(master=window, textvariable=City, height=50, width=300)
button = ctk.CTkButton(master=window, text="Search", command=on_press, height=50, width=50, fg_color='#4386f0')
label = ctk.CTkLabel(master=window, text='', anchor='nw', font=("Arial", 20), textvariable=Desc, height=480, width=400, fg_color='#4386f0', corner_radius=10, text_color='white', justify='left')
label2 = ctk.CTkLabel(master=window, font=("Arial", 80), textvariable=Temp, anchor="center", height=200, width=350, fg_color='#4386f0', corner_radius=10, text_color='white')

image = Image.open('assets\\cloudy.png')
image2 = Image.open('assets\\mist.png')
image3 = Image.open('assets\\sun.png')
image4 = Image.open('assets\\snowflake.png')
image5 = Image.open('assets\\clouds.png')
image6 = Image.open('assets\\cloud.png')
image7 = Image.open('assets\\raining.png')
image8 = Image.open('assets\\storm.png')
image9 = Image.open('assets\\weather.png')

image_fewclouds = ctk.CTkImage(light_image=image, size = (250, 250))
image_mist = ctk.CTkImage(light_image=image2, size = (250, 250))
image_clearsky = ctk.CTkImage(light_image=image3, size = (250, 250))
image_snow = ctk.CTkImage(light_image=image4, size = (250, 250))
image_brokenclouds = ctk.CTkImage(light_image=image5, size = (250, 250))
image_scatteredclouds = ctk.CTkImage(light_image=image6, size = (250, 250))
image_showerrain = ctk.CTkImage(light_image=image7, size = (250, 250))
image_thunderstorm = ctk.CTkImage(light_image=image8, size = (250, 250))
image_rain = ctk.CTkImage(light_image=image9, size = (250, 250))

label_fewclouds = ctk.CTkLabel(master=window, height=250, width=250, image=image_fewclouds, text="")
label_mist = ctk.CTkLabel(master=window, height=250, width=250, image=image_mist, text="")
label_clearsky = ctk.CTkLabel(master=window, height=250, width=250, image=image_clearsky, text="")
label_snow = ctk.CTkLabel(master=window, height=250, width=250, image=image_snow, text="")
label_brokenclouds = ctk.CTkLabel(master=window, height=250, width=250, image=image_brokenclouds, text="")
label_scatteredclouds = ctk.CTkLabel(master=window, height=250, width=250, image=image_scatteredclouds, text="")
label_showerrain = ctk.CTkLabel(master=window, height=250, width=250, image=image_showerrain, text="")
label_thunderstorm = ctk.CTkLabel(master=window, height=250, width=250, image=image_thunderstorm, text="")
label_rain = ctk.CTkLabel(master=window, height=250, width=250, image=image_rain, text="")

entry.place(x=10, y=10)
button.place(x=320, y=10)
label.place(x=10, y=80)
label2.place(x=430, y=10)

window.bind('<Return>', on_enter_press)

on_press()
window.mainloop()

