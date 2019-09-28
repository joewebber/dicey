# Get the list of users
def get_user_list():
  return ['joe']

# Check that the user is in the approved list
def is_user_auth(user):
  return user in get_user_list()