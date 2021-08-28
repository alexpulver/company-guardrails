from typing import cast

from aws_cdk import aws_s3 as s3
from aws_cdk import core as cdk

import cdk_props
from company_cdk import appsec
from company_cdk import fedramp
from company_cdk import nist80053


class Website(cdk.Construct):
    def __init__(self, scope: cdk.Construct, id_: str):
        super().__init__(scope, id_)

        logs_bucket = s3.Bucket(self, "LogsBucket")
        cfn_logs_bucket = cast(s3.CfnBucket, logs_bucket.node.default_child)
        cfn_logs_bucket.add_metadata(
            "cdk_nag",
            {
                "rules_to_suppress": [
                    {
                        "id": "NIST.800.53-S3BucketLoggingEnabled",
                        "reason": "This is the logging bucket itself",
                    },
                ],
            },
        )
        bucket_props = cdk_props.merge(
            props=[
                appsec.PropsCollection.aws_s3_bucket_public_access(),
                fedramp.PropsCollection.aws_s3_bucket(),
                nist80053.PropsCollection.aws_s3_bucket(
                    server_access_logs_bucket=logs_bucket
                ),
            ],
            overrides=s3.BucketProps(versioned=True, public_read_access=True),
        )
        bucket_props_dict = cdk_props.to_dict(bucket_props)
        s3.Bucket(self, "Bucket", **bucket_props_dict)
