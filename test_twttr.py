from twttr import shorten

def test_Lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("CaT") == "CT"
    assert shorten("Happy") == "Hppy"

def test_Uppercase():
    assert shorten("EdUcAtION") == "dctN"
    assert shorten("hUmAn") == "hmn"
    assert shorten("WORLD") == "WRLD"

def test_characters():
    assert shorten("CS50") == "CS50"
    assert shorten("What's Your Name?") == "Wht's Yr Nm?"