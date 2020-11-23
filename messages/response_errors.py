ERROR_NOT_FOUND = (
    {
        "tweets": [],
        "message": "No tweets found under this identifier.",
        "success": False,
    },
    404,
)

ERROR_JSON_FORMAT_INCORRECT = (
    {"message": "Incorrect JSON format", "success": False},
    400,
)

ERROR_FLAG_INCORRECT = ({"message": "Incorrect flag sent", "success": False}, 400)
