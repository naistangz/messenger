AWS_DEFAULT_REGION = "us-west-2"

QUEUE_NAME = "bitpanda-queue"
QUEUE_URL = f"https://sqs.us-west-2.amazonaws.com/123456789012/{QUEUE_NAME}"
MAX_WAIT_TIME_SECONDS = 20
MAX_NUM_MESSAGES = 5