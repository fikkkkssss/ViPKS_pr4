import unittest
from inventory import Inventory


class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory()

    def test_add_device(self):
        self.inv.add_device("A1", "PC")
        self.assertEqual(self.inv.count(), 1)

    def test_add_multiple(self):
        self.inv.add_device("A1", "PC")
        self.inv.add_device("A2", "Laptop")
        self.assertEqual(self.inv.count(), 2)

    def test_remove_device(self):
        self.inv.add_device("A1", "PC")
        self.inv.remove_device("A1")
        self.assertEqual(self.inv.count(), 0)

    def test_remove_missing_is_noop(self):
        self.inv.remove_device("NOPE")
        self.assertEqual(self.inv.count(), 0)

    def test_find_existing(self):
        self.inv.add_device("A1", "PC")
        self.assertEqual(self.inv.find("A1")["name"], "PC")

    def test_find_missing_returns_none(self):
        self.assertIsNone(self.inv.find("NOPE"))

    def test_device_name_stored(self):
        self.inv.add_device("A1", "PC")
        self.assertEqual(self.inv.devices[0]["name"], "PC")

    def test_device_serial_stored(self):
        self.inv.add_device("A1", "PC")
        self.assertEqual(self.inv.devices[0]["serial"], "A1")

    def test_count_zero_initially(self):
        self.assertEqual(self.inv.count(), 0)

    # КЛЮЧЕВОЙ ТЕСТ ВАРИАНТА 5
    def test_serial_number_is_unique(self):
        self.inv.add_device("A1", "PC")
        with self.assertRaises(ValueError):
            self.inv.add_device("A1", "Laptop")


if __name__ == "__main__":
    unittest.main()