# todo are there any bugs in this code?

# module: validators.py

def validate_client_version(payload: dict) -> bool:
    return payload.get('client_version') is not None and payload.get('client_version') is not '2.0.1'


def validate_ip(payload: dict) -> bool:
    # ... some validation logic
    return True


# module: main.py

data = {
    'payload': {
        'ip': '192.168.1.1',
        'app_id': 'consumer.notifications.user.logouts',
        'client_version': '2.0.1'
    },
    'status': 201,
    'status_text': 'created'
}

validate_client_version(data['payload'])
