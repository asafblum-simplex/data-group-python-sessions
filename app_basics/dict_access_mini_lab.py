# todo are there any bugs in this code?

def handle(i):
    return i*i

[handle(i) for i in range(100)]


# module: validators.py

WORKING_VER = ('2.0.1',)


def validate_client_version(payload: dict) -> bool:
    ver = payload.get('client_version') if isinstance(payload, dict) else ''
    return bool(payload) and ver in WORKING_VER


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


consumer_alerts_validation_pipeline = [validate, [validate_ip, validate_client_version]]


for handle in :
    handle(dat)
