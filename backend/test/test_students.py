from api import app
import unittest, json
from unittest.mock import patch
from models import student


class test_students(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client

    @patch('api.students.student.create_student')
    def test_students_fetch_none(self, mock_create_student):
        input_student = json.dumps(dict(
            name="Rami"
        ))

        response = self.client().post('/student',
                                      data=input_student,
                                      content_type='application/json')

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Student Rami has been created successfully.')
        self.assertTrue(mock_create_student.called)

    @patch('api.students.student.fetch_all')
    @patch('api.students.student.create_student')
    def test_students_fetch_all(self, mock_create_student, mock_fetch_all):
        students = []
        students.append(student.student('Rami'))
        mock_fetch_all.return_value = students
        response = self.client().get('/student',
                                      content_type='application/json')

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['count'], 1)

if __name__ == '__main__':
    unittest.main() 
