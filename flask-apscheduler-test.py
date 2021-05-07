from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from flask_apscheduler import APScheduler

'''flask_apscheduler的JOBS可以在Config中配置，
也可以通过装饰器调用，还可以通过flask_apschedule的api进行添加
job stores 默认为内存， 可以下在flask的Config中配置为存储在数据库中
'''


class Config(object):
    # JOBS可以在配置里面配置
    JOBS = [{
        'id': 'job1',
        'func': 'app:job1',
        'args': (1, 2),
        'trigger': 'interval',
        'seconds': 10
    }]
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'  # 配置时区
    SCHEDULER_API_ENABLED = True  # 添加API
    # 配置job store
    # DATABASE_URL="mysql+pymysql://scott:xxxx@192.168.0.95:3306/test?charset=utf8mb4"
    # SCHEDULER_JOBSTORES = {
    #     'default': SQLAlchemyJobStore(url=DATABASE_URL)
    # }


# 初始化调度器
scheduler = APScheduler(BackgroundScheduler(timezone="Asia/Shanghai"))


def job1(a, b):
    print(str(a) + ' ' + str(b))


# 使用装饰器调用
@scheduler.task('interval', id='job_2', seconds=30, misfire_grace_time=900)
def job2():
    print('Job 2 executed')


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config())
    # it is also possible to enable the API directly
    scheduler.api_enabled = True
    scheduler.init_app(app)
    # scheduler.start()
    app.run(host='0.0.0.0', port=5000)