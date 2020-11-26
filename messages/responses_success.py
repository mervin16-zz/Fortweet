SUCCESS_TWEETS_STARTED = (
    {"message": "Live tweets capturing has started", "success": True},
    200,
)


def SUCCESS_TWEETS_RETURNED(tweets):
    return ({"tweets": tweets, "message": "", "success": True,}, 200)


def SUCCESS_AUTHENTICATED(access_token, refresh_token):
    return (
        {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "success": True,
        },
        200,
    )

