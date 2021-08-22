import os

from aws_cdk import core as cdk

CDK_APP_NAME = "LandingPageFrontend"

DEV_ENV = cdk.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"], region=os.environ["CDK_DEFAULT_REGION"]
)
