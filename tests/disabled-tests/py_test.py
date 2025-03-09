import pytest

@pytest.fixture(scope="session")
def recurso_compartido():
    """Fixture con ámbito de sesión para un recurso compartido."""
    print("\nConfigurando recurso compartido...")
    recurso = "Recurso configurado"
    yield recurso
    print("\nLiberando recurso compartido...")

def xtest_uso_recurso_1(recurso_compartido):
    """Prueba que usa el recurso compartido."""
    assert recurso_compartido == "Recurso configurado"

def xtest_uso_recurso_2(recurso_compartido):
    """Otra prueba que usa el recurso compartido."""
    assert recurso_compartido == "Recurso configurado"
