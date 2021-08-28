import os

from aws_cdk import core as cdk
from cdk_nag import NIST80053Checks

from deployment import LandingPageFrontend

app = cdk.App()

LandingPageFrontend(
    app,
    "LandingPageFrontend",
    env=cdk.Environment(
        account=os.environ["CDK_DEFAULT_ACCOUNT"],
        region=os.environ["CDK_DEFAULT_REGION"],
    ),
)

cdk.Aspects.of(app).add(NIST80053Checks())

app.synth()
