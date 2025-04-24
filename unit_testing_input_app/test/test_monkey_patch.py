import sys
import os
import pytest
import io
sys.path += ['C:/Users/yasmi/Desktop/Test_git/learn_pytest/unit_testing_input_app/src'] #adding the absolut path to import main
from main import *
def test_username_notempty(monkeypatch): #using monkeypatch to simulate userinput 
    monkeypatch.setattr('sys.stdin', io.StringIO('\n'))
    assert get_user_name() is None
def test_username_nospaces(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Alice Bruce'))
    assert get_user_name() is None
def test_password_8characters(monkeypatch): 
    monkeypatch.setattr('sys.stdin', io.StringIO('@Z$*2'))
    assert get_password() is None
def test_password_Onenumber(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('@Zerty$*frzad'))
    assert get_password() is None
def test_password_onelettre(monkeypatch): 
    monkeypatch.setattr('sys.stdin', io.StringIO('$*233910938760'))
    assert get_password() is None 
def test_password_onespecialchar(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('qsdfghh123456'))
    assert get_password() is None
def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('bruce,wayne2wayneenterprises,com'))
    assert get_email() is None
def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('brucewayne@wayneenterprises,com'))
    assert get_email() is None
def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('bruce.wayne@wayneenterprisescom'))
    assert get_email() == 'bruce.wayne@wayneenterprisescom'
