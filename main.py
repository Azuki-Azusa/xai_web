from flask import Flask, send_file, request
from xai import chat

app = Flask(__name__)

@app.route("/faosuiefhiausnbvidbalnvsalshjdogfhasdiulgasliugiousadsdfhlaiusfhiausdhf")
def index(host="localhost"):
    print("访问首页")
    return send_file("templates/index.html")

@app.route("/fsdufyaowuihfioufiuosahuivhasdiuvisauvhiuh4iuhvvisuhasioduhviusahvioash", methods=["POST"])
def xai_route():
    messages = request.json["messages"]
    return chat(messages)

if __name__ == "__main__":
    app.run(port=19981)