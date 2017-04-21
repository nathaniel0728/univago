'''
	API for Colleges
'''

from flask import Flask, jsonify
from colleges import updateCollege

app = Flask(__name__)

#app.config["MONGO_DBNAME"] = "collegeApi"
#app.config["MONGO_URL"] = "mongodb://localhost:27017/collegeApi"

#mongo = PyMongo(app)

#c = mongo.db.colleges

'''
colleges = [
	{
		'id':1,
		'name': u'Berkeley',
		'visits':{"09-11-2001":"Information Session"},
		'address': u'UC Berkeley',
		'zipcode': u'22101',
		'hotels': ['Hotel #1', 'Hotel #2'],
	},
	{
		'id':1,
		'name': u'Alabama University',
		'visits':{"09-11-2001":"Information Session"},
		'address': u'Alabama University',
		'zipcode': u'35487',
		'hotels': ['Hotel #1', 'Hotel #2'],
	}

]
'''

with app.app_context():
        

    @app.route("/college/api/v1.0/getCollegeList", methods=['GET'])
    def getColleges():
        collegeList = []
        for college in colleges:
            collegeList.append(college["name"])
        return jsonify({'data': collegeList})

    @app.route("/college/api/v1.0/getCollegeData", methods=['GET'])
    def hello_world():
        #return jsonify("{}")
        return jsonify({'data': colleges})

    if __name__ == "__main__":
        colleges = updateCollege()
        #mongo.db.colleges.insert_one({"store": colleges})
        print(colleges)
        app.run(port=3000)




