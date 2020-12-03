import unittest
from app import app


class TweetsResourceTests(unittest.TestCase):
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
        url_case = ["/api", "/", "/api/tw", "/tweets"]

        for url in url_case:
            # Act
            result = self.app.get(url)
            result_json = result.get_json()

            # Assert
            self.assertEqual(result_json["tweets"], [])
            self.assertEqual(
                result_json["message"], "Oops, looks like you got the wrong address"
            )
            self.assertFalse(result_json["success"])
            self.assertEqual(result.status_code, 404)

    def test_error_400(self):
        # Arrange
        url_case = [
            "api/tweets/tweet",
            "api/tweets/source",
            "api/tweets/date",
            "api/tweets/author",
            "api/tweets/location",
        ]

        for url in url_case:
            # Act
            result = self.app.get(url)
            result_json = result.get_json()

            # Assert
            self.assertEqual(
                result_json["message"],
                "The browser (or proxy) sent a request that this server could not understand.",
            )
            self.assertEqual(result.status_code, 400)

    ############################################################
    ###################### Resource Paths ######################
    ############################################################

    def test_tweets_getAll(self):
        # Arrange
        url = "/api/tweets/1"

        # Act
        result = self.app.get(url)
        result_json = result.get_json()

        # Assert
        self.assertTrue("tweets" in result_json)
        self.assertEqual(result_json["message"], "")
        self.assertTrue(result_json["success"])
        self.assertEqual(result.status_code, 200)

    def test_tweets_search_byMessage(self):
        # Arrange
        url_case = [
            "/api/tweets/tweet?query=test",
            "/api/tweets/tweet?query=",
            "/api/tweets/tweet?query=test&bad=asdsa",
            "/api/tweets/tweet?query=test&bad",
        ]

        for url in url_case:
            # Act
            result = self.app.get(url)
            result_json = result.get_json()

            # Assert
            self.assertTrue("tweets" in result_json)
            self.assertEqual(result_json["message"], "")
            self.assertTrue(result_json["success"])
            self.assertEqual(result.status_code, 200)

    def test_tweets_search_byAuthor(self):
        # Arrange
        url_case = [
            "/api/tweets/author?query=test",
            "/api/tweets/author?query=",
            "/api/tweets/author?query=test&bad=asdsa",
            "/api/tweets/author?query=test&bad",
        ]

        for url in url_case:
            # Act
            result = self.app.get(url)
            result_json = result.get_json()

            # Assert
            self.assertTrue("tweets" in result_json)
            self.assertEqual(result_json["message"], "")
            self.assertTrue(result_json["success"])
            self.assertEqual(result.status_code, 200)

    def test_tweets_search_bySource(self):
        # Arrange
        url_case = [
            "/api/tweets/source?query=test",
            "/api/tweets/source?query=",
            "/api/tweets/source?query=test&bad=asdsa",
            "/api/tweets/source?query=test&bad",
        ]

        for url in url_case:
            # Act
            result = self.app.get(url)
            result_json = result.get_json()

            # Assert
            self.assertTrue("tweets" in result_json)
            self.assertEqual(result_json["message"], "")
            self.assertTrue(result_json["success"])
            self.assertEqual(result.status_code, 200)

    def test_tweets_search_byDate(self):
        # Arrange
        url_case = [
            "/api/tweets/date?query=test",
            "/api/tweets/date?query=",
            "/api/tweets/date?query=test&bad=asdsa",
            "/api/tweets/date?query=test&bad",
        ]

        for url in url_case:
            # Act
            result = self.app.get(url)
            result_json = result.get_json()

            # Assert
            self.assertTrue("tweets" in result_json)
            self.assertEqual(result_json["message"], "")
            self.assertTrue(result_json["success"])
            self.assertEqual(result.status_code, 200)

    def test_tweets_search_byLocation(self):
        # Arrange
        url_case = [
            "/api/tweets/location?query=test",
            "/api/tweets/location?query=",
            "/api/tweets/location?query=test&bad=asdsa",
            "/api/tweets/location?query=test&bad",
        ]

        for url in url_case:
            # Act
            result = self.app.get(url)
            result_json = result.get_json()

            # Assert
            self.assertTrue("tweets" in result_json)
            self.assertEqual(result_json["message"], "")
            self.assertTrue(result_json["success"])
            self.assertEqual(result.status_code, 200)

