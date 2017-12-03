""" This is a class defining the REST API interface to access the 'Datasets'
    uploaded to the database. There should be the ability to GET, POST, PUT,
    and DELETE to the 'Datasets' table in the database.
"""

from flask import abort
from flask_restful import Resource, request
from cadetapi.models import ResultSet
from cadetapi.controllers.database.DbControl import DbResult

class TestAnalysis(Resource):
    def get(self, result_id):
        # Retrieve comments from database
        inst = DbResult()
        result = inst.GetAnalysis(result_id)
        return result
        # return result dict and 204 code if empty
        if (result):
            return result
        else:
            return result, 204


    def post(self):
        # Receive single comment as json object (primarily for unit testing)
        record = DbResult()
        req = request.get_json()
        pk = record.StoreAnalysis(
                req['resultset_id'],
                req['results'],
            )
        response = {}
        response['resultset_id'] = pk
        return response

"""
    def get(self, dataset_id=None):
        if dataset_id:
            dataset = DataSet.query.get(dataset_id)
            if not dataset:
                abort(404)
            return dataset
        else:
            datasets = DataSet.query.all()
            return datasets
"""
