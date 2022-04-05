import json
import unittest
from manage import app, db


CONTENT_TYPE = 'application/json'


class TestTask(unittest.TestCase):
    def setUp(self):
        app.testing = True
        
        self.client = app.test_client()
        db.create_all()


    def test_form_parameter(self):
        response = self.client.post('/task', data = json.dumps(dict()))
        err_msg = json.loads(response.data).get('_schema')
        self.assertEqual(response.status_code, 422)
        self.assertEqual(err_msg,  ['Invalid input type.'])


    def test_empty_parameter(self):
        response = self.client.post('/task', data = json.dumps(dict()), content_type=CONTENT_TYPE)
        err_msg = json.loads(response.data).get('status')
        self.assertEqual(response.status_code, 422)
        self.assertEqual(err_msg, ['Missing data for required field.'])
        

    def test_wrong_type_parameter(self):
        response = self.client.post('/task', data = json.dumps({'name': 'pull report daily', 'status': 'wrong'}), content_type=CONTENT_TYPE)
        err_msg = json.loads(response.data).get('status')
        self.assertEqual(response.status_code, 422)
        self.assertEqual(err_msg,  ['Not a valid boolean.'])

    
    def test_task_post(self):
        response = self.client.post('/task', data = json.dumps({'name': 'pull report daily', 'status': False}), content_type=CONTENT_TYPE)
        resp_json = json.loads(response.data).get('result')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(resp_json['name'], 'pull report daily')
        self.assertNotEqual(resp_json['status'], True)
        self.assertIsNotNone(resp_json['id'])


    def test_task_deletion(self):
        response = self.client.delete('/task/-1000')
        err_msg = json.loads(response.data).get('err_msg')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(err_msg,  'task id not found')

        response = self.client.delete('/task/1')
        self.assertEqual(response.status_code, 200)


    
    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()