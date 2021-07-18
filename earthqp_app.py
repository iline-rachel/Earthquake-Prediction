from flask import Flask, render_template, request
import pickle
import numpy as np


filename='earthquake-prediction.pkl'
model = pickle.load(open(filename, 'rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/predict', methods=['POST'])
def man():
   if request.method == 'POST':
       geolevel1=int(request.form['geo_level_1_id'])
       geolevel2=int(request.form['geo_level_2_id'])
       geolevel3=int(request.form['geo_level_3_id'])
       age=int(request.form['age'])
       areapercentage=int(request.form['area_percentage'])
       heightpercentage=int(request.form['height_percentage'])
       rooftype=request.form['roof_type']
       if(rooftype=='n'):
           rooftype=0
       elif(rooftype=='q'):
           rooftype=1
       else:
          rooftype=2
              
       groundfloortype=request.form['ground_floor_type']
       if(groundfloortype=='f'):
           groundfloortype=0
       elif(groundfloortype=='m'):
          groundfloortype=1
       elif(groundfloortype=='v'):
         groundfloortype=2
       elif(groundfloortype=='x'):
          groundfloortype=3
       else:
           groundfloortype=4
       
       adobemud=int(request.form['has_superstructure_adobe_mud'])
       mortarstone=int(request.form['has_superstructure_mud_mortar_stone'])
       stoneflag=int(request.form['has_superstructure_stone_flag'])
       cementmortarstone=int(request.form['has_superstructure_cement_mortar_stone'])
       mudmortarbrick=int(request.form['has_superstructure_mud_mortar_brick'])
       cementmortarbrick=int(request.form['has_superstructure_cement_mortar_brick'])
       timber=int(request.form['has_superstructure_timber'])
       bamboo=int(request.form['has_superstructure_bamboo'])
       rcnonengineered=int(request.form['has_superstructure_rc_non_engineered'])
       rcengineered=int(request.form['has_superstructure_rc_engineered'])
       
       arr=np.array([[geolevel1,geolevel2,geolevel3,age,areapercentage,heightpercentage,rooftype,groundfloortype,adobemud,mortarstone,stoneflag,cementmortarstone,mudmortarbrick,cementmortarbrick,timber,bamboo,rcnonengineered,rcengineered]])
       pred=model.predict(arr)
       
       return render_template('next.html',data=pred)
   

if __name__ == "__main__":
    app.run(debug=True)