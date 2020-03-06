# -*- coding: UTF-8 -*-

from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('proj',
             backend='redis://192.168.31.254:6379', broker='amqp://guest@192.168.31.254:5672//',
             include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
