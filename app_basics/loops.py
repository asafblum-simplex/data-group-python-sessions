import datetime


def send_email(user_id):
    print(f'sending email to {user_id}')

def loop_handler(user_id):
    if user_id % 2 == 0:
        raise ExceptionA()

    if user_id > 15:
        raise StopIteration()

    print(f'processing {user_id}')
    send_email(user_id)

def for_in_loop(user_ids, handler):


    [loop_handler(user_id) for user_id in user_ids]



def while_loop(user_ids):
    output = []
    while len(output) <= 20:
        print('running...')
        output.append(datetime.datetime.now())
        # is_running = False

    print("loop is finished")
