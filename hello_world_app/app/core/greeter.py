from app.common.user_vars import email


def greet_user(username, ip):
    location = input(f"Hi {username}, Where do you live? ")
    my_global_var = "some global stuff"
    print(f"Hi! How is {location}?", email, my_global_var, ip)
    print(f"say_hi: __name__: {__name__}, __package__: {__package__}")
