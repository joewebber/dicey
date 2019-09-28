# Get the list of users
def get_user_list():
  return ['joe', 'charlie']

# Check that the user is in the approved list
def is_user_auth(user):
  return user in get_user_list()

# Set the name of the specified player
def set_player_name(player_number):
  text = 'Enter name of player ' + str(player_number) + ':'
  player_name = input(text)

  if (is_user_auth(player_name)):
    return player_name
  else:
    print('Player is not authorised')
    set_player_name(player_number)

# Set all player names
def set_player_names():
  player_names = []
  player = 1
  while player <= 2:
    player_name = set_player_name(player)
    if (player_name):
      player_names.append(player_name)
      player += 1
  return player_names