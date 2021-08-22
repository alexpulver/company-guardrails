from typing import Any

from aws_cdk import core as cdk

from website.infrastructure import Website


class LandingPageFrontend(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id_: str, **kwargs: Any):
        super().__init__(scope, id_, **kwargs)

        Website(self, "Website")
