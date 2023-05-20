from flask import Flask, render_template,jsonify
app=Flask(__name__)

JOBS=[
  {'id':1,'title':'Data Analyst','location':'Madrid','salary':'30.000 EUR'},
  {'id':2,'title':'Front End Engineer','location':'Madrid','salary':'35.000 EUR'},
  {'id':3,'title':'Back End Engineer','location':'Barcelona','salary':'40.000 EUR'},
  {'id':4,'title':'Solutions Arquitect','location':'Bilbao'}
]
@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
  
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)