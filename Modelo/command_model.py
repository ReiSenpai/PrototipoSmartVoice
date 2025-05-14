class CommandModel:
    def __init__(self):
        self.commands = {
            "encender luz": "🔆 Luz encendida",
            "activar ventilador": "🌀 Ventilador activado",
        }

    def get_action(self, command):
        return self.commands.get(command.lower(), "Comando no reconocido")

