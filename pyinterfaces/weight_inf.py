# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#
###############################################################################
"""
This module define the weight sensor interfaces.

Authors: wangxiao05(wangxiao05@baidu.com)
Date:    2018/07/29 22:46:43
"""

import attr
import cattr


@attr.s
class WeightSensorTriggerEvent(object):
    """Event output of weight sensor."""

    weight_event_id = attr.ib(type=str)
    start_time = attr.ib(type=int)
    end_time = attr.ib(type=int)
    gid = attr.ib(type=str)
    cells = attr.ib(type=str)


@attr.s
class WeightSensorProductRecognizer(object):
    """Regonize product by event."""

    weight_diff = attr.ib(type=float,
                          metadata=dict(doc='Weight diff generate from cells.'))
    gpropose = attr.ib(factory=list,
                       metadata=dict(doc='sku propose by only weight sensor.'))
    exc_num = attr.ib(default=0, type=int,
                      metadata=dict(doc='Exception type. 0 means normal. 1: unable to predict'))
    exc_info = attr.ib(default='', type=str,
                       metadata=dict(doc='Extra info goes with exc_num.'))


if __name__ == '__main__':
    wte = WeightSensorTriggerEvent('111', 123, 245, 'weight_sensor_id', '10 10 10 11 12 15')
    wpr = WeightSensorProductRecognizer(15, [111, 234, 456], 0, 'Normal')
    print cattr.unstructure(wte)
    s = cattr.unstructure(wpr)
    print s
    print cattr.structure(s, WeightSensorProductRecognizer)