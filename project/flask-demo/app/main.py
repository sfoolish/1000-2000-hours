from flask import Flask, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["MONGO2_HOST"] = "mongodb"
app.config["MONGO2_PORT"] = 27017
app.config["MONGO2_DBNAME"] = "students_db"
# app.config["MONGO2_DBPASSWORD"] = "tsppass"

mongo = PyMongo(app, config_prefix='MONGO2')
APP_URL = "http://192.168.99.100:5000"


class Student(Resource):
    def get(self, registration=None, department=None):
        data = []
        print "sssss#####\n"
        if registration:
            studnet_info = mongo.db.student.find_one({"registration": registration}, {"_id": 0})
            if studnet_info:
                return jsonify({"status": "ok", "data": studnet_info})
            else:
                return {"response": "no student found for {}".format(registration)}

        elif department:
            cursor = mongo.db.student.find({"department": department}, {"_id": 0}).limit(10)
            for student in cursor:
                student['url'] = APP_URL + url_for('students') + "/" + student.get('registration')
                data.append(student)

            return jsonify({"department": department, "response": data})

        else:
            cursor = mongo.db.student.find({}, {"_id": 0, "update_time": 0}).limit(10)

            for student in cursor:
                print student
                student['url'] = APP_URL + url_for('students') + "/" + student.get('registration')
                data.append(student)

            return jsonify({"response": data})

    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return jsonify(data)
        else:
            registration = data.get('registration')
            if registration:
                if mongo.db.student.find_one({"registration": registration}):
                    return {"response": "student already exists."}
                else:
                    mongo.db.student.insert(data)
            else:
                return {"response": "registration number missing"}

        return redirect(url_for("students"))

    def put(self, registration):
        data = request.get_json()
        mongo.db.student.update({'registration': registration}, {'$set': data})
        return redirect(url_for("students"))

    def delete(self, registration):
        mongo.db.student.remove({'registration': registration})
        return redirect(url_for("students"))


class Index(Resource):
    def get(self):
        return redirect(url_for("students"))


api = Api(app)
api.add_resource(Index, "/", endpoint="index")
api.add_resource(Student, "/api", endpoint="students")
api.add_resource(Student, "/api/<string:registration>", endpoint="registration")
api.add_resource(Student, "/api/department/<string:department>", endpoint="department")


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
