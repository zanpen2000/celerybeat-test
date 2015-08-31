from celery import Celery

app = Celery('tasks', broker='redis://192.168.2.123:6379/1')
app.config_from_object('celeryconfig')

@app.task
def add(x,y,**kwargs):
    if 'taskid' in kwargs.keys():
        print kwargs['taskid']
    return x+y

@app.task
def test():
    print 'test task'
    return "this is a test function."
