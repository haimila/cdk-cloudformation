from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_sqs as sqs,
)


class MainStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(
            self, "s3bucket",
            bucket_name="mitjan-cdk-boksi"
        )

        jono = sqs.Queue(
            self, "sqsqueue",
            queue_name="Mitjan-jono"
        )






