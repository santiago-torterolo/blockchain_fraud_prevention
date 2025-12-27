import pytest
from blockchain_fraud_prevention.fraud_detection.model import FraudModel

def test_model_prediction():
    model = FraudModel()
    assert model.predict({}) == 0
