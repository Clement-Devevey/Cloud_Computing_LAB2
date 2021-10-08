import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Create the queue. This returns an SQS.Queue instance
#queue = sqs.create_queue(QueueName='requestQueue')
inputt = input("Entrez au maximum 10 valeurs separees par des espaces")

queue = sqs.get_queue_by_name(QueueName='requestQueue')

queue.send_message(MessageBody='boto3', MessageAttributes={
    'Clement': {
        'StringValue': inputt,
        'DataType': 'String'
    }
})
