import pytest
from blockchain_fraud_prevention.blockchain.blockchain import Blockchain

def test_blockchain_initialization():
    bc = Blockchain()
    assert len(bc.chain) == 0 # Genesis block not yet implemented
