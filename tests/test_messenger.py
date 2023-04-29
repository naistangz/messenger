from messenger import Messenger
from consumer import MessageConsumer
from conftest import test_kwargs


def test_send_message(mock_sqs_resource):
    messenger = Messenger(**test_kwargs)
    message_body = {"test_key": "test_value"}
    message_id = messenger.send_message(message_body)
    assert isinstance(message_id, str)


def test_receive_messages(mock_sqs_resource):
    messenger = Messenger(**test_kwargs)
    message_body = {"test_key": "test_value"}
    messenger.send_message(message_body)
    consumer = MessageConsumer(mock_sqs_resource, "test_url", 0, 0)
    received_messages = consumer.consume_messages()
    assert len(received_messages) > 0


def test_receive_messages_with_wait_time_seconds(mock_sqs_resource):
    messenger = Messenger(**test_kwargs)
    message_body = {"test_key": "test_value"}
    messenger.send_message(message_body)
    consumer = MessageConsumer(mock_sqs_resource, "test-url", 1, 1)

    received_messages = consumer.consume_messages()
    assert len(received_messages) > 0


def test_receive_messages_with_max_number_of_messages(mock_sqs_resource):
    messenger = Messenger(**test_kwargs)
    message_body = {"test_key": "test_value"}
    messenger.send_message(message_body)

    consumer = MessageConsumer(mock_sqs_resource, "test-url", 1, 1)
    max_number_of_messages = 1
    received_messages = consumer.consume_messages()
    assert len(received_messages) == max_number_of_messages
