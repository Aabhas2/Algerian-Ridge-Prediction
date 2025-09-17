# Algerian Forest Fire Prediction

A machine learning project that predicts the Forest Fire Weather Index (FWI) using Ridge Regression. The project provides both Flask web interface and Streamlit application for making predictions.

## Dataset Information

The dataset used in this project contains forest fire data from two regions of Algeria:
- Bejaia region (Northeast of Algeria)
- Sidi Bel-abbes region (Northwest of Algeria)

**Period**: June 2012 to September 2012
**Total Instances**: 244 (122 instances for each region)
**Classes**: Fire (138 cases) and Not Fire (106 cases)

### Features

1. Temperature (°C)
2. RH (%): Relative Humidity
3. Ws (km/h): Wind Speed
4. Rain (mm): Rainfall
5. FFMC: Fine Fuel Moisture Code
6. DMC: Duff Moisture Code
7. DC: Drought Code
8. ISI: Initial Spread Index
9. BUI: Buildup Index
10. FWI: Fire Weather Index (Target Variable)
11. Classes: Fire / Not Fire
12. Region: Bejaia (0) / Sidi Bel-abbes (1)

## Project Structure

```
├── application.py          # Flask web application
├── streamlit_app.py       # Streamlit web application
├── requirements.txt       # Project dependencies
├── models/
│   ├── ridge.pkl         # Trained Ridge regression model
│   └── scaler.pkl        # Fitted StandardScaler
├── notebook/
│   ├── Algerian_EDA.ipynb    # Exploratory Data Analysis
│   ├── Model_Training.ipynb  # Model training notebook
│   └── Algerian_forest_fires_cleaned_dataset.csv  # Dataset
└── templates/
    ├── home.html         # Prediction page template
    └── index.html        # Landing page template
```

## Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/Aabhas2/Algerian-Ridge-Prediction.git
cd Algerian-Ridge-Prediction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Applications

### Flask Web Application
```bash
python application.py
```
Access the application at `http://localhost:5000`

### Streamlit Application
```bash
streamlit run streamlit_app.py
```
The application will automatically open in your default web browser.

## Model Information

- **Algorithm**: Ridge Regression
- **Features**: The model uses all input features after standardization
- **Target**: Fire Weather Index (FWI)
- **Preprocessing**: StandardScaler for feature normalization

## Using the Web Interface

1. Enter the following values in the input form:
   - Temperature
   - Relative Humidity (RH)
   - Wind Speed (Ws)
   - Rainfall
   - Fine Fuel Moisture Code (FFMC)
   - Duff Moisture Code (DMC)
   - Initial Spread Index (ISI)
   - Classes (0 for not fire, 1 for fire)
   - Region (0 for Bejaia, 1 for Sidi Bel-abbes)

2. Click "Predict" to get the FWI prediction

## Files Description

- `application.py`: Flask web application that serves the prediction interface
- `streamlit_app.py`: Streamlit application providing an alternative interface
- `models/ridge.pkl`: Serialized Ridge regression model
- `models/scaler.pkl`: Serialized StandardScaler for feature normalization
- `notebook/Algerian_EDA.ipynb`: Jupyter notebook containing exploratory data analysis
- `notebook/Model_Training.ipynb`: Jupyter notebook with model training process
- `templates/`: Contains HTML templates for the Flask web application

## Requirements

- Python 3.x
- Flask
- Streamlit
- NumPy
- Pandas
- Scikit-learn

## Contributing

Feel free to submit issues and enhancement requests!
