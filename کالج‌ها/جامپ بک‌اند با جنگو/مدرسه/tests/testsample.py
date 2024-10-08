from django.test import TestCase
from rest_framework import serializers

from classes.models import Classroom
from classes.serializers import ClassroomSerializer


class ProductTest(TestCase):
    def test_serializer_baseclass(self):
        baseclass = ClassroomSerializer.__base__
        expected = serializers.ModelSerializer
        self.assertEqual(baseclass, expected, '\nکلاس ClassroomSerializer باید از کلاس ModelSerializer ارث‌بری کند.')

    def test_serializer_model(self):
        model = getattr(ClassroomSerializer.Meta, 'model', None)
        expected = Classroom
        self.assertEqual(model, expected, '\nسریالایزر ایجاد شده باید بر مبنای مدل Classroom باشد.')