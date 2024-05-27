from faker import Faker
import random
import time
fake = Faker()

def generate_accuracy():
    return round(random.uniform(0.75, 0.81), 2)

def generate_precision():
    return round(random.uniform(0.70, 0.90), 2)

def generate_log_entry():
    timestamp = fake.date_time_this_year()
    image_id = fake.uuid4()
    accuracy = generate_accuracy()
    precision = generate_precision()
    return f"{timestamp} - Image ID: {image_id} - Accuracy: {accuracy} - Precision: {precision}"


num_entries = 10

# Print start message
print("Started at http://tb.test.woza.work/")

# Generate and print log entries
for _ in range(num_entries):
    log_entry = generate_log_entry()
    print(log_entry)
    # Simulate a delay between log entries
    time.sleep(1)
