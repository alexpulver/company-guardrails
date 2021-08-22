from aws_cdk import core as cdk

import constants
from deployment import LandingPageFrontend

app = cdk.App()

# Development stack
LandingPageFrontend(app, f"{constants.CDK_APP_NAME}-Dev", env=constants.DEV_ENV)

app.synth()
