from flask import Flask ,request,render_template
import pickle
import json
app=Flask(__name__)

#http://localhost:8090/usecase_name
@app.route("/usecase_name",methods=["GET"])
def usecase():
    return ("gpa prediction using sat score")

#http://localhost:8090/predict_gpa
#JSON
#{"sat_score":2500}
#{"gpa_grade":4.1}

@app.route("/predict_gpa",methods=["POST"])
def predict():
    request_data=request.json["sat_score"]
    pickel_m = "\saved_model\linear_reg.pkl"  #your saved model path
    with open(pickel_m, 'rb') as file:  
        load_model = pickle.load(file)
    gpa_result=load_model.predict([[request_data]])[0][0]  #[[4.1]] 
    return json.dumps({"gpa_grade":gpa_result})   # '{"gpa_grade":gpa_result}'


#http://localhost:8090/home
@app.route("/home",methods=["GET"])
def home():
    return render_template("index.html")

# #http://localhost:8090/handel_data
@app.route("/handel_data",methods=["POST"])
def handel_data():
    student_name=request.form.get("student_name")
    sat_score=float(request.form.get("sat_score"))
    pickel_m = "\saved_model\linear_reg.pkl" #your saved model path
    with open(pickel_m, 'rb') as file:  
        load_model = pickle.load(file)
    gpa_result=load_model.predict([[sat_score]])[0][0]  #[[4.1]] 
    return render_template("predict.html",gpa_result=gpa_result,student_name=student_name)

if __name__ == "__main__":
    app.run(port="8090")