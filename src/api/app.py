import tornado
from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor

class JobApplication(tornado.web.Application):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.executor = ThreadPoolExecutor()
        self.job_id = 0
        self.jobs: dict[int, Future] = {}
