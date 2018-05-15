from flask_restful import Resource, reqparse
from Model import EmployInfoTest

class EmployInfoResource(Resource):
    def get(self, keyword=None):
        '''
        获取招聘信息
        keyword: 搜索关键字
        返回1代表获取成功，返回-1代表无数据
        '''
        all_data = []
        page_size = 10
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, help='Find [page_index] data')
        args = parser.parse_args()
        page_index = 1 if args['page'] is None else args['page']
        if keyword:
            jobs = EmployInfoTest.query.filter(EmployInfoTest.positionName.ilike('%{}%'.format(keyword))).order_by(EmployInfoTest.createTime.desc())
        else:
            jobs = EmployInfoTest.query
        length = jobs.count()
        jobs = jobs.limit(page_size).offset((page_index-1)*page_size)
        for job in jobs:
            all_data.append(job.getData())
        if all_data:
            return {'status': '1', 'allnums': length, 'data': all_data}, 200
        else:
            return {'status': '-1'}
