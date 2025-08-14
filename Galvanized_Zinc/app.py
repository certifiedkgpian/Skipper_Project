from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import re
from xgboost import XGBRegressor

app = Flask(__name__)

# --- Configuration ---
file_path = "Skipperindus_datacombined.xlsx"
sheet_name = "Angles"

# Load data
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Helper: compute angle area from string
def angle_area(section_str):
    dims = list(map(int, re.findall(r'\d+', str(section_str))))
    if len(dims) == 3:
        width1, width2, thickness = dims
        return (width1 + width2 - thickness) * thickness
    return np.nan

# Add computed column
df["ANGLE AREA (mm²)"] = df["SECTION"].apply(angle_area)

# Input features & output targets
input_features = [
    "ANGLE AREA (mm²)", "THICKNESS (MM)", "JIG WT (KG)",
    "Avg Top Coating (µm)", "Avg Middle Coating (µm)", "Avg Bottom Coating (µm)"
]
output_targets = [
    "ACID CONC (%)", "PICKLING TIME (MIN)", "FLUX DIPPING TIME (SEC)",
    "DRYER HOLDING TIME (MIN)", "ZINC BATH TEMP. (C°)", "IMMERSION TIME (SEC)"
]

# Train models once at startup
models = {}
X = df[input_features]
for target in output_targets:
    y = df[target]
    model = XGBRegressor(verbosity=0, random_state=42)
    model.fit(X, y)
    models[target] = model

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form inputs
    section_input = request.form['section_input']
    thickness_input = float(request.form['thickness_input'])
    jig_weight_input = float(request.form['jig_weight_input'])
    avg_top = float(request.form['avg_top'])
    avg_mid = float(request.form['avg_mid'])
    avg_bot = float(request.form['avg_bot'])

    # Compute angle area
    angle_area_input = angle_area(section_input)

    # Create input vector
    input_vector = np.array([[
        angle_area_input,
        thickness_input,
        jig_weight_input,
        avg_top,
        avg_mid,
        avg_bot
    ]])

    # Predictions
    predictions = {target: models[target].predict(input_vector)[0] for target in output_targets}

    return render_template('result.html', predictions=predictions)

if __name__ == "__main__":
    app.run(debug=True)
