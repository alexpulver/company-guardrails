from aws_cdk import aws_s3 as s3


class BucketPropsCollection:
    @staticmethod
    def public_access() -> s3.BucketProps:
        return s3.BucketProps(enforce_ssl=True, public_read_access=True)

    @staticmethod
    def fedramp_moderate() -> s3.BucketProps:
        return s3.BucketProps(enforce_ssl=True, public_read_access=False)

    @staticmethod
    def nist80053(server_access_logs_bucket: s3.IBucket) -> s3.BucketProps:
        return s3.BucketProps(server_access_logs_bucket=server_access_logs_bucket)
