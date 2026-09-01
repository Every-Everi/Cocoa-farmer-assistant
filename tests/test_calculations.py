from calculations import calculate_profit

def test_calculate_profit():
    result = calculate_profit(1000, 400)
    assert result == 600
    print("Test passed! Profit calculation is correct.")

test_calculate_profit()