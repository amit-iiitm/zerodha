from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    "poll_SO": {
        "task": "stocks_scraper.stocks",
        "schedule": timedelta(seconds=30),
        "args": []
    }
}
