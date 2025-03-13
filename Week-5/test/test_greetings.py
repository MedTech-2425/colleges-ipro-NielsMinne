from greetings import hello, goodbye

def test_default():
    assert hello() == "Hello, Guest"
    assert goodbye() == "Goodbye, Guest"

def test_argument():
    assert hello('Niels') == "Hello, Niels"
    assert goodbye('Niels') == "Goodbye, Niels"
