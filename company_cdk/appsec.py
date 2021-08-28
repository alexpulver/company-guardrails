from aws_cdk import aws_s3 as s3


class PropsCollection:
    @staticmethod
    def aws_s3_bucket_public_access() -> s3.BucketProps:
        return s3.BucketProps(enforce_ssl=True, public_read_access=True)
