class Inventory:
    def __init__(self):
        self.devices = []

    def add_device(self, serial: str, name: str) -> None:
        # Проверка уникальности серийного номера (вариант 5)
        if any(d["serial"] == serial for d in self.devices):
            raise ValueError(f"Serial {serial} already exists")
        self.devices.append({"serial": serial, "name": name})

    def remove_device(self, serial: str) -> None:
        self.devices = [d for d in self.devices if d["serial"] != serial]

    def find(self, serial: str):
        for d in self.devices:
            if d["serial"] == serial:
                return d
        return None

    def count(self) -> int:
        return len(self.devices)


if __name__ == "__main__":
    inv = Inventory()
    inv.add_device("A1", "PC")
    print(inv.devices)