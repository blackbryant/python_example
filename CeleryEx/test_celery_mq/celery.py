from celery import Celery



app = Celery("test_celery",
      broker='amqp://test:test123@localhost/test_vhost',
      backend='rpc://',
      include=['test_celery.tasks'])