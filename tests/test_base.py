from app import app
import unittest
import json
import datetime


class TestsStart(unittest.TestCase):

    def setUp(self):
         self.app = app.test_client()
        
    def test_if_can_get_users(self):
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)


    def test_if_can_get_redflags(self):
        response = self.app.get('/api/v1/red-flags')
        self.assertEqual(response.status_code, 200)

    # def test_redflag_not_json(self):
    #     """ Test redflag content to be posted not in json format """
    #     expectedreq = {
    #         'incident_type': 'redflag/whistle blowing',
    #         'comment_description': 'officer taking a bribe',
    #         'status': 'under invesitagation',
    #         'current_location': 'mulago,bukoto street',
    #         'created': datetime.datetime.utcnow()
    #     }
    #     result = self.app.post(
    #         '/api/v1/red-flags',
    #         content_type = 'text/html',
    #         data=json.dumps(expectedreq)
    #     )
    #     self.assertEqual(result.status_code,401)
    #     self.assertIn('Content-type must be application/json',str(result.data))
    # def test_create_user_request_not_json(self):
    #     """ Test redflag content to be posted not in json format """
    #     expectedreq = {
    #          'incident_type': 'government intervention/broken bridge',
    #         'comment_description': 'river rwizi bridge had broken down',
    #         'status': 'ressolved',
    #         'current_location': 'kashanyarazi, mbarara',
    #         'created': datetime.datetime.utcnow()
    #     }
    #     result = self.app.post(
    #         '/api/v1/users',
    #         content_type = 'text/html',
    #         data=json.dumps(expectedreq)
    #     )
    #     self.assertEqual(result.status_code,401)
    #     self.assertIn('Content-type must be application/json',str(result.data))

if __name__ == "__main__":
    unittest.main()
