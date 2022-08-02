from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """O9o2o0g2o0 Userモデル拡張"""

    # この User オブジェクトの下に Profile オブジェクトをぶら下げると思ってください
    #
    # Example
    # -------
    #
    # user = User.objects.get(pk=user_id)
    # print(user.profile.match_state)
    #
    # OneToOneField - 1対1対応のリレーション。 デフォルトで Unique 属性
    #
    # * `on_delete` - 必須。 models.CASCADE なら、親テーブルのレコードが消されると、子テーブルのレコードも削除されます
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)

    # 対局のマッチング状態
    #
    # 0 を休憩中， 1 を対局申込中， 2 を対局案内中， 3 を対局中， 4 を観戦中 とする
    #
    # * `blank` - 未指定でもセーブを受け入れるなら真
    # * `default` - 初期値
    match_state = models.IntegerField(
        '対局のマッチング状態', null=True, blank=True, default=0)

    def __str__(self):
        """このオブジェクトを文字列にしたとき返るもの"""
        return f"{self.user}'s profile"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """O9o2o0g2o0 新規作成"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """O9o2o0g2o0 保存"""

    if hasattr(instance, 'profile'):
        # * ここを通らないといけない
        instance.profile.save()
    else:
        # * ここに来るようならおかしい。管理画面から Profile モデルを追加し、User に紐づけるステップをやっていないのではないか？
        print("Userオブジェクトがprofile属性を持っていなかった。ここに来るようならおかしい。管理画面から Profile モデルを追加し、User に紐づけるステップをやっていないのではないか？(^～^)")


# この行が何をやっているか分からないが、分からないからサンプルの真似をしておく（＾～＾）
# 📖 [Extending the User model with custom fields in Django](https://stackoverflow.com/questions/44109/extending-the-user-model-with-custom-fields-in-django)
post_save.connect(create_user_profile, sender=User)
