import pytest
from blockchain_fraud_prevention.fraud_detection.feature_engineering import extract_features

def test_feature_extraction():
    assert extract_features({}) == {}
