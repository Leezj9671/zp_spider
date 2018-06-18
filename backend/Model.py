from sqlalchemy import Column, DateTime, Integer, String
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI


db = SQLAlchemy()


class EmployInfoTest(db.Model):
    __tablename__ = 'employ_info_test'

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255, 'utf8_bin'), nullable=False)
    companyFullName = db.Column(db.String(255, 'utf8_bin'), nullable=False)
    companyID = db.Column(db.Integer)
    companyShortName = db.Column(db.String(200, 'utf8_bin'))
    companySize = db.Column(db.String(100, 'utf8_bin'))
    createTime = db.Column(db.String(100, 'utf8_bin'))
    district = db.Column(db.String(50, 'utf8_bin'))
    education = db.Column(db.String(20, 'utf8_bin'))
    financeStage = db.Column(db.String(20, 'utf8_bin'))
    positionAdvantage = db.Column(db.String(200, 'utf8_bin'))
    positionName = db.Column(db.String(100, 'utf8_bin'))
    positionID = db.Column(db.Integer, unique=True)
    positionURL = db.Column(db.String(200, 'utf8_bin'), nullable=False)
    salary = db.Column(db.String(200, 'utf8_bin'), nullable=False)
    workYear = db.Column(db.String(10, 'utf8_bin'))
    crawl_time = db.Column(db.DateTime, nullable=False)

    def getData(self):
        """
        返回dict类型的数据,删除了多个参数
        """
        data = vars(self)
        data.pop('_sa_instance_state')
        data.pop('id')
        data.pop('crawl_time')
        return data
