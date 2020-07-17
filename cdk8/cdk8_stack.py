from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_cloudformation as cfn,
)


class Cdk8Stack(cfn.NestedStack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.vpc = ec2.Vpc(
            self, "MitjaVPC",
            max_azs=3,
            cidr="10.0.0.0/16",
            nat_gateways=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Pubnet",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                ),
                ec2.SubnetConfiguration(
                    name="Privanet",
                    subnet_type=ec2.SubnetType.PRIVATE,
                    cidr_mask=24,
                    )
                ]
            )

