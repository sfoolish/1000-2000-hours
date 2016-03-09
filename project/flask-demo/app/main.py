import threading
# import ssh

from flask import Flask, jsonify, url_for, redirect, request, render_template
from flask_pymongo import PyMongo
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["MONGO2_HOST"] = "mongodb"
app.config["MONGO2_PORT"] = 27017
app.config["MONGO2_DBNAME"] = "students_db"
# app.config["MONGO2_DBPASSWORD"] = "tsppass"

global_thread = None

mongo = PyMongo(app, config_prefix='MONGO2')
APP_URL = "http://192.168.99.100:5000"

# def exec_yardstick_cmd():
#     user = "root"
#     ip = "yardstick"
#     key_filename = None
#     connection = ssh.SSH(user, ip, key_filename=key_filename) 
#     connection.wait()

#     # TODO add stderr check
#     exit_status, stdout, stderr = connection.execute(
#         "sleep 20; yardstick -h")
#     app.logger.info("yardstick output: %r" % stdout)

# class Student(Resource):
#     def get(self, registration=None, department=None):
#         data = []
#         if registration:
#             studnet_info = mongo.db.student.find_one({"registration": registration}, {"_id": 0})
#             if studnet_info:
#                 return jsonify({"status": "ok", "data": studnet_info})
#             else:
#                 return {"response": "no student found for {}".format(registration)}

#         elif department:
#             cursor = mongo.db.student.find({"department": department}, {"_id": 0}).limit(10)
#             for student in cursor:
#                 student['url'] = APP_URL + url_for('students') + "/" + student.get('registration')
#                 data.append(student)

#             return jsonify({"department": department, "response": data})

#         else:
#             cursor = mongo.db.student.find({}, {"_id": 0, "update_time": 0}).limit(10)

#             for student in cursor:
#                 print student
#                 student['url'] = APP_URL + url_for('students') + "/" + student.get('registration')
#                 data.append(student)

#             return jsonify({"response": data})

#     def post(self):
#         global global_thread
#         global_thread = threading.Thread(target=exec_yardstick_cmd, name='yardstick')
#         global_thread.start()
#         data = request.get_json()
#         if not data:
#             data = {"response": "ERROR"}
#             return jsonify(data)
#         else:
#             registration = data.get('registration')
#             if registration:
#                 if mongo.db.student.find_one({"registration": registration}):
#                     return {"response": "student already exists."}
#                 else:
#                     mongo.db.student.insert(data)
#             else:
#                 return {"response": "registration number missing"}

#         return redirect(url_for("students"))

#     def put(self, registration):
#         global global_thread
#         if global_thread != None:
#             # join with timeout 0 to check if thread task is finished
#             global_thread.join(0)
#             if global_thread.isAlive() == True:
#                 app.logger.info("thread is still running...")
#             else:
#                 global_thread = None
#         data = request.get_json()
#         mongo.db.student.update({'registration': registration}, {'$set': data})
#         return redirect(url_for("students"))

#     def delete(self, registration):
#         mongo.db.student.remove({'registration': registration})
#         return redirect(url_for("students"))


# class Index(Resource):
#     def get(self):
#         return redirect(url_for("students"))

# class Hello(Resource):
#     def get(self):
#         return render_template("hello.html", name="abc")

import os
import random
import time
from flask import Flask, request, render_template, session, flash, redirect, \
    url_for, jsonify
from celery import Celery


app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def send_async_email(msg):
    """Background task to yardstick command."""
    with app.app_context():
        for i in xrange(10):
            time.sleep(1)
            app.logger.info("yardstick command running ...")

@celery.task(bind=True)
def long_task(self):
    """Background task that runs a long function with progress reports."""
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10, 50)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective),
                                              random.choice(noun))
        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': total,
                                'status': message})
        time.sleep(1)
    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': 42}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', email=session.get('email', ''))
    email = request.form['email']
    session['email'] = email

    # send the email
    msg = 'This is a test email sent from a background Celery task.'
    if request.form['submit'] == 'Send':
        # send right away
        send_async_email.delay(msg)
        flash('Sending email to {0}'.format(email))
    else:
        # send in one minute
        send_async_email.apply_async(args=[msg], countdown=60)
        flash('An email will be sent to {0} in one minute'.format(email))

    return redirect(url_for('index'))


@app.route('/longtask', methods=['POST'])
def longtask():
    task = long_task.apply_async()
    return jsonify({}), 202, {'Location': url_for('taskstatus',
                                                  task_id=task.id)}


@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)


# api = Api(app)
# api.add_resource(Index, "/", endpoint="index")
# api.add_resource(Student, "/api", endpoint="students")
# api.add_resource(Student, "/api/<string:registration>", endpoint="registration")
# api.add_resource(Student, "/api/department/<string:department>", endpoint="department")
# api.add_resource(Hello, "/hello", endpoint="hello")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

# http://salmanwahed.github.io/2015/05/01/flask-restful-mongodb-api/
#
# curl -v http://192.168.99.100:5000/api
# curl -v -X POST -H "Content-Type: application/json" http://192.168.99.100:5000/api -d '{"name": "Example Name", "registration": "123433199", "department": "cse"}'
# curl -v http://192.168.99.100:5000/api/123433199
# curl -v -X PUT -H "Content-Type: application/json" http://192.168.99.100:5000/api/123433199 -d '{"website": "www.example.com"}'
# curl -v http://192.168.99.100:5000/api/123433199
# curl -v -X DELETE http://192.168.99.100:5000/api/123433199
