from aws_cdk import core as cdk

import constants
from deployment import LandingPageFrontend


def create_app() -> cdk.App:
    app = cdk.App()
    # Development stack
    LandingPageFrontend(app, f"{constants.CDK_APP_NAME}-Dev", env=constants.DEV_ENV)
    return app
