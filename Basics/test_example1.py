def test_add(a=20,b=10):
    c=a+b
    assert c==30

def test_sub(a=40,b=10):
    c=a-b
    assert c==30

def test_m1():
    software='selenium'
    assert software.upper()=='selenium'

def test_m2():
    tool='selenium'
    assert tool.lower()=='selenium'

