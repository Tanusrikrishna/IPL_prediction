from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load dataset
df = pd.read_csv("IPL_data.csv")

# Basic model: Predict total runs based on averages
def predict_runs(batting_team, bowling_team, overs, runs_last_5, wickets_last_5):
    avg_runs = df.groupby("batting_team")["total"].mean()
    predicted_runs = avg_runs.get(batting_team, df["total"].mean())
    return int(predicted_runs)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    batting_team = request.form['batting_team']
    bowling_team = request.form['bowling_team']
    overs = float(request.form['overs'])
    runs_last_5 = int(request.form['runs_last_5'])
    wickets_last_5 = int(request.form['wickets_last_5'])
    
    predicted_runs = predict_runs(batting_team, bowling_team, overs, runs_last_5, wickets_last_5)
    
    return render_template('result.html', prediction=predicted_runs)

if __name__ == '__main__':
    app.run(debug=True)
