import tornado
from tornado.web import RequestHandler
from api.app import JobApplication
from time import sleep
import asyncio

def worker(timeout: int):
    print('starting')
    sleep(timeout)
    print('DONE')

class JobHandler(RequestHandler):
    application: JobApplication

    def post(self):
        job_length = int(self.get_query_argument("job_length", "20"))
        future = self.application.executor.submit(worker, job_length)
        self.application.jobs[self.application.job_id] = future
        self.write(str(self.application.job_id))
        self.application.job_id += 1

    async def get(self, job_id: int):
        wait_time = int(self.get_query_argument("wait_time", "19"))
        done = asyncio.Event()
        loop = tornado.ioloop.IOLoop.current()

        def on_done(_):
            print("done! setting event")
            loop.add_callback(done.set)
        self.application.jobs[int(job_id)].add_done_callback(on_done)

        if self.application.jobs[int(job_id)].done():
            print("exiting because job is done")
            self.write("done!")
            return

        try:
            await asyncio.wait_for(done.wait(), timeout=wait_time)
            print("waited for event")
            self.write("done!")
            return

        except asyncio.TimeoutError:
            self.write("pending")

 
