from messenger import Messenger
from consumer import MessageConsumer
import utils
import boto3


def execute(message_body, queue_name, queue_url, sqs):
    messenger = Messenger(queue_name=queue_name, region_name=utils.AWS_DEFAULT_REGION, sqs_resource=sqs)
    messenger.send_message(message_body)

    # Create a MessageConsumer instance and start listening for messages
    consumer = MessageConsumer(sqs, queue_url, utils.MAX_NUM_MESSAGES, utils.MAX_WAIT_TIME_SECONDS)
    consumer.consume_messages()


if __name__ == "__main__":
    sqs = boto3.resource("sqs", region_name=utils.AWS_DEFAULT_REGION)
    execute({"body": "This is a message"}, utils.QUEUE_NAME, utils.QUEUE_URL, sqs)
