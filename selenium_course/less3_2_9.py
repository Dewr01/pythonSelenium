def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"


a, b = map(str, input().split())
test_substring(a, b)
