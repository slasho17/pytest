from funcoes import *

def test_email_valido():
    assert email_valido("mei eimail@.com") is True    
    assert email_valido("l@.com") is True    
    assert email_valido(".@.@.@.@") is True    
    assert email_valido("mei eimail@") is False    
    assert email_valido("mei eimail") is False    
    assert email_valido("@@@@@@@@@@@@@@") is False    

def test_dividir():
    assert dividir(4,2) == 2
    assert dividir(4,4) == 1
    assert dividir(4,0) is None