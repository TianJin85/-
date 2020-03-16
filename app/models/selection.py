# -*- encoding: utf-8 -*-
"""
@File    : selection.py
@Time    :  2020/3/10 15:40
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from app.models.love import Love_selection


class Selection(Love_selection):

    @classmethod
    def add_selection(cls, mid, marriage, age, stature, weight, monthly, housing, vehicle, children, census, pests):
        mess = Love_selection.query.filter_by(mid=mid).first()
        if mess is None:
            Love_selection.create(
                mid=mid,
                marriage=marriage,
                age=age,
                stature=stature,
                weight=weight,
                monthly=monthly,
                housing=housing,
                vehicle=vehicle,
                children=children,
                census=census,
                pests=pests,
                commit=True
            )

        return True