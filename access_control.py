import time

access_control = {}
roles = {"user1": ["keyword1", "keyword2"], "user2": ["keyword2"]}  # Replace with a database

def grant_access(user, keyword, duration=60):
    if keyword in roles.get(user, []):
        access_control[(user, keyword)] = time.time() + duration
        return True
    return False

def check_access(user, keyword):
    return (user, keyword) in access_control and time.time() < access_control[(user, keyword)]
