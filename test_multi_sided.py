from multi_sided_die import MultiSidedDie

dice_instance = MultiSidedDie()

def test_addition():
    assert dice_instance.addition(3,3) == 6
    assert dice_instance.addition(3, 3,3) == 9
    assert dice_instance.addition(3, 3,3,3) == 12