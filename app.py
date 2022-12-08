from flask import Flask, render_template, request, jsonify,redirect
#from flask_ngrok import run_with_ngrok
import pickle
app = Flask(__name__)

model0 = pickle.load(open('production.pkl','rb'))
model1 = pickle.load(open('RandomForest.pkl','rb'))
model2 = pickle.load(open('state.pkl','rb'))

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/state_wise")
def state_wise():
    return render_template("state_wise.html")
@app.route("/what_grow")
def what_grow():
    return render_template("what_grow.html")
@app.route("/production")
def production():
    return render_template("production.html")

@app.route('/crop')
def predict(): 
    v1 = float(request.args.get('nitrogen'))
    v2 = float(request.args.get('potatisum'))
    v3 = float(request.args.get('calsium'))
    v4 = float(request.args.get('temperature'))
    v5 = float(request.args.get('humidity'))
    v6 = float(request.args.get('ph'))
    v7 = float(request.args.get('rainfall'))
    prediction = model1.predict([[v1,v2,v3,v4,v5,v6,v7]])
    return render_template('what_grow.html', OUTPUT= '{}'.format((prediction[0]))) 



@app.route('/produce')
def find():
    p1=int(request.args.get('state'))
    p2=int(request.args.get('crop'))
    p3=int(request.args.get('season'))
    p4=int(request.args.get('area'))
    p5=int(request.args.get('production'))
    prediction = model0.predict([[p1,p3,p2,p4,p5]])
    return render_template('production.html', OUTPUT= '{}'.format(prediction[0]))



@app.route('/state')
def best():
    s1=int(request.args.get('state'))
    prediction = model2.predict([[s1]])
    if prediction[0]==0:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Arhar/Tur"))
    if prediction[0]==1:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Coconut "))
    if prediction[0]==2:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Coriander"))
    if prediction[0]==3:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Cotton(lint)"))
    if prediction[0]==4:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Dry chillies"))
    if prediction[0]==5:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Dry ginger"))
    if prediction[0]==6:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Gram"))
    if prediction[0]==7:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Horse-gram"))
    if prediction[0]==8:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Linseed"))
    if prediction[0]==9:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Maize"))
    if prediction[0]==10:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Masoor"))
    if prediction[0]==11:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Moong(Green Gram)"))
    if prediction[0]==12:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Moth"))
    if prediction[0]==13:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Other  Rabi pulses"))
    if prediction[0]==14:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Peas & beans (Pulses)"))
    if prediction[0]==15:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Potato"))
    if prediction[0]==16:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Rice"))
    if prediction[0]==17:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Sannhamp"))
    if prediction[0]==18:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Sesamum"))
    if prediction[0]==19:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Small millets"))
    if prediction[0]==20:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Sugarcane"))
    if prediction[0]==21:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Sweet potato"))
    if prediction[0]==22:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Turmeric"))
    if prediction[0]==23:
        return render_template('state_wise.html', OUTPUT= '{}'.format("Wheat"))
    if prediction[0]==24:
        return render_template('state_wise.html', OUTPUT= '{}'.format("other oilseeds"))

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
    
    