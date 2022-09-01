from typing import Dict, List, Tuple, Optional


def is_host_in_domain(host: str, domain: str) -> bool:
    """
    checks the given host is associated to the given domain

    :param host: the current host given from the user
    :param domain: the domain to check the host against

    :return: True if domain is included in host, else False
    """

    return domain in host


def is_host_not_simplex(host: str) -> bool:
    return not is_host_in_domain(host, "simplex")


def parse_email(email: str) -> Tuple:
    """
    :param email: the user email
    :return: the username and host, extracted from the email
    """

    user_name, host = email.split('@', 1)
    print(f"finsihed processing {user_name} from {email}")
    return user_name, host


generated_machine_ids = [f'machine-{m_id * m_id}' for m_id in range(50)]

# input data
user_emails = ['tamier@gmail.com', 'anna@gmail.com', 'shay@gmail.com', 'tal@simplex.com', 'ariel@simplex.com',
               'shay@simplex.com']

# some empty container for modified/mapped entries
# user_names: List[str] = []
# for user_email in user_emails:
#     user, host = parse_email(user_email)
#     if is_host_not_simplex(host):
#         user_names.append(user)

user_infos = [parse_email(user_email) for user_email in user_emails]
filtered = [user for user, email in user_infos if is_host_not_simplex(email)]

print(filtered)


for i in range(10):
    print(i)

print(i)











################

def calc_square(x: int) -> int:
    return x ** 2


user_names = [extract_username(user_email) for user_email in user_emails]

print(user_names)

user_emails_bckup = [print("as") for user_email in user_emails]
user_emails2 = user_emails
is_the_same = user_emails is user_emails_bckup  # False
is_eq = user_emails == user_emails_bckup  # True

my_dict = {
    'key': [],
    'other_key': []
}


def foo(some_dict: Dict[str, List[str]]):
    value_a: List[str] = some_dict.get('key')
    value_b: List[str] = some_dict.get('other_key')

    some_dict['foo'] = 'bar'
    if some_dict.get('key') is some_dict.get('other_key'):
        print("error occured -- same user detected")
        return False
