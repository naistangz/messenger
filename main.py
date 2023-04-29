from messenger import Messenger
from consumer import MessageConsumer
import utils
import boto3


def execute(message_body, queue_name, queue_url, sqs):
    messenger = Messenger(queue_name=queue_name,sqs_resource=sqs)
    messenger.send_message(message_body)

    # Create a MessageConsumer instance and start listening for messages
    consumer = MessageConsumer(sqs, queue_url, utils.MAX_NUM_MESSAGES, utils.MAX_WAIT_TIME_SECONDS)
    consumer.consume_messages()


if __name__ == "__main__":
    sqs = boto3.resource("sqs", region_name=utils.AWS_DEFAULT_REGION)
    message = input("Input your message here:\n")
    execute({"body": message}, utils.QUEUE_NAME, utils.QUEUE_URL, sqs)
