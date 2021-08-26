from aws_cdk import aws_s3 as s3
from aws_cdk import core as cdk

import cdk_props
from company_cdk_security import aws_s3 as security_s3


class Website(cdk.Construct):
    def __init__(self, scope: cdk.Construct, id_: str):
        super().__init__(scope, id_)

        bucket_props = cdk_props.merge(
            props=[
                security_s3.BucketPropsCollection.public_access(),
                security_s3.BucketPropsCollection.fedramp_moderate(),
            ],
            overrides=s3.BucketProps(versioned=True, public_read_access=True),
        )
        bucket_props_dict = cdk_props.to_dict(bucket_props)
        s3.Bucket(self, "Bucket", **bucket_props_dict)
