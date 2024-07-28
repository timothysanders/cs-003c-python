# CS-003 - Lab 9.33.22
# 7/25/2024
# Zoraida Rodriguez
# Tim Sanders

# pytest can be installed by running `pip install pytest` in the terminal
import pytest


## A bank account has a balance that can be changed by deposits and
#  withdrawals.
#
class BankAccount:

    ## Constructs a bank account with a given balance.
    #  @param initial_balance: float
    #        - The initial account balance (default = 0.0)
    #
    def __init__(self, initial_balance: float = 0.0) -> None:
        if initial_balance < 0:
            raise ValueError("Initial balance must be non-negative.")
        self._balance = initial_balance

    ## Deposits money into the this account.
    #  @param amount: float
    #        - The amount to deposit
    #
    def deposit(self, amount: float) -> None:
        if not isinstance(amount, (float, int)):
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    ## Makes a withdrawal from this account
    #  @param amount: float
    #
    def withdraw(self, amount: float) -> None:
        if not isinstance(amount, (float, int)):
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds in account.")
        self._balance -= amount

    ## Gets the current balance of this account.
    #  @return the current balance
    #
    def get_balance(self) -> float:
        return self._balance


## A class to manage a portfolio consisting of a checking and a savings account.
#
class Portfolio:
    VALID_ACCOUNTS = {'C', 'S'}

    ## Initialize the Portfolio() class with two accounts. The default
    ## balance for the accounts is $100.00, unless otherwise specified
    #  @param checking_initial_balance: float = 100.00
    #        - The initial balance that will be given to a checking account,
    #          defaults to 100.00, unless otherwise specified
    #  @param savings_initial_balance: float = 100.00
    #        - The initial balance that will be given to a savings account,
    #          defaults to 100.00, unless otherwise specified
    #
    def __init__(self,
                 checking_initial_balance: float = 100.00,
                 savings_initial_balance: float = 100.00
                 ) -> None:
        if not (
                isinstance(checking_initial_balance, (float, int)) and
                isinstance(savings_initial_balance, (float, int))
        ):
            raise TypeError("Initial balances provided must be numbers.")
        if checking_initial_balance < 0 or savings_initial_balance < 0:
            raise ValueError("Initial balances must be non-negative.")
        self.checking = BankAccount(checking_initial_balance)
        self.savings = BankAccount(savings_initial_balance)

    ## Method for adding money to a given account. Amounts added to accounts
    ## must be positive numbers
    #  @param amount: float
    #        - The dollar amount to be deposited into a given account
    #  @param account: str
    #        - The account to deposit the given amount to, can only be one
    #          of “S” (savings) or “C” (checking)
    #
    def deposit(self, amount: float, account: str = "C") -> None:
        if not isinstance(account, str):
            raise TypeError("Account type must be a string.")
        if not isinstance(amount, (float, int)):
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        if account not in self.VALID_ACCOUNTS:
            raise ValueError(
                "Account must be 'C' for checking or 'S' for savings."
            )

        if account == 'C':
            self.checking.deposit(amount)
        else:
            self.savings.deposit(amount)

    ## Method to withdraw money from the specified account, withdrawal amount
    ## must be a positive number
    #  @param amount: float
    #        - The dollar amount to be withdrawn from the given account
    #  @param account: str
    #        - The account to withdraw the given amount from, can only be one
    #          of “S” (savings) or “C” (checking)
    #
    def withdraw(self, amount: float, account: str = "C") -> None:
        if not isinstance(account, str):
            raise TypeError("Account type must be a string.")
        if not isinstance(amount, (float, int)):
            raise TypeError("Withdrawal amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if account not in self.VALID_ACCOUNTS:
            raise ValueError(
                "Account must be 'C' for checking or 'S' for savings."
            )

        if account == 'C':
            self.checking.withdraw(amount)
        else:
            self.savings.withdraw(amount)

    ## Method to move specific amounts from one account to another. Note that
    ## the account specified indicates the account from which the money is
    ## taken; the money is automatically transferred to the other account
    #  @param amount: float
    #        - The dollar amount to be transferred out of the given account.
    #          This amount must be a positive amount
    #  @param account: str
    #        - The account from which to transfer the given amount, can only
    #          be one of “S” (savings) or “C” (checking)
    #
    def transfer(self, amount: float, fromAccount: str = "C") -> None:
        if not isinstance(fromAccount, str):
            raise TypeError("Account type must be a string.")
        if not isinstance(amount, (float, int)):
            raise TypeError("Transfer amount must be a number.")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if fromAccount not in self.VALID_ACCOUNTS:
            raise ValueError(
                "Account must be 'C' for checking or 'S' for savings."
            )

        if fromAccount == 'C':
            self.checking.withdraw(amount)
            self.savings.deposit(amount)
        else:
            self.savings.withdraw(amount)
            self.checking.deposit(amount)

    ## Accessor method to retrieve the balance of a particular account in a
    ## portfolio.
    #  @param account: str
    #        - The account from which to retrieve the balance, can only be
    #          one of “S” (savings) or “C” (checking)
    #
    def get_balance(self, account: str = "C") -> float:
        if not isinstance(account, str):
            raise TypeError("Account type must be a string.")
        if account not in self.VALID_ACCOUNTS:
            raise ValueError(
                "Account must be 'C' for checking or 'S' for savings."
            )
        if account == "C":
            balance = self.checking.get_balance()
        else:
            balance = self.savings.get_balance()
        return balance


def main():
    tims_portfolio = Portfolio()
    # deposit $100 into our savings account and get the current balance
    tims_portfolio.deposit(amount=100.00, account="S")
    current_savings_balance = tims_portfolio.get_balance("S")
    print(f"Current savings account balance: ${current_savings_balance}")

    # Sample Input and Output with Enhanced Validation and Default Parameters
    tims_portfolio = Portfolio(
        checking_initial_balance=100.00,
        savings_initial_balance=100.00
    )

    # Test deposit with named argument
    tims_portfolio.deposit(amount=50.00, account="S")
    # Output: Deposited $50.00 to savings account. New balance: $150.00.

    # Test withdrawal that exceeds amount available in account
    try:
        tims_portfolio.withdraw(amount=200.00, account="C")
    except ValueError as e:
        print(e)  # Output: Insufficient funds in account.

    # Test transfer with named arguments
    tims_portfolio.transfer(amount=50.00, fromAccount="C")
    # Output: Transferred $50.00 from checking to savings account.
    # Checking balance: $50.00, Savings balance: $200.00.

    # Test get_balance with default parameter
    balance = tims_portfolio.get_balance(account="C")
    print(f"The balance of the checking account is ${balance:.2f}.")
    # Output: The balance of the checking account is $50.00.


if __name__ == "__main__":
    main()


# UNIT TESTS
# Unit tests can be run by executing `pytest main.py` in the terminal
# after the installation of pytest above.

# BankAccount() class and method unit tests
def test_account_init_with_type_error():
    with pytest.raises(TypeError):
        BankAccount(initial_balance="one")


def test_account_default_init():
    assert BankAccount().get_balance() == 0.0


def test_account_deposit_with_type_error():
    with pytest.raises(TypeError):
        BankAccount().deposit("a")


def test_account_deposit_with_value_error():
    with pytest.raises(ValueError):
        BankAccount().deposit(-1)


def test_account_deposit():
    test_account = BankAccount()
    test_account.deposit(100.0)
    assert test_account.get_balance() == 100.0


def test_account_withdraw():
    test_account = BankAccount(initial_balance=100.0)
    test_account.withdraw(50)
    assert test_account.get_balance() == 50.0


def test_account_withdraw_with_value_error():
    with pytest.raises(ValueError):
        test_account = BankAccount(initial_balance=100.0)
        test_account.withdraw(200)


def test_account_withdraw_with_type_error():
    with pytest.raises(TypeError):
        test_account = BankAccount(initial_balance=100.0)
        test_account.withdraw("ten")


# Portfolio() class and method unit tests
def test_portfolio_init_savings_with_type_error():
    with pytest.raises(TypeError):
        Portfolio(checking_initial_balance=100.00,
                  savings_initial_balance="a")


def test_portfolio_init_checking_with_type_error():
    with pytest.raises(TypeError):
        Portfolio(checking_initial_balance="a",
                  savings_initial_balance=100.00)


def test_portfolio_init_both_with_type_error():
    with pytest.raises(TypeError):
        Portfolio(checking_initial_balance="a",
                  savings_initial_balance="a")


def test_portfolio_deposit_checking_type_error():
    with pytest.raises(TypeError):
        test_portfolio = Portfolio()
        test_portfolio.deposit(amount="a", account="C")


def test_portfolio_deposit_savings_type_error():
    with pytest.raises(TypeError):
        test_portfolio = Portfolio()
        test_portfolio.deposit(amount="a", account="S")


def test_portfolio_deposit_checking_value_error():
    with pytest.raises(ValueError):
        test_portfolio = Portfolio()
        test_portfolio.deposit(amount=-100.00, account="C")


def test_portfolio_deposit_savings_value_error():
    with pytest.raises(ValueError):
        test_portfolio = Portfolio()
        test_portfolio.deposit(amount=-100.00, account="S")


def test_portfolio_deposit_checking():
    test_portfolio = Portfolio()
    test_portfolio.deposit(amount=100.00, account="C")
    assert test_portfolio.get_balance(account="C") == 200.0


def test_portfolio_deposit_savings():
    test_portfolio = Portfolio()
    test_portfolio.deposit(amount=100.00, account="S")
    assert test_portfolio.get_balance(account="S") == 200.0


def test_portfolio_withdraw_checking_type_error():
    with pytest.raises(TypeError):
        test_portfolio = Portfolio()
        test_portfolio.withdraw(amount="a", account="C")


def test_portfolio_withdraw_savings_type_error():
    with pytest.raises(TypeError):
        test_portfolio = Portfolio()
        test_portfolio.withdraw(amount="a", account="S")


def test_portfolio_withdraw_checking_value_error():
    with pytest.raises(ValueError):
        test_portfolio = Portfolio()
        test_portfolio.withdraw(amount=-100, account="C")


def test_portfolio_withdraw_savings_value_error():
    with pytest.raises(ValueError):
        test_portfolio = Portfolio()
        test_portfolio.withdraw(amount=-100, account="S")


def test_portfolio_withdraw_checking():
    test_portfolio = Portfolio()
    test_portfolio.withdraw(amount=100, account="C")
    assert test_portfolio.get_balance(account="C") == 0.0


def test_portfolio_withdraw_savings():
    test_portfolio = Portfolio()
    test_portfolio.withdraw(amount=100, account="S")
    assert test_portfolio.get_balance(account="S") == 0.0


def test_portfolio_transfer_checking_type_error():
    with pytest.raises(TypeError):
        test_portfolio = Portfolio()
        test_portfolio.transfer(amount="a", fromAccount="C")


def test_portfolio_transfer_savings_type_error():
    with pytest.raises(TypeError):
        test_portfolio = Portfolio()
        test_portfolio.transfer(amount="a", fromAccount="S")


def test_portfolio_transfer_checking_value_error():
    with pytest.raises(ValueError):
        test_portfolio = Portfolio()
        test_portfolio.transfer(amount=-100, fromAccount="C")


def test_portfolio_transfer_savings_value_error():
    with pytest.raises(ValueError):
        test_portfolio = Portfolio()
        test_portfolio.transfer(amount=-100, fromAccount="S")


def test_portfolio_transfer_checking():
    test_portfolio = Portfolio()
    test_portfolio.transfer(amount=100, fromAccount="C")
    assert test_portfolio.get_balance(account="S") == 200.00


def test_portfolio_transfer_savings():
    test_portfolio = Portfolio()
    test_portfolio.transfer(amount=100, fromAccount="S")
    assert test_portfolio.get_balance(account="C") == 200.00


def test_portfolio_get_balance():
    test_portfolio = Portfolio()
    assert test_portfolio.get_balance(account="C") == 100.00
    assert test_portfolio.get_balance(account="S") == 100.00

