from machinetranslation import translator
from flask import Flask, render_template, request
import json
from machinetranslation.translator import englishToFrench, frenchToEnglish

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    return englishToFrench(textToTranslate)

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    return frenchToEnglish(textToTranslate)

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
