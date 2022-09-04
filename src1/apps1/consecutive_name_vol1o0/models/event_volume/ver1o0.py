# BOF [OAAA1001o2o1o0g3o1o0]

# See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92
from django.db import models


class EventVolume(models.Model):
    """[OAAA1001o2o1o0g3o1o0] 催事巻"""

    # プロパティの仕様を決める感じで
    id = models.AutoField('Id', primary_key=True)
    event_id = models.IntegerField('催事種別Id', blank=True, default=0)
    name = models.CharField('名称', max_length=64, blank=True, null=True)
    name_s = models.CharField('名称_短縮', max_length=16, blank=True, null=True)
    sort = models.IntegerField('順番', blank=True, default=0)

    def __str__(self):
        """このオブジェクトを文字列にしたとき返るもの"""
        return f"{self.display_name} event-volume"

# EOF [OAAA1001o2o1o0g3o1o0]
