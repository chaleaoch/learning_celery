# -*- coding: UTF-8 -*-

from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('proj',
             # backend='redis://192.168.31.254:6379', broker='amqp://guest@192.168.31.254:5672//',
             backend='redis://192.168.31.254:6379', broker='redis://192.168.31.254:6379/0',
             include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
    task_routes={
        'tasks.add': {'queue': 'hipri'},
    },
)
app.conf.timezone = 'Europe/London'

if __name__ == '__main__':
    app.start()
