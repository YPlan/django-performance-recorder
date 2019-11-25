import django
import pytest
from django.db.models import Q
from django.test import SimpleTestCase

from django_perf_rec.orm import patch_ORM_to_be_deterministic


class PatchORMToBeDeterministicTests(SimpleTestCase):
    def test_call_it(self):
        patch_ORM_to_be_deterministic()

    def test_call_it_again(self):
        patch_ORM_to_be_deterministic()

    @pytest.mark.skipif(django.VERSION < (2, 0), reason="Django 2.0+")
    def test_q_connector(self):
        q = Q(foo="bar") | Q(bar="foo")
        _, _, kwargs = q.deconstruct()
        self.assertEqual(kwargs, {"_connector": "OR"})
