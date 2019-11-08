#!/usr/bin/env python
# Created by Enrique Plata

from ast import literal_eval
from google.cloud import storage
from google.cloud import pubsub_v1

def getRegistry():
    '''
    This returns a dictionary containing the credentials for GCP
    '''
    listOfRegistries = {'SUBSCRIPTION': 'Appusma206_apps_Listener', 'PROJECT_ID':'microstrategyit', 'TOPIC':'projects/microstrategyit/topics/Appusma206_apps'}
    return listOfRegistries

def synchronous_pull(project_id, subscription_name):
    """Pulling messages synchronously."""
    # [START pubsub_subscriber_sync_pull]

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(
        project_id, subscription_name)

    NUM_MESSAGES = 1

    # The subscriber pulls a specific number of messages.
    response = subscriber.pull(subscription_path, max_messages=NUM_MESSAGES)

    ack_ids = []
    for received_message in response.received_messages:
        # print("Received: {}".format(received_message.message.data))
        ack_ids.append(received_message.ack_id)

    # Acknowledges the received messages so they will not be sent again.
    subscriber.acknowledge(subscription_path, ack_ids)
    # print('Received and acknowledged {} messages. Done.'.format(
    #     len(response.received_messages)))

    return received_message.message.data
    
    # [END pubsub_subscriber_sync_pull]

def binary_to_dict(the_binary):
    dictionary = literal_eval(str(the_binary, 'utf-8'))
    return dictionary

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)
    



    