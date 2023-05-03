from celery import Celery

#app = Celery(<module_name>, broker="<broker_url>", backend="<backend_url>")
app = Celery('tasks', broker='redis://localhost/')
@app.task
def hello_world(name: str):
    if name is not None:
        return f"hello {name}"
    else:
        return "hello world"

