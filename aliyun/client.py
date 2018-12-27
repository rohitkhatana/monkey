# -*- coding: utf8 -*-
from aliyunsdkcore.client import AcsClient
from credentials import ACCESS_ID, ACCESS_SECRET, REGION
# Create an AcsClient instance
client = AcsClient(ACCESS_ID, ACCESS_SECRET, REGION)
