from django.test import TestCase, Client
from rest_framework import status
from .models import Task
from .tasks import update_task_status

class TaskAPITestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_create_task(self):
        response = self.client.post('/api/task/create/', {
            'title': 'Test Task',
            'description': 'This is a test task',
            'owner_email': 'owner@example.com',
            'creator_email': 'creator@example.com',
            'priority': '2',
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

    def test_get_task(self):
        task = Task.objects.create(
            title='Test Task',
            description='This is a test task',
            owner_email='owner@example.com',
            creator_email='creator@example.com',
            priority='2',
        )

        response = self.client.get(f'/api/task/get/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_list_tasks(self):
        Task.objects.create(
            title='Task 1',
            description='This is task 1',
            owner_email='owner@example.com',
            creator_email='creator@example.com',
            priority='1',
        )
        Task.objects.create(
            title='Task 2',
            description='This is task 2',
            owner_email='owner@example.com',
            creator_email='creator@example.com',
            priority='0',
        )

        response = self.client.get('/api/task/list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_delete_task(self):
        task = Task.objects.create(
            title='Task 1',
            description='Description for Task 1',
            owner_email='owner@example.com',
            creator_email='creator@example.com',
            priority='0',
        )

        response = self.client.delete(f'/api/task/delete/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 0)
