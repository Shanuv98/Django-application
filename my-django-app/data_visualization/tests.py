from django.test import TestCase
from django.urls import reverse
from .models import DataPoint

class DataVisualizationTestCase(TestCase):
    def setUp(self):
        self.data_point = DataPoint.objects.create(date='2024-06-15', value=50.0)

    def test_data_point_creation(self):
        self.assertEqual(self.data_point.date, '2024-06-15')
        self.assertEqual(self.data_point.value, 50.0)

    def test_chart_view(self):
        url = reverse('chart_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'data_visualization/chart.html')

    def test_add_data_point(self):
        url = reverse('add_data_point')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        data = {
            'date': '2024-06-16',
            'value': 60.0
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission

        new_data_point = DataPoint.objects.last()
        self.assertEqual(new_data_point.date, '2024-06-16')
        self.assertEqual(new_data_point.value, 60.0)
