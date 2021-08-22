from aws_cdk import aws_s3 as s3
from aws_cdk import core as cdk

import cdk_props

# import company_cdk_solutions
from company_cdk_security import aws_s3 as security_s3

# from company_cdk_operations import aws_s3 as operations_s3
# from company_cdk8s_security import deployment as security_deployment


class Website(cdk.Construct):
    def __init__(self, scope: cdk.Construct, id_: str):
        super().__init__(scope, id_)

        bucket_props = security_s3.BucketPropsCollection.public_access
        bucket_props = cdk_props.update(
            bucket_props, security_s3.BucketPropsCollection.retention_policy
        )
        bucket_props = cdk_props.update(
            bucket_props, s3.BucketProps(versioned=True, enforce_ssl=False)
        )
        bucket_props_dict = cdk_props.to_dict(bucket_props)
        s3.Bucket(self, "Bucket", **bucket_props_dict)

        # bucket_props = security_s3.BucketPropsCollection.public_access
        # bucket_props.update(security_s3.BucketPropsCollection.retention_policy)
        # bucket_props.update(s3.BucketProps(versioned=True, enforce_ssl=False))
        # s3.Bucket.from_props(stack, "Bucket", bucket_props)
