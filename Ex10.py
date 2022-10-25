def test_phrase():
    phrase = input("Set a phrase: ")
    symbols = len(phrase)
    assert symbols <= 15, "Phrase is longer than 15 characters"
