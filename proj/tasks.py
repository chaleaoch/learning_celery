# -*- coding: UTF-8 -*-

from __future__ import absolute_import, unicode_literals

from datetime import datetime

import celery

from proj import celery_app


@celery_app.task(name='tasks.mul')
def mul(x, y):
    return x * y


@celery_app.task(name='tasks.add')
def add(x, y):
    print(datetime.now())
    print(1233333333333333)
    # sleep(100)
    return x + y


@celery_app.task(name='tasks.xsum')
def xsum(numbers):
    return sum(numbers)


class MyTask(celery.Task):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('hhhhhhhhhhhhhhhhhhhhhhhh{0!r} failed: {1!r}'.format(task_id, exc))


# @celery_app.task(bind=True, base=MyTask, name='tasks.add')
# def add(self, x, y):
#     raise KeyError()


if __name__ == "__main__":
    add.delay(1, 2)
