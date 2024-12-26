# Car Price Prediction API

This is a simple API for predicting car prices using a Linear Regression model. The API is built with **FastAPI** and uses a pre-trained model saved as `LRModel.pkl`. The predictions are based on input features that must match the format of the training data.

## Project Structure

- **`API/scoring.py`**: Contains functions to process input and run predictions using the Linear Regression model.
- **`data-train/`**: Includes the training data (`car data.csv`) and a cleaned dataset (`Cleaned Car.csv`).
- **`model/`**: Contains the trained model (`LRModel.pkl`) and the training notebook (`model.ipynb`).
- **`server/application.py`**: Main FastAPI application to handle API requests.
- **`Procfile`**: Configuration for deploying the application on platforms like Heroku.
- **`requirements.txt`**: Lists all Python dependencies for the project.
- **`README.md`**: Documentation for the project.

## Features

- Predict car prices based on input data matching the training data format.
- Built using FastAPI for fast and efficient API responses.
- Includes all necessary files to train, test, and deploy the model.


## Training the Model
- The model was trained using the data in data-train/ and the code in model/model.ipynb.
- The final model is serialized and saved as LRModel.pkl in the model/ directory.