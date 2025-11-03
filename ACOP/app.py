from flask import Flask, render_template
from threat_engine import collect_threat_data, analyze_and_respond

app = Flask(__name__)

@app.route('/')
def dashboard():
    threats = collect_threat_data()
    actions = analyze_and_respond(threats)
    return render_template('dashboard.html', actions=actions)

if __name__ == '__main__':
    app.run(debug=True)

