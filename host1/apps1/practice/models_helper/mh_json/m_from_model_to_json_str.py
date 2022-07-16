from django.core import serializers


def from_model_to_json_str(model):
    """モデルをJSON文字列に変換する"""
    return serializers.serialize('json', model)
