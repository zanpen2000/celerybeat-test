CELERY_RESULT_BACKEND = 'redis://192.168.2.123:6379/1'

CELERY_MONGODB_SCHEDULER_DB = "test"
CELERY_MONGODB_SCHEDULER_COLLECTION = "celery_beat_schedule"
CELERY_MONGODB_SCHEDULER_URL = "mongodb://192.168.2.123:27017"


CELERYBEAT_SCHEDULE = {
    'add-task':{
        'task':'tasks.add',
        'schedule':10,
        'args':(100,100),
        'kwargs':{'taskid':'123'},
    },
    'test-task':{
        'task':'tasks.test',
        'schedule':10,
        'args':(),
        'kwargs':{},
    }

}
