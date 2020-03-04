# -*- coding: UTF-8 -*-

broker_url = 'amqp://guest@192.168.31.254:5672//'
result_backend = 'redis://192.168.31.254:6379'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True

task_routes = {
    'tasks.add': 'low-priority',
}

task_annotations = {
    'tasks.add': {'rate_limit': '10/m'}
}

# celery -A tasks control rate_limit tasks.add 10/m
