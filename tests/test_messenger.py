import unittest

from messenger import Messenger
from consumer import MessageConsumer
from conftest import test_kwargs


class TestMessenger(unittest.TestCase):
    def test_send_message(self, mock_sqs_resource):
        messenger = Messenger(**test_kwargs)
        message_body = {"test_key": "test_value"}
        message_id = messenger.send_message(message_body)
        self.assertIsInstance(message_id, str)

    def test_send_message_attributes(self, mock_sqs_resource):
        messenger = Messenger(**test_kwargs)
        message_body = {"test_key": "test_value"}

        message_id = messenger.send_message(message_body)
        self.assertIsInstance(message_id, str)


class TestMessageConsumer(unittest.TestCase):
    def test_receive_messages(self, mock_sqs_resource):
        messenger = Messenger(**test_kwargs)
        message_body = {"test_key": "test_value"}
        messenger.send_message(message_body)
        consumer = MessageConsumer(mock_sqs_resource,"test_url", 1, 1)
        received_messages = consumer.consume_messages()
        self.assertGreater(len(received_messages), 0)

    def test_receive_messages_with_wait_time_seconds(self, mock_sqs_resource):
        messenger = Messenger(**test_kwargs)
        message_body = {"test_key": "test_value"}
        messenger.send_message(message_body)
        consumer = MessageConsumer(mock_sqs_resource,"test-url", 1, 1)

        received_messages = consumer.consume_messages()
        self.assertGreater(len(received_messages), 0)

    def test_receive_messages_with_max_number_of_messages(self, mock_sqs_resource):
        messenger = Messenger(**test_kwargs)
        message_body = {"test_key": "test_value"}
        messenger.send_message(message_body)

        consumer = MessageConsumer(mock_sqs_resource, "test-url", 1, 1)
        max_number_of_messages = 1
        received_messages = consumer.consume_messages()
        self.assertEqual(len(received_messages), max_number_of_messages)
