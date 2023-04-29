import boto3
import pytest

from moto import mock_sqs
import utils


@pytest.fixture
def mock_sqs_resource():
    with mock_sqs():
        sqs = boto3.resource("sqs", region_name=utils.AWS_DEFAULT_REGION)
        sqs.create_queue(QueueName=utils.QUEUE_NAME)
        yield sqs


test_kwargs = {
    "sqs_resource": mock_sqs_resource,
    "queue_name": "test_queue"
}
