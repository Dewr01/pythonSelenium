def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"


a, b = map(int, input().split())
test_input_text(a, b)
