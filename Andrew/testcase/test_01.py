# -*- coding:utf-8 -*-

import pytest


class Test01():

    @pytest.mark.run(order=1)
    def test_01_login(self):
        print("第一条用例")

    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    def test_03_login(self):
        print("第三条用例")

    @pytest.mark.run(order=2)
    @pytest.mark.username
    def test_04_login(self):
        print("第四条用例")