import unittest
from app import app


class AdminBlueprintTests(unittest.TestCase):
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
    ###################### Paths Response ######################
    ############################################################

    def test_admin_dashboard_active(self):
        # Arrange
        url = "/admin/dashboard"

        # Act
        result = self.app.get(url)

        # Assert
        self.assertEqual(result.status_code, 200)

    def test_admin_analysis_active(self):
        # Arrange
        url = "/admin/analysis"

        # Act
        result = self.app.get(url)

        # Assert
        self.assertEqual(result.status_code, 200)

    def test_admin_manage_active(self):
        # Arrange
        url = "/admin/manage"

        # Act
        result = self.app.get(url)

        # Assert
        self.assertEqual(result.status_code, 200)

    def test_admin_settings_active(self):
        # Arrange
        url = "/admin/settings"

        # Act
        result = self.app.get(url)

        # Assert
        self.assertEqual(result.status_code, 200)

    def test_admin_add_get_active(self):
        # Arrange
        url = "/admin/add"

        # Act
        result = self.app.get(url)

        # Assert
        self.assertEqual(result.status_code, 200)
