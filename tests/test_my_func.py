import pytest
import source.basic as test_main


#test on numbers
def test_add():
    result = test_main.add(3,2)
    assert result == 5

#def test_divide():
    #reult = test_main.divide(1,0)
    #assert reult == 2

#def test_divide_0():
    #with pytest.raises(ZeroDivisionError):
        #test_main.divide(1,0)


def test_divide_V():
    with pytest.raises(ValueError):
        test_main.divide(1,0)
 
#Test on Strings 
def test_add_strings():
    result = test_main.add("I like ","Burger")
    assert result == "I like Burger"
