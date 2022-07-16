import json
from django.core import serializers


def from_model_to_json_str(any_object):
    """モデルをJSON文字列に変換する"""
    return serializers.serialize('json', any_object)


def from_model_to_json_str_with_indent(any_object):
    """モデルをインデント付きでJSON文字列に変換する"""
    json_str = from_model_to_json_str(any_object)
    doc = json.loads(json_str)
    return json.dumps(doc, indent=4)
