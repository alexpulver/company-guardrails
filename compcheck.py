from aws_cdk import core as cdk
from cdk_nag import NIST80053Checks

from helpers import create_app

app = create_app()
cdk.Aspects.of(app).add(NIST80053Checks())
app.synth()
