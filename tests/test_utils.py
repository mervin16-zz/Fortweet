import unittest
from app.helpers.utils import hash, tweets_to_list
from app.models.tweet import TweetModel


class TestUtils(unittest.TestCase):

    ############################################################
    ##################### Hashing Function #####################
    ############################################################

    def test_hashFunction_when_messageIsNotEmpty1Of3(self):
        # Arrange
        message = "This is a message"
        expected_result = (
            "a826c7e389ec9f379cafdc544d7e9a4395ff7bfb58917bbebee51b3d0b1c996a"
        )

        # Act
        result = hash(message)

        # Assert
        self.assertEqual(result, expected_result)

    def test_hashFunction_when_messageIsNotEmpty2Of3(self):
        # Arrange
        message = " This is a message "
        expected_result = (
            "1f6859fe5973f8411cc9c6f5555c6d43250662909660c0560e784ce0a1aca985"
        )

        # Act
        result = hash(message)

        # Assert
        self.assertEqual(result, expected_result)

    def test_hashFunction_when_messageIsNotEmpty3Of3(self):
        # Arrange
        message = "This is a Big MessAge"
        expected_result = (
            "69fcc28e2e974a4dda08b08b9145b21fa4d3c369432f1a93fc4d2c471eb78801"
        )

        # Act
        result = hash(message)

        # Assert
        self.assertEqual(result, expected_result)

    def test_hashFunction_when_messageIsEmpty(self):
        # Arrange
        message = ""
        expected_result = None

        # Act
        result = hash(message)

        # Assert
        self.assertEqual(result, expected_result)

    def test_hashFunction_when_messageIsNone(self):
        # Arrange
        message = ""
        expected_result = None

        # Act
        result = hash(message)

        # Assert
        self.assertEqual(result, expected_result)

    def test_tweetsToList_OneData(self):
        # Arrange
        tweets = [
            TweetModel(
                "PlayStation®Network",
                "ZeyRoC",
                "",
                "My Message",
                "2020-11-29 17:11:52",
                None,
            )
        ]

        # Act
        result = tweets_to_list(tweets)

        # Assert
        self.assertEqual(len(tweets), len(result))
        self.assertTrue(type(tweets), type(result))

    def test_tweetsToList_MultipleData(self):
        # Arrange
        tweets = [
            TweetModel(
                "PlayStation®Network",
                "ZeyRoC",
                "",
                "My Message",
                "2020-11-29 17:11:52",
                None,
            ),
            TweetModel(
                "PlayStation®Network",
                "ZeyRoC",
                "",
                "My Message",
                "2020-11-29 17:11:52",
                None,
            ),
            TweetModel(
                "PlayStation®Network",
                "ZeyRoC",
                "",
                "My Message",
                "2020-11-29 17:11:52",
                None,
            ),
            TweetModel(
                "PlayStation®Network",
                "ZeyRoC",
                "",
                "My Message",
                "2020-11-29 17:11:52",
                None,
            ),
        ]

        # Act
        result = tweets_to_list(tweets)

        # Assert
        self.assertEqual(len(tweets), len(result))
        self.assertTrue(type(tweets), type(result))

    def test_tweetsToList_NoData(self):
        # Arrange
        tweets = []

        # Act
        result = tweets_to_list(tweets)

        # Assert
        self.assertEqual(len(tweets), len(result))
        self.assertTrue(type(tweets), type(result))
