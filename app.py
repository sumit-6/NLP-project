import requests
from flask import Flask,render_template
from flask import request as req


app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html", data="", result="")

@app.route("/summarize",methods=["GET","POST"])
def summarize():
    if req.method== "POST":
        API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
        headers = {"Authorization": f"Bearer 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"}

        data=req.form["data"]

        maxL=int(req.form["maxL"])
        minL=maxL//4
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs":data,
            "parameters":{"min_length":minL,"max_length":maxL},
        })[0]
        
        return render_template("index.html",result=output["summary_text"], data=data)
    else:
        return render_template("index.html", data="", result="")