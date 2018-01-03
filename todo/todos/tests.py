from django.test import TestCase
from todos.models import ToDo, List
from datetime import datetime
from django.contrib.auth.models import User

class ToDosTestcase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jacob', email='jacob@orr.org', password='top_secret')
        self.list = List.objects.create(name="test")
        self.list_2 = List.objects.create(name="weel")

    def test_todoname(self):
        self.assertEqual(self.list.name, "test")
    
    def test_user_created(self):
        self.assertIsNotNone(self.user)

    def test_list_created(self):
        self.assertIsNotNone(self.list)

    def test_list2_created(self):
        self.assertIsNotNone(self.list_2)
    
    def test_user(self):
        self.assertEqual(self.user.username, "jacob")

    def test_user_id_pk(self):
        self.assertEqual(self.user.id, self.user.pk)

    def test_list_id_pk(self):
        self.assertEqual(self.list.id, self.list.pk)

    def test_list_id_not_equal(self):
        self.assertNotEqual(self.list.id, 2)

    def test_lists_not_equal(self):
        self.assertNotEqual(self.list.name, self.list_2.name)

    def test_list1lees(self):
        self.assertTrue(self.list.id < self.list_2.id)
