# application.py, application.py
from flask import Flask, request
import json
# connection=MongoClient(host="localhost", port=27017)
# db=connection.test# connection,database name
# collection=db.employee
application = Flask(__name__)

@application.route("/",methods=["GET"])
def test():
    return "hello vcube students"
    # html code
    # css code

@application.route("/test",methods=['POST'])
def posttest():
    data = request.data
    data2=json.loads(data)
    n1=data2['number1']
    n2=data2['number2']
    n3=int(n1)+int(n2)

    #print(json.loads(data))
    return str(n3)


if __name__ == '__main__':
    application.run(host="0.0.0.0",port=5000)
