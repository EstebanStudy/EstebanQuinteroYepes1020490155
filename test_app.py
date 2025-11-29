from app import saludar

def test_saludar():
    assert saludar() == "Hola Mundo desde CI/CD"