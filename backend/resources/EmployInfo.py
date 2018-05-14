# from flask import request
from flask_restful import Resource, reqparse
from Model import EmployInfoTest

class EmployInfoResource(Resource):
    def get(self, keyword=None):
        all_data = []
        page_size = 10
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, help='Find [page_index] data')
        args = parser.parse_args()

        page_index = 1 if args['page'] is None else args['page']
        if keyword:
            for job in EmployInfoTest.query.filter(EmployInfoTest.positionName.ilike('%{}%'.format(keyword))).order_by(EmployInfoTest.createTime.desc()).limit(page_size).offset((page_index-1)*page_size):
                all_data.append(job.getData())
            return {'status': 'success', 'data': all_data}, 200
        else:
            for job in EmployInfoTest.query.limit(10).offset((page_index-1)*page_size):
                all_data.append(job.getData())
            return {'status': 'success', 'data': all_data}, 200
