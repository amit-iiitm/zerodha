from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    "poll_SO": {
        "task": "stack_scrap_modified.questions",
        "schedule": timedelta(seconds=30),
        "args": []
    }
}
