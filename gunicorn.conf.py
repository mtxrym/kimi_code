import multiprocessing

bind = "unix:/opt/fastapi-app/app.sock"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 120
keepalive = 5
errorlog = "/var/log/gunicorn/error.log"
accesslog = "/var/log/gunicorn/access.log"
capture_output = True
enable_stdio_inheritance = True
