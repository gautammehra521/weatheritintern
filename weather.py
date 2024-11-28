import requests, json
apikey = "b1f6442d795dd3bb1fcb94c7bdba52f7"
baseURL = "https://api.openweathermap.org/data/2.5/weather?q="
cityName = input("Enter your city")
completeURL = baseURL + cityName + "$appid=" + apikey
response = requests.get (completeURL)
data = response.json()
print(data)
print ("Current Temperature ", data ["main"] ["temp"]) 
print ("Current Temperature Feels like ", data["main"] ["feels_like"]) 
print ("Maximum Temperature ", data["main"] ["temp_max"]) 
print ("Minimum Temperature ", data["main"] ["temp_min"])
