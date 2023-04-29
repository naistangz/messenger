import boto3
import utils


class MessageConsumer:
    def __init__(
        self,
        sqs: boto3.resource("s3"),
        queue_url: str,
        max_number_of_messages: utils.MAX_NUM_MESSAGES,
        wait_time_seconds: int = utils.MAX_WAIT_TIME_SECONDS,
    ):
        self.sqs = sqs
        self.queue = self.sqs.Queue(queue_url)
        self.max_number_of_messages = max_number_of_messages
        self.wait_time_seconds = wait_time_seconds

    def process_message(self, message):
        # process the message
        print(f"Processing message: {message.body}")

    def consume_messages(self):
        while True:
            messages = self.queue.receive_messages(
                WaitTimeSeconds=self.wait_time_seconds,
                MaxNumberOfMessages=self.max_number_of_messages,
            )
            for message in messages:
                self.process_message(message)
                message.delete()

