from unittest.mock import patch
from django.core.management import call_command
from django.test import TestCase
from notification.models import NotificationType, Rule


class TestPopulateDatabase(TestCase):
    def test_populate_database(self):
        call_command("populate_database")
        self.assertEqual(NotificationType.objects.count(), 3)
        self.assertEqual(Rule.objects.count(), 3)
