from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "^<h1^>Прив?т! Веб-застосунок усп?шно розгорнуто на PaaS ^(Render^).^</h1^>^<p^>Виконав: Михайло^</p^>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
