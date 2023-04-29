import boto3
import pytest

from moto import mock_sqs
import utils
import os


@pytest.fixture(scope="function")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"


@pytest.fixture
def mock_sqs_resource():
    with mock_sqs():
        sqs = boto3.resource("sqs", region_name=utils.AWS_DEFAULT_REGION)
        sqs.create_queue(QueueName="test-queue")
        yield sqs


test_kwargs = {"sqs_resource": mock_sqs_resource, "queue_name": "test-queue"}
