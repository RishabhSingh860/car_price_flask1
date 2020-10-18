from flask import Flask,render_template,request
from flask_cors import cross_origin
import numpy as np
import pickle
app=Flask(__name__)


model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict",methods=["GET","POST"])
@cross_origin()
def predict():
    ##let render value from html page to our model
    if request.method=="POST":
        Doors=int(request.form['Door'])
        Odometer=int(request.form['Odometer'])
        ## request is equual to Make
        make=request.form['make']
        if(make=="Honda"):
            Make_Honda=1
            Make_BMW=0
            Make_Toyota=0
            Make_Nissan=0
        elif(make=="Toyota"):
            Make_Honda=0
            Make_BMW=0
            Make_Toyota=1
            Make_Nissan=0
        elif(make=="Nissan"):
            Make_Honda=0
            Make_BMW=0
            Make_Toyota=0
            Make_Nissan=1
        else:
            Make_Honda=0
            Make_BMW=0
            Make_Toyota=0
            Make_Nissan=0
        color=request.form['colour']
        if(color=="White"):
            Colour_White=1
            Colour_Blue=0
            Colour_Red=0
            Colour_Green=0
            Colour_Black=0
        elif(color=="Black"):
            Colour_White=1
            Colour_Blue=0
            Colour_Red=0
            Colour_Green=0
            Colour_Black=1
        elif(color=="Blue"):
            Colour_White=0
            Colour_Blue=1
            Colour_Red=0
            Colour_Green=0
            Colour_Black=0
        elif(color=="Red"):
           Colour_White=0
           Colour_Blue=0
           Colour_Red=1
           Colour_Green=0
           Colour_Black=0
        else:
           Colour_White=0
           Colour_Blue=0
           Colour_Red=0
           Colour_Green=0
           Colour_Black=0
          
        
        prediction=model.predict([[Doors,
                                   Odometer,
                                   Colour_White,
                                   Colour_Blue,
                                   Colour_Red,
                                   Colour_Green,
                                   Make_Honda,
                                   Make_Toyota,
                                   Make_Nissan]])
        output=round(prediction[0],2)
        return render_template('home.html',prediction_text="Your car price is Rs. {}".format(output))
    return render_template('home.html')
if __name__ == "__main__":
    app.run(debug=True)
