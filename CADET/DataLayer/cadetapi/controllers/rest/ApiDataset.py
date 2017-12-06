""" This is a class defining the REST API interface to access the 'Datasets'
    uploaded to the database. There should be the ability to GET, POST, PUT,
    and DELETE to the 'Datasets' table in the database.
"""

from flask import abort
from flask_restful import Resource, request
#from cadetapi.models import DataSet
from cadetapi.controllers.database.DbControl import DbDataset
from cadetapi.schemas import DatasetSchema

class DatasetApi(Resource):
    def get(self, dataset_id=None):
        # Retrieve datasets from database
        inst = DbDataset()
        response = inst.Query(dataset_id)

        # marshall dataset(s) into dict
        if dataset_id is None:
            result = DatasetSchema(many=True).dump(response).data
        else:
            result = DatasetSchema(many=False).dump(response).data

        # return result dict and 204 code if empty
        if (result):
            return result
        else:
            return result, 204


    def post(self):
        NewDataset = DbDataset()
        response = {}
        response = NewDataset.GetId(request.get_json()['raw_file_stats'])
        return response, 201

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
