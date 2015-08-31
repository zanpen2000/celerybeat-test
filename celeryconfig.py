CELERY_RESULT_BACKEND = 'redis://192.168.2.123:6379/1'

CELERY_MONGODB_SCHEDULER_DB = "test"
CELERY_MONGODB_SCHEDULER_COLLECTION = "celery_beat_schedule"
CELERY_MONGODB_SCHEDULER_URL = "mongodb://192.168.2.123:27017"


CELERYBEAT_SCHEDULE = {
    'test-task':{
        'task':'tasks.test',
        'schedule':10,
    }

}
