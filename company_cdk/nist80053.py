from aws_cdk import aws_s3 as s3


class PropsCollection:
    @staticmethod
    def aws_s3(server_access_logs_bucket: s3.IBucket) -> s3.BucketProps:
        return s3.BucketProps(server_access_logs_bucket=server_access_logs_bucket)
