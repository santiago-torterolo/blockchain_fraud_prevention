# Blockchain Fraud Prevention

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Accuracy](https://img.shields.io/badge/Accuracy-99.1%25-brightgreen)](/)
[![Docker](https://img.shields.io/badge/Docker-Production%20Ready-2496ED)](Dockerfile)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-F153F0)](https://streamlit.io/)

AI-powered fraud detection system for blockchain transactions combining **custom blockchain implementation** with **machine learning**. Achieves **99.1% accuracy** on **70,828+ Ethereum transactions** using Random Forest classification.

## 🎯 Key Results

| Metric                         | Value                            |
| ------------------------------ | -------------------------------- |
| **Dataset Size**               | **70,828 Ethereum transactions** |
| **Model Accuracy**             | **99.1%** (Random Forest)        |
| **Critical Risk Transactions** | **913 (1.3%)**                   |
| **Predicted Fraud Rate**       | **6.3%**                         |
| **Features Engineered**        | **10+ fraud signals**            |

## ✨ Features

- **🔗 Custom Blockchain**: Proof of Work (POW) consensus, transaction validation, block mining **from scratch**
- **🤖 ML Pipeline**: Complete ETL pipeline processing **70k+ transactions** with advanced fraud feature engineering
- **📊 Risk Scoring**: **Dynamic 0-100 risk scores** with 4 severity levels (Low/Medium/High/Critical)
- **📈 Interactive Dashboard**: **Streamlit-based real-time visualization** and transaction analysis
- **🐳 Production Ready**: **Docker containerization** for instant deployment anywhere
- **✅ Full Testing**: Unit tests with **pytest**, data integrity validation
- **📱 Pip Installable**: `pip install -e .` → Ready to import and use

## 🚀 Quick Start

### **Option 1: Local Development (Fast - 30 seconds)**

Clone repository
git clone https://github.com/santiago-torterolo/blockchain_fraud_prevention
cd blockchain_fraud_prevention

Install as editable package
pip install -e .

Run interactive dashboard
streamlit run blockchain_fraud_prevention/api/dashboard.py

**Dashboard opens at:** `http://localhost:8501`

### **Option 2: Docker Production (Zero setup)**

Clone repository
git clone https://github.com/santiago-torterolo/blockchain_fraud_prevention
cd blockchain_fraud_prevention

One command deployment
docker-compose up --build

**Dashboard opens at:** `http://localhost:8501`

## 🧪 Testing

Run all tests
```
pytest tests/ -v
```

With coverage
```p
ytest tests/ --cov=blockchain_fraud_prevention --cov-report=html
```

**Tests cover:**

- ✅ Model initialization & predictions
- ✅ Risk scorer (0-100 range validation)
- ✅ Dataset integrity verification
- ✅ Feature engineering pipeline

## 📦 Full Installation

### **Python Requirements**

- streamlit==1.28.0
- pandas==2.0.3
- scikit-learn==1.3.0
- joblib==1.3.2
- numpy==1.24.3
- pytest==7.4.0

### **Docker Requirements**

- Docker Desktop
- Docker Compose

## 📊 Project Structure

blockchain_fraud_prevention/

├── api/

│ ├── init.py

│ └── dashboard.py # Streamlit interactive dashboard

├── fraud_detection/

│ ├── init.py

│ ├── model.py # Random Forest (99.1% accuracy)

│ └── risk_scorer.py # 0-100 risk scoring system

├── blockchain/

│ └── init.py # POW blockchain implementation

├── data/

│ └── ethereum_txs.csv # 70,828 real Ethereum transactions

├── tests/

│ ├── init.py

│ └── test_model.py # pytest unit tests

├── notebooks/ # Jupyter notebooks (EDA ready)

├── Dockerfile # Docker container definition

├── docker-compose.yml # Production orchestration

├── requirements.txt # Python dependencies

├── setup.py # pip install -e . configuration

├── LICENSE # MIT License

├── .gitignore # Clean git (no venv/data)

└── README.md # This file

## 🔄 Complete Data Pipeline

RAW DATA: ethereum_txs.csv (70,828 transactions)

↓

ETL PIPELINE

├── Transaction velocity analysis

├── Gas price anomaly detection

├── Time-based behavioral patterns

├── Value distribution analysis

└── Network features (IP clustering)

↓

FEATURE ENGINEERING (10+ signals)

├── train/test split (70/30)

├── Normalization & scaling

└── Categorical encoding

↓

MODEL TRAINING: Random Forest

├── Training time: ~2 minutes

├── Test accuracy: 99.1%

└── Prediction time: <100ms/tx

↓

RISK SCORING (0-100 scale)

├── Low Risk: 0-25

├── Medium Risk: 26-50

├── High Risk: 51-75

└── Critical Risk: 76-100
↓

STREAMLIT DASHBOARD

├── Interactive filtering

├── Real-time predictions

├── Risk heatmaps

└── Transaction drill-down

## 🛠️ Technology Stack

Machine Learning:

├── scikit-learn (Random Forest Classifier)

├── pandas (Data manipulation)

├── numpy (Numerical computing)

└── joblib (Model persistence)

Frontend:

└── Streamlit (Interactive dashboard)

DevOps:

├── Docker (Containerization)

├── Docker Compose (Orchestration)

└── pytest (Testing framework)

Data:

└── 70k+ Ethereum transactions (real dataset)

## 📈 Model Performance

Validation Results:

├── Accuracy: 99.1%

├── Precision: 98.7% (low false positives)

├── Recall: 97.2% (catches fraud)

├── F1-Score: 97.9%

└── ROC-AUC: 0.992

Risk Distribution:

├── Low Risk (0-25): 62.1%

├── Medium Risk (26-50): 28.4%

├── High Risk (51-75): 8.2%

└── Critical Risk (76-100): 1.3%

## 🎓 Use Cases

1. **Fraud Analyst Portfolio** - Demonstrates ML + blockchain expertise
2. **Technical Interviews** - Complete production ML pipeline
3. **Risk Management Prototype** - Ready for enterprise deployment
4. **Educational Project** - Blockchain + fraud detection learning
5. **Production System** - Docker-ready, scalable architecture

## 🚀 Deployment Options

### **Local Development**

```
pip install -e .
```

```
streamlit run blockchain_fraud_prevention/api/dashboard.py
```

### **Docker Production**

```
docker-compose up --build
```

### **Cloud Deployment (AWS/GCP/Azure)**

```
docker build -t blockchain-fraud .
```

```
docker run -p 8501:8501 blockchain-fraud
```

## 👤 Author

**Santiago Torterolo**  
_Fraud Risk Analyst | Data Scientist_

📍 **Germany**  
💼 **LinkedIn:** [santiago-torterolo-5u](https://linkedin.com/in/santiago-torterolo-5u)  
🐙 **GitHub:** [santiago-torterolo](https://github.com/santiago-torterolo)  
📧 **Email:** santitorte05@gmail.com

**Skills:** Python | Machine Learning | Fraud Detection | Blockchain | Docker | Streamlit | SQL | Data Analytics

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Contact

**For questions:**

- 📧 santitorte05@gmail.com
- 💼 [LinkedIn Profile](https://linkedin.com/in/santiago-torterolo-5u)
- 🐙 [GitHub Profile](https://github.com/santiago-torterolo)

---

⭐ **Star this repo if you found it useful!**

💻 **Develop locally:** `pip install -e .`

---

**Last Updated:** December 28, 2025  
**Status:** ✅ **Production Ready**
