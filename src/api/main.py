from api.app import JobApplication
from api.request_handlers.job import JobHandler
import tornado


if __name__ == "__main__":
    app = JobApplication(((r'/jobs/?', JobHandler),(r'/jobs/(\d+)/?', JobHandler)),)
    app.listen(5150)
    tornado.ioloop.IOLoop.current().start()

