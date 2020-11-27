import unittest
import json
from app import app


class AdminResourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    ############################################################
    ###################### Error Handling ######################
    ############################################################

    def test_error_404(self):
        # Arrange
        url_case = ["/admin", "/", "/admin/mana"]

        for url in url_case:
            # Act
            result = self.app.get(url)
            result_json = result.get_json()

            # Assert
            self.assertEqual(result_json["tweets"], [])
            self.assertEqual(
                result_json["message"], "No tweets found under this identifier."
            )
            self.assertFalse(result_json["success"])
            self.assertEqual(result.status_code, 404)

    ############################################################
    ###################### Resource Paths ######################
    ############################################################

    def test_admin_auth_getRequest(self):
        # Arrange
        url = "/fortauth"

        # Act
        result = self.app.get(url)
        result_json = result.get_json()

        # Assert
        self.assertEqual(
            result_json["message"], "The method is not allowed for the requested URL."
        )
        self.assertEqual(result.status_code, 405)

    def test_admin_auth_postInvalidUsernameParameter(self):
        # Arrange
        url = "/fortauth"
        headers = {"Content-Type": "application/json"}
        data = {"user": "us", "pass": "pass"}

        # Act
        result = self.app.post(url, data=json.dumps(data), headers=headers)
        result_json = result.get_json()

        # Assert
        self.assertEqual(
            result_json["message"]["username"], "This field cannot be blank"
        )
        self.assertEqual(result.status_code, 400)

    def test_admin_auth_postInvalidPasswordParameter(self):
        # Arrange
        url = "/fortauth"
        headers = {"Content-Type": "application/json"}
        data = {"username": "us", "passw": "pass"}

        # Act
        result = self.app.post(url, data=json.dumps(data), headers=headers)
        result_json = result.get_json()

        # Assert
        self.assertEqual(
            result_json["message"]["password"], "This field cannot be blank"
        )
        self.assertEqual(result.status_code, 400)

    def test_admin_auth_postInvalidCredentials(self):
        # Arrange
        url = "/fortauth"
        headers = {"Content-Type": "application/json"}
        data = {"username": "nada", "password": "nada"}

        # Act
        result = self.app.post(url, data=json.dumps(data), headers=headers)
        result_json = result.get_json()

        # Assert
        self.assertEqual(result_json["message"], "Invalid credentials")
        self.assertFalse(result_json["success"])
        self.assertEqual(result.status_code, 401)

    def test_admin_auth_postEmptyCredentials(self):
        # Arrange
        url = "/fortauth"
        headers = {"Content-Type": "application/json"}
        data = {"username": "nada", "password": "nada"}

        # Act
        result = self.app.post(url, data=json.dumps(data), headers=headers)
        result_json = result.get_json()

        # Assert
        self.assertEqual(result_json["message"], "Invalid credentials")
        self.assertFalse(result_json["success"])
        self.assertEqual(result.status_code, 401)

    def test_admin_manage_withoutAuthorizationHeader(self):
        # Arrange
        url = "/admin/manage"

        # Act
        result = self.app.get(url)
        result_json = result.get_json()

        # Assert
        self.assertEqual(result_json["msg"], "Missing Authorization Header")
        self.assertEqual(result.status_code, 401)

    def test_admin_manage_withBadHeader(self):
        # Arrange
        url = "/admin/manage"
        headers = {"Authorization": "Bearer"}

        # Act
        result = self.app.get(url, headers=headers)
        result_json = result.get_json()

        print(f"results {result_json}")

        # Assert
        self.assertEqual(
            result_json["msg"],
            "Bad Authorization header. Expected value 'Bearer <JWT>'",
        )
        self.assertEqual(result.status_code, 422)
