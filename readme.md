# Bitpanda Take Home Task


## Spec
Your task is to create two microservices that exchange data. The microservices should be
implemented in Python and should use a queue for communication. The expected output is
a complete Python application, including tests and documentation.
Requirements
1. You should implement two microservices, one to produce data and one to consume
data. The producer should be able to generate a message and send it to a queue.
The consumer should be able to receive and acknowledge the message from the
queue after processing it.
2. You should use a queue to communicate between the two microservices. You can
use any queue technology that you are familiar with.
3. You should use Python 3.9 or higher to implement the microservices.
4. You should provide comprehensive tests for your code.
5. You should provide documentation for your code, including instructions on how to set
up and run the microservices.
6. Additional marks will be given for the use of AWS services, Docker, and any Python
packaging.
Submission
You have 24 hours to complete the task. Please submit your code as a Gitlab repository or
as a compressed archive file. The repository should include a README file that explains
how to set up and run the microservices.
Evaluation
1. Your submission will be evaluated based on the following criteria:
2. Functionality: Does your code meet the requirements and work as expected?
3. Code quality: Is your code well-structured, easy to read, and well-documented?
4. Testing: Have you provided comprehensive tests for your code?
5. Documentation: Have you provided clear and comprehensive documentation for your
code?


## Run the following commands to get started.

1. Check you have pip installed
2. Install poetry
```
pip install poetry
```
or
```angular2html
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

```
3. Install dependencies
```angular2html
poetry install
```

4. Activate your virtual environment by running the command:
```angular2html
poetry shell
```