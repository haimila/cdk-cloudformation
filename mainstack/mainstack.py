from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_sqs as sqs,
    aws_elasticloadbalancingv2 as elb,
    aws_autoscaling as asg,
    aws_cloudformation as cfn,
)


class AppStack(cfn.NestedStack):

    def __init__(self, scope: core.Construct, id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(
            self, "s3bucket",
        )

        jono = sqs.Queue(
            self, "sqsqueue",
            queue_name="Mitjan-jono"
        )

        image = ec2.MachineImage.latest_amazon_linux()

        skripti = open("C:\\Users\\Mitja\\PycharmProjects\\cdk8\\mainstack\\nginx-script.sh", "rb").read()
        nginx = ec2.UserData.for_linux()
        nginx.add_commands(str(skripti, "utf-8"))

        autoscaling = asg.AutoScalingGroup(
            self, "ASG",
            vpc=vpc,
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=image,
            user_data=nginx,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType('PUBLIC')),
            min_capacity=3,
            max_capacity=6,
        )

        loadbalancer = elb.ApplicationLoadBalancer(
            self, "ELB",
            vpc=vpc,
            load_balancer_name="mitja-cdk-elb",
            internet_facing=True,
        )

        listener = loadbalancer.add_listener("Listener", port=80)
        listener.add_targets("Target", port=80, targets=[autoscaling])
        listener.connections.allow_default_port_from_any_ipv4("Open to the world")



