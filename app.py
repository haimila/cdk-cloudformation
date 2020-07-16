#!/usr/bin/env python3

from aws_cdk import core

from cdk8.cdk8_stack import Cdk8Stack
from mainstack.mainstack import MainStack

app = core.App()
Cdk8Stack(app, "nestvpc", env={'region': 'ap-northeast-1', 'account': '821383200340'},)
MainStack(app, "main", env={'region': 'ap-northeast-1', 'account': '821383200340'},)
app.synth()
