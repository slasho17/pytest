from funcoes import *

def test_email_valido():
    assert email_valido("mei eimail@.com") == True    
    assert email_valido("l@.com") == True    
    assert email_valido(".@.@.@.@") == True    
    assert email_valido("mei eimail@") == False    
    assert email_valido("mei eimail") == False    
    assert email_valido("@@@@@@@@@@@@@@") == False    

def test_dividir():
    assert dividir(4,2) == 2
    assert dividir(4,4) == 1
    assert dividir(4,0) is None