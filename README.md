# ML - CI/CD - Azure WebApp Deployment - Project Architecture

![image](https://github.com/user-attachments/assets/81cd27d8-6001-4d4a-a7d4-09210d5bf777)

# Dataset

![image](https://github.com/user-attachments/assets/27161b83-0c51-4323-bfae-cec659f1004e)

# CI/CD Pipeline

![image](https://github.com/user-attachments/assets/d6532373-7aa2-4921-be1e-4701026c4ddf)

# Azure WebApp Deployment - Prediction UI

![image](https://github.com/user-attachments/assets/9ca6efc8-f17d-4510-99cf-d92546c38bdd)


# 🍷 Wine Quality Prediction Web App

This project presents a machine learning model deployed as an Azure Web App to predict the quality of wine based on its physicochemical properties. Users can input various attributes of wine, and the application will predict its quality score.

## 🚀 Features

- **Machine Learning Model**: Utilizes a trained model to predict wine quality.
- **Web Interface**: User-friendly interface for inputting wine characteristics.
- **Azure Deployment**: Hosted on Microsoft Azure for accessibility.

## 📊 Dataset

The model is trained on the [Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/Wine+Quality) from the UCI Machine Learning Repository, which includes physicochemical tests and quality ratings for red and white wines.

## 🛠️ Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jnoothan/Wine_Quality_ML_Azure_WebApp.git
   cd Wine_Quality_ML_Azure_WebApp
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application Locally**:
   ```bash
   python app.py
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

## 🌐 Deployment on Azure

To deploy the application on Azure:

1. **Create an Azure Web App**:
   - Navigate to the [Azure Portal](https://portal.azure.com/).
   - Create a new Web App resource.
   - Configure the runtime stack (e.g., Python 3.8).

2. **Deploy the Application**:
   - Use Azure CLI or GitHub Actions for deployment.
   - Ensure all necessary files (`app.py`, `requirements.txt`, etc.) are included.

3. **Configure Application Settings**:
   - Set any required environment variables.
   - Adjust settings as needed for the application to run smoothly.

For detailed instructions, refer to Azure's [official documentation](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python).

## 📁 Project Structure

```
├── app.py
├── model.pkl
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── README.md
```

- `app.py`: Main application file.
- `model.pkl`: Serialized machine learning model.
- `requirements.txt`: Python dependencies.
- `static/`: Static files like CSS.
- `templates/`: HTML templates.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Youtube playlist - https://www.youtube.com/playlist?list=PLPMPu1ti8DuF94N9QX-PbngIKsA0zsUCc

## 📬 Contact

- **Author**: Noothana Prasanna  
- **Email**: [noothanms998@gmail.com](mailto:noothanms998@gmail.com)
