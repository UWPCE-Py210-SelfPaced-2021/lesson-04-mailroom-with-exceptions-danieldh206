
from mailroom import main_selection, letter, donor_list, donor_report, sort, add_donor

def test_donor_list():
    print (donor_list)
    #assert (donor_list()) == 'William Gates, III\nJeff Bezos\nPaul Allen\nMark Zuckerberg'
    # To see the output when I run 'pytest -rP'
    print (donor_list())

def test_add_dono_0():
    # verify correct return for new donor
    assert add_donor('Chizuko',18000.25) == ('Chizuko', [18000.25])

def test_add_donor_1():
    # verify new donation from current donor is added to donations
    assert add_donor('William Gates',653772.32) == ('William Gates', [653772.32, 12.17, 653772.32])

def test_letter():
    # Using the len of the output is the only way I figured out how to test
    assert len(letter('Jeff',500)) == 115
    
def test_donor_report():
    # I could not figure out an easy way to configure an assert so I run 'pytest -rP' to see output 
    print (donor_report())
    
def test_main_selection(monkeypatch):
    # if lowercase Q is made uppercase
    monkeypatch.setattr('builtins.input', lambda choice: 'q')
    assert main_selection() == 'Q'
    