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
class SubClass(object):
    """This is a subclass."""
    z = attr.ib()
    y = attr.ib()


@attr.s
class Empty(object):
    """Empty class for test.

    Arguments:
       x: point x

    """
    x = attr.ib()
    rz = attr.ib(SubClass, type=SubClass)


if __name__ == '__main__':
    sc = SubClass(z=5, y=4)
    e = Empty(x=3, rz=sc)
    print attr.asdict(e)
    print cattr.structure(attr.asdict(e), Empty)