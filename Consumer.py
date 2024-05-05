from confluent_kafka import Consumer, KafkaError

def consume_inventory_data():
    # Kafka consumer configuration
    kafka_config = {'bootstrap.servers': 'localhost:9092', 'group.id': 'inventory_group'}

    # Create Kafka consumer
    consumer = Consumer(kafka_config)
    consumer.subscribe(['inventory_orders'])

    # Consume messages
    while True:
        msg = consumer.poll(timeout=1.0)  # Poll for messages
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition
                continue
            else:
                print(f"Consumer error: {msg.error()}")
                break
        # Process inventory message
        inventory_data = json.loads(msg.value().decode('utf-8'))
        print("Received inventory data:", inventory_data)
        # Perform actions like updating inventory databases

def consume_delivery_data():
    # Kafka consumer configuration
    kafka_config = {'bootstrap.servers': 'localhost:9092', 'group.id': 'delivery_group'}

    # Create Kafka consumer
    consumer = Consumer(kafka_config)
    consumer.subscribe(['delivery_orders'])

    # Consume messages
    while True:
        msg = consumer.poll(timeout=1.0)  # Poll for messages
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition
                continue
            else:
                print(f"Consumer error: {msg.error()}")
                break
        # Process delivery message
        delivery_data = json.loads(msg.value().decode('utf-8'))
        print("Received delivery data:", delivery_data)
        # Perform actions like scheduling deliveries, updating status, etc.

# Consume inventory and delivery data
consume_inventory_data()
consume_delivery_data()
