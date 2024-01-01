import pytest

import source.my_functions as my_functions

def test_add():
    result = my_functions.add(number_one=4, number_two=10)

    assert result == 14

def test_add_strings():

    result = my_functions.add(  number_one="Pep Guardiola is ", number_two= "the best coach in the league")

    assert result == "Pep Guardiola is the best coach in the league"



def test_divide():
    result = my_functions.divide(number_one=15, number_two=3)

    assert result == 5