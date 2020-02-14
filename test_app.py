from app import *

def test_finish_month():
    fnb= BankAccount(1000)
    assert fnb.finish_month()==960

