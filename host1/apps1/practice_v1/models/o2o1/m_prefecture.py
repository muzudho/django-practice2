# See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92
from django.db import models


class Prefecture(models.Model):
    """都道府県"""

    # プロパティの仕様を決める感じで
    seq = models.AutoField('連番', primary_key=True)
    name = models.CharField('名前', max_length=4)
    # email = models.CharField('E-Mail', max_length=255)
    # age = models.IntegerField('年齢', blank=True, default=0)
    # stateInPark = models.IntegerField('状態1', blank=False, default=0)

    def __str__(self):
        """このオブジェクトを文字列にしたとき返るもの"""
        return f"{self.name} prefecture"
