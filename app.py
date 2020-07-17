#!/usr/bin/env python3
import os
from aws_cdk import core

from cdk8.cdk8_stack import Cdk8Stack
from mainstack.mainstack import AppStack
my_env = os.environ["AWS_ACCOUNTID"]

app = core.App()
main_stack = core.Stack(app, 'main', env={'region': 'ap-northeast-1', 'account': my_env})

vpcstackki = Cdk8Stack(main_stack, "vpcstack")

ec2_app = AppStack(
    main_stack,
    'App',
    vpc=vpcstackki.vpc
)


app.synth()
