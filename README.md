# Company guardrails
The project shows an approach to company guardrails for AWS CDK applications.
It implements a *landing page frontend* component that uses Amazon S3 for hosting.

## Create development environment
See [Getting Started With the AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)
for additional details and prerequisites

### Clone the code
```bash
git clone https://github.com/alexpulver/company-guardrails
cd company-guardrails
```

### Create Python virtual environment and install the dependencies
```bash
python3.7 -m venv .venv
source .venv/bin/activate
# [Optional] Needed to upgrade dependencies and cleanup unused packages
pip install pip-tools==6.2.0
./scripts/install-deps.sh
./scripts/run-tests.sh
```

### [Optional] Upgrade AWS CDK Toolkit version
```bash
vi package.json  # Update "aws-cdk" package version
./scripts/install-deps.sh
./scripts/run-tests.sh
```

### [Optional] Upgrade dependencies (ordered by constraints)
Consider [AWS CDK Toolkit (CLI)](https://docs.aws.amazon.com/cdk/latest/guide/reference.html#versioning) compatibility 
when upgrading AWS CDK packages version.

```bash
pip-compile --upgrade requirements.in
pip-compile --upgrade requirements-dev.in
./scripts/install-deps.sh
# [Optional] Cleanup unused packages
pip-sync requirements.txt requirements-dev.txt
./scripts/run-tests.sh
```

## Run compliance checks
The checks are performed using [cdk-nag](https://github.com/cdklabs/cdk-nag) library
```bash
npx cdk synth -a "python compcheck.py"
```

If `cdk-nag` finds issues, you can use company's policy library to remediate, 
or suppress the rule if needed. Follow the instructions in `cdk-nag` webpage 
for how to suppress a rule.

See [website infrastructure](website/infrastructure.py) construct for an example
of applying NIST 800-53 rules to the website bucket, while suppressing the rule
for the logs bucket used to make the website bucket compliant.

## Deploy the component to development environment
The `LandingPageFrontend-Dev` stack uses your default AWS account and region.

```bash
npx cdk deploy LandingPageFrontend-Dev
```

## Delete the component
**Do not forget to delete the component to avoid unexpected charges**

```bash
npx cdk destroy LandingPageFrontend-Dev
```
