import unittest
from app import app


class LiveBluePrintTests(unittest.TestCase):
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
        url_case = ["live/live", "live/another", "live/tweets"]

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
    ###################### Paths Response ######################
    ############################################################

    def test_live_root_active(self):
        # Arrange
        url = "/live/"

        # Act
        result = self.app.get(url)

        # Assert
        self.assertEqual(result.status_code, 200)
