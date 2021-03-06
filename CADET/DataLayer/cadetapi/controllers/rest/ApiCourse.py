""" This is a class defining the REST API interface to access the 'Courses'
    uploaded to the database. There should be the ability to GET, POST, PUT,
    and DELETE to the 'Courses' table in the database.
"""

from flask import abort
from flask_restful import Resource, request
from ..database.DbControl import DbCourse
from ...schemas import CourseSchema

class CourseApi(Resource):
    def get(self, course_id=None):
        # Retrieve courses from database
        inst = DbCourse()
        response = inst.Query(course_id)

        # marshall course(s) into dict
        if course_id is None:
            result = CourseSchema(many=True).dump(response).data
        else:
            result = CourseSchema(many=False).dump(response).data

        # return result dict and 204 code if empty
        if (result):
            return result
        else:
            return result, 204

