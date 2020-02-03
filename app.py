from flask import Flask,jsonify,render_template,request
import requests
import json
app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():
    # reading the json file
    if request.method=='POST':
        city_name= request.form["city"]

        with open("city.list.json","r",encoding="utf-8") as cities:
            city_list=json.load(cities)

        for city in city_list:
            
       
                    if city['name']==city_name or city['name']==city_name.capitalize():
                      
                            city_id = city['id']
                            
                            # print(city_id)
                

                            url="https://api.openweathermap.org/data/2.5/forecast?id={}&APPID=****************".format(city_id)
                            data=requests.get(url).json()
                            if data:
                                    current_weather=[]
                                    
                                    
                                    
                                    description=data["list"][1]["weather"][0]["description"]
                                    icon=data["list"][1]["weather"][0]["icon"]
                                    
                                    main=data["list"][1]["weather"][0]["main"]
                                    
                                    country=data["city"]["country"]
                                    current_weather=[description,icon,main,country]

                            else:
                                print("sorry main sever down")

                        

        
    return render_template('index.html',current_weather=current_weather)

if __name__=="__main__":
    app.run(debug=True)