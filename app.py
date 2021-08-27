from aws_cdk import core as cdk
from cdk_nag import NIST80053Checks

import constants
from deployment import LandingPageFrontend

app = cdk.App()

# Development stack
LandingPageFrontend(app, f"{constants.CDK_APP_NAME}-Dev", env=constants.DEV_ENV)

cdk.Aspects.of(app).add(NIST80053Checks())

app.synth()
