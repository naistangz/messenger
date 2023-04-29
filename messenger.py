import json
import utils


class Messenger:
    def __init__(self, sqs_resource, queue_name, region_name):
        self.queue_name = queue_name
        self.region_name = region_name
        self.sqs = sqs_resource
        self.queue = self.sqs.get_queue_by_name(QueueName=self.queue_name)

    def send_message(self, message_body):
        return self.queue.send_message(MessageBody=message_body)

    def receive_message(self):
        messages = self.queue.receive_messages(
            MaxNumberOfMessages=1, WaitTimeSeconds=5
        )

        if not messages:
            return None

        message = messages[0]
        message_body = json.loads(message.body)
        receipt_handle = message.receipt_handle

        return message_body, receipt_handle

    def delete_message(self, receipt_handle):
        self.queue.delete_messages(Entries=[{"Id": "1", "ReceiptHandle": receipt_handle}])
