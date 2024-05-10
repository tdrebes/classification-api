from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

MAX_CLASSES = 20
zeroshot_classifier = pipeline("zero-shot-classification", model="model")

@app.route("/")
def index():
    return "<p>Listening</p>"

@app.route("/classification", methods=['GET', 'POST'])
def classification():
    try:
        data = request.json
        text = data.get("text", "")
        template = data.get("template", "This text is about")
        classes = data.get("classes", [])
        hypothesis_template = f"{template} {{}}"

        if (len(classes) > MAX_CLASSES):
            raise Exception("Too many classes")

        output = zeroshot_classifier(text, classes, hypothesis_template=hypothesis_template, multi_label=False)
        results = dict(zip(output["labels"], output["scores"]))

        return jsonify(success=True, best_match=max(results, key=results.get), results=results)
    except:
        return jsonify(success=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
