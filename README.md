# Skipper Project

This is a Flask-based web application designed for data analysis and machine learning. The project includes a user-friendly interface for interacting with data and visualizing results.

---

## Features

- **Web Framework**: Built with Flask.
- **Data Processing**: Utilizes `pandas` and `numpy` for data manipulation.
- **Machine Learning**: Includes `xgboost` and `scikit-learn` for model training and predictions.
- **Excel Support**: Reads and processes `.xlsx` files using `openpyxl`.
- **Frontend**: Styled with custom CSS and HTML templates.

---

## Project Structure

```
Galvanized_Zinc/
│
├── app.py                  # Main Flask application
├── model_training.py       # Machine learning model training script
├── requirements.txt        # Python dependencies
├── Skipperindus_datacombined.xlsx  # Sample dataset
│
├── static/                 # Static files (CSS, JS, images)
│   └── style.css           # Custom styles
│
├── templates/              # HTML templates
│   ├── index.html          # Homepage
│   └── result.html         # Results page
│
└── README.md               # Project documentation
```

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/certifiedkgpian/Skipper_Project.git
   cd Skipper_Project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## Deployment

### Render.com

1. Add a `Procfile` with the following content:
   ```
   web: gunicorn app:app
   ```

2. Push the code to GitHub and connect it to Render.com.

3. Follow the Render deployment guide to host your application.

---

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS
- **Data Processing**: pandas, numpy
- **Machine Learning**: xgboost, scikit-learn
- **Excel Handling**: openpyxl

---

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For any inquiries or issues, please contact:
- **GitHub**: [certifiedkgpian](https://github.com/certifiedkgpian)
- **Email**: rohan.vjs2004@gmail.com
