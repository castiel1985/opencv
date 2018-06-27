# coding: utf-8
from app.dept import dept

from flask import jsonify
import json

dept_data = [
    {
        'name':'IT',
        'id':'001'
    },
    {
        'name':'caiwu',
        'id':'002'
    }
]


@dept.route('/<int:id>', methods=['GET', ])
def get(id):
    for dept in dept_data:
        if int(dept['id']) == id:
            return jsonify(status='success',dept=dept)
    return jsonify(status='failed',msg='data not found')

@dept.route('/depts', methods = ['GET', ])
def get_depts():
    data = {
        'status':'success',
        'depts':dept_data
    }
    return json.dump(data,ensure_ascii=False,indent=1)