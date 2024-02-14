 
 #||========================================================================================================================================================||
 #||                                                                                                                                                        ||
 #||                                                                                                                                                        ||
 #||                                 W   E   A   T   H   E    R                        F   O   R   E   C   A   S   T   I   N   G                            ||
 #||                                                                                                                                                        ||
 #||                                                                                                                                                        ||
 #||========================================================================================================================================================||

import streamlit as st                            #used as front end and used to create webpages
import requests                                   #allows to send HTTP requests
import datetime                                   
API_Key="3635c301ef9954aab314556148b28971"        #to call the weather APIs from the website


def find_weather(city):

    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}"        #for current weather
    data1=requests.get(url).json()                                                         #json format easy to read from humans
    #st.json(data1)                
        
   
    try:
        general=data1['weather'][0]['main']                                
        icon_id=data1['weather'][0]['icon']
        temperature=data1['main']['temp']
        humid=data1['main']['humidity']
        winds=data1['wind']['speed']
        country=data1['sys']['country']
        rise=data1['sys']['sunrise']
        sset=data1['sys']['sunset']
        
        icon=f"http://openweathermap.org/img/wn/{icon_id}@2x.png"                         #extracting icon data
    except KeyError:
       st.error("City not found")
       st.stop()
    return general,temperature,icon,humid,winds,country,rise,sset
        
    
    
    



def farh(temperature):                                                 #to convert temp to farhenheit
    f=(temperature-273.15)*9/5+32
    return round(f,2)

def cel(temperature):                                                   #to convert temp to celcius
    c=(temperature-273.15)
    return round(c,2)


def main():
    st.title("Weather Forecast")                                       
    st.write("##### Write the name of a City and select the Temperature Unit from the sidebar")
    city=st.text_input("Enter a city Name").lower()                        #taking city name as input
    degree=st.selectbox("Degree:",["Farheniet","Celcius","Kelvin"])        
    if st.button("Submit"):
        general,temperature,icon,humid,winds,country,rise,sset=find_weather(city)
        st.subheader(f"Weather Forcast for {city.upper()} ,{country}")
        date_time = datetime.datetime.fromtimestamp(rise)              #converting UTC format to date and time format
        date_time1 = datetime.datetime.fromtimestamp(sset)
        st.write(f"Sunrise 🌞: {date_time.strftime('%Y-%m-%d %H:%M:%S')} AM")
        st.write(f"Sunset 🌤: {date_time1.strftime('%Y-%m-%d %H:%M:%S')} PM")
        
        col_1,col_2,col_3,col_4=st.columns(4)                           # creating 4 columns
        if degree=="Farheniet":
            with col_1:
                st.metric(label="Temperature",value=f"{farh(temperature)}°F",delta="3°F") #delta refers to the variation
        elif degree=="Celcius":
            with col_1:
                st.metric(label="Temperature",value=f"{cel(temperature)}°C",delta="-5°C")
        else:
            with col_1:
                st.metric(label="Temperature",value=f"{temperature}K")
        with col_2:
            st.metric(label="Humidity",value=f"{humid}%",delta="-1%") #humidity

            
            
        with col_3:     
            st.metric(label="Wind Speed",value=f"{winds}Kmph",delta="1Kmph")  #wind speed    
        with col_4:
            st.write(general)    #general weather condition
            st.image(icon)
        
            
    st.write("_____________________________________________________________________________________________________")           
            
        
        
           
    
if __name__=='__main__':
    main()
