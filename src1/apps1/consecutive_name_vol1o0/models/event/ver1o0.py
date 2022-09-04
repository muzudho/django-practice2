# BOF [OAAA1001o2o1o0g3o0]

# See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92
from django.db import models


class Event(models.Model):
    """[OAAA1001o2o1o0g3o0] 催事種別"""

    # プロパティの仕様を決める感じで
    id = models.AutoField('Id', primary_key=True)
    name = models.CharField('名称', max_length=32, blank=True, null=True)
    name_s = models.CharField('名称_短縮', max_length=16, blank=True, null=True)
    sort = models.IntegerField('順番', blank=True, default=0)

    def __str__(self):
        """このオブジェクトを文字列にしたとき返るもの"""
        return f"{self.display_name} event"

# EOF [OAAA1001o2o1o0g3o0]
