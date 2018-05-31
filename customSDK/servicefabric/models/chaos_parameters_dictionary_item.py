# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChaosParametersDictionaryItem(Model):
    """Defines an item in ChaosParametersDictionary of the Chaos Schedule.
    .

    :param key: The key identifying the Chaos Parameter in the dictionary.
     This key is referenced by Chaos Schedule Jobs.
    :type key: str
    :param value: Defines all the parameters to configure a Chaos run.
    :type value: ~azure.servicefabric.models.ChaosParameters
    """

    _validation = {
        'key': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'key': {'key': 'Key', 'type': 'str'},
        'value': {'key': 'Value', 'type': 'ChaosParameters'},
    }

    def __init__(self, key, value):
        super(ChaosParametersDictionaryItem, self).__init__()
        self.key = key
        self.value = value