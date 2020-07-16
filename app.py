#!/usr/bin/env python3

from aws_cdk import core

from cdk8.cdk8_stack import Cdk8Stack


app = core.App()
Cdk8Stack(app, "cdk8", env={'region': 'ap-northeast-1'})

app.synth()
