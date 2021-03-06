import unittest
import testing.postgresql as tpg

import utilities as util
from models.mouse import Mouse

import database.handlers.handlers
import database.seed_tables.seed_tables
from database.seed_tables.seeds import test_mouse_table_seed

mice_seed = set(test_mouse_table_seed)
Postgresql = tpg.PostgresqlFactory(cache_initialized_db=True,
                                   on_initialized=database.handlers.handlers.handler_create_mouse_table)


def tearDownModule():
    Postgresql.clear_cache()


class TestNewMouse(unittest.TestCase):
    birthdate = 20200527

    def setUp(self):
        self.postgresql = Postgresql()

    def tearDown(self):
        self.postgresql.stop()

    @unittest.skip("Not currently testing")
    def test_setUp_tearDown(self):
        self.assertTrue(1)

    def test_add_new_mouse(self):
        test_mouse = Mouse(1111, self.birthdate, 'wild type', 'female').save_to_db(testing=True,
                                                                                   postgresql=self.postgresql)
        self.assertEqual(1111, test_mouse.eartag)
        self.assertEqual(util.convert_date_int_yyyymmdd(self.birthdate), test_mouse.birthdate)
        self.assertEqual('wild type', test_mouse.genotype)
        self.assertEqual('female', test_mouse.sex)
        self.assertFalse(test_mouse.mouse_id is None)

    def test_duplicate_mouse(self):
        test_mouse = Mouse(1111, self.birthdate, 'wild type', 'female').save_to_db(testing=True,
                                                                                   postgresql=self.postgresql)
        dup_mouse = test_mouse.save_to_db(testing=True, postgresql=self.postgresql)
        self.assertFalse(dup_mouse.mouse_id is None)


class TestLoadDeleteMouse(unittest.TestCase):
    seed_tup = mice_seed.pop()

    def setUp(self):
        self.postgresql = Postgresql()
        database.handlers.handlers.handler_seed_mouse(self.postgresql)

    def tearDown(self):
        self.postgresql.stop()

    @unittest.skip("Not currently testing")
    def test_setUp_tearDown(self):
        self.assertTrue(1)

    def test_from_db(self):
        self.load_mouse = Mouse.from_db(self.seed_tup[0], testing=True, postgresql=self.postgresql)
        self.assertEqual(self.seed_tup[0], self.load_mouse.eartag)
        self.assertEqual(self.seed_tup[1], self.load_mouse.birthdate)
        self.assertEqual(self.seed_tup[2], self.load_mouse.genotype)
        self.assertEqual(self.seed_tup[3], self.load_mouse.sex)
        self.assertFalse(self.load_mouse.mouse_id is None)

    def test_delete_mouse(self):
        mouse_to_delete = Mouse.from_db(self.seed_tup[0], testing=True, postgresql=self.postgresql)
        mouse_to_delete.delete_from_db(testing=True, postgresql=self.postgresql)
        test_reload_mouse = Mouse.from_db(self.seed_tup[0], testing=True, postgresql=self.postgresql)
        self.assertIsNone(test_reload_mouse)


if __name__ == '__main__':
    unittest.main()
