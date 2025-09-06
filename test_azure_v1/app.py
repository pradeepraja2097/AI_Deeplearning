from flask import Flask,request,jsonify
import openai
import os

app=Flask(__name__)
openai.api_key= os.getenv()
@app.route("/prompt",methods=["POST"])

def prompt():
    data=request.json
    response=openai.Completion.create(
        engine="text-davinci-003",
        prompt=data['prompt'],
        max_tokens=100
    )
    return jsonify(response.choices[0].text.strip())

if __name__=="__main__":
    app.run(debug=True)
