from multi_sided_die import MultiSidedDie

def test_addition():
    dice_instance = MultiSidedDie(5)
    assert dice_instance.roll() == 3
    assert dice_instance.roll() == 3
    assert dice_instance.roll() == 1

def test_set_and_get_value():
    dice_instance = MultiSidedDie(8)
    dice_instance.set_value(8) 
    assert dice_instance.get_value() == 8
    dice_instance.set_value(7) 
    assert dice_instance.get_value() == 7
    dice_instance.set_value(6) 
    assert dice_instance.get_value() == 6

