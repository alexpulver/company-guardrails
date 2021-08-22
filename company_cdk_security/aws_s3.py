from aws_cdk import aws_s3 as s3
from aws_cdk import core as cdk


# pylint: disable=too-few-public-methods
class BucketPropsCollection:
    public_access = s3.BucketProps(enforce_ssl=True, public_read_access=True)

    __expiration_lifecycle_rule = s3.LifecycleRule(expiration=cdk.Duration.days(30))
    retention_policy = s3.BucketProps(lifecycle_rules=[__expiration_lifecycle_rule])
