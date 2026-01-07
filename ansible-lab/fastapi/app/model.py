import time

class DummyModel:
    def __init__(self):
        # simula carga pesada
        time.sleep(1)

    def predict(self, text: str) -> str:
        return f"processed: {text}"

# se carga UNA vez al importar el módulo
model = DummyModel()