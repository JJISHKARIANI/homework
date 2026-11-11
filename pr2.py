import pytest
from bank import BankAccount

def test_initial_balance():
    account = TestAccount = BankAccount("Jaba", 100.0)
    assert account.balance == 100.0
    
    default_account = BankAccount("Jaba")
    assert default_account.balance == 0.0

def test_deposit_success():
    account = BankAccount("Jaba", 100.0)
    new_balance = account.deposit(50)
    assert new_balance == 150.0
    assert account.balance == 150.0

def test_deposit_negative():
    account = BankAccount("Jaba", 100.0)
    with pytest.raises(ValueError):
        account.deposit(-50)
    with pytest.raises(ValueError):
        account.deposit(0)

def test_withdraw_success():
    account = BankAccount("Jaba", 200.0)
    new_balance = account.withdraw(50)
    assert new_balance == 150.0
    assert account.balance == 150.0

def test_withdraw_insufficient_funds():
    account = BankAccount("Jaba", 50.0)
    with pytest.raises(ValueError):
        account.withdraw(100)

def test_withdraw_negative():
    account = BankAccount("Jaba", 100.0)
    with pytest.raises(ValueError):
        account.withdraw(-20)
    with pytest.raises(ValueError):
        account.withdraw(0)