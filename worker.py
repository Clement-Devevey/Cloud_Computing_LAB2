import boto3

# Get the service resource
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='requestQueue')

for message in queue.receive_messages(MessageAttributeNames=['Clement']):
    # Get the custom author message attribute if it was set'
    if message.message_attributes is not None:
        mes_int = message.message_attributes.get('Clement').get('StringValue')
        mes_int_split = mes_int.split()
        
    # Let the queue know that the message is processed
    message.delete()
    queue.reload()
    moyenne = 0
    for i in range (len(mes_int_split)):
        moyenne = moyenne + int(mes_int_split[i])
        
    moyenne = moyenne / len(mes_int_split)
    print("Moyenne = ", moyenne)
    
    