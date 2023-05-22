workers = 1

threads = 4

bind = '127.0.0.1:8090'

worker_class = 'gevent'

worker_connections = 2000

pidfile = 'gunicorn.pid'

accesslog = './logs/gunicorn_acess.log'
errorlog  = './logs/gunicorn_error.log'

loglevel = 'info'

reload=True