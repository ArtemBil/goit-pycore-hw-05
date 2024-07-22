def input_error(func):
  def inner(*args, **kwargs):
    try:
      return func(*args, **kwargs);
    except ValueError:
      contact_info_args_len = len(args[0]);

      if contact_info_args_len == 1:
        return 'Missing phone. Please provide phone number';

      if contact_info_args_len == 0:
        return 'Missing name and phone. Please provide name and phone info.'
    except KeyError:
      name = args[0][0];

      return f'The contact with name {name} does not exists.'
  return inner;

def parse_input(user_input: str):
  cmd, *args = user_input.split();
  cmd = cmd.strip().lower();

  return cmd, *args;

@input_error
def add_contact(args: list, contacts: dict):
  name, phone = args;

  if contacts.get(name):
    is_override_approved = input('The contact with such name already exists. Would you like to override (yes, no)? ');
    command, *args = parse_input(is_override_approved);

    if command == 'yes':
      contacts[name] = phone;
      return 'Contatct has successfully been updated.';
  else:
    contacts[name] = phone;
    return 'Contatct has successfully been added.';

  return f'The contact has not been added as such user with phone {phone} already exists.';

@input_error
def update_contact(args, contacts):
    name, phone = args

    if contacts.get(name):
      contacts[name] = phone;
    else:
      return f'Failed to update. Contact with name {name} does not exist.'

    return "Contact has been updated.";

@input_error
def show_contact(args, contacts):
  name, *args = args;
  
  return contacts[name];

def show_all(contacts):
  for key, value in contacts.items():
    print('Contact Name: ', key, '\n');
    print('Contact Phone: ', value);
    print('--------------');

def main():
  contacts = {};
  print('Welcome to the assistant bot!');

  while True:
    user_input = input('Enter a command: ').strip().lower();
    command, *args = parse_input(user_input);

    if command in ['close', 'exit']:
      print('Good bye!');
      break;
    elif command == 'hello':
      print('How can I help you?');
    elif command == 'add':
      print(add_contact(args, contacts));
    elif command == 'change':
      print(update_contact(args, contacts));
    elif command == 'phone':
      print(show_contact(args, contacts));
    elif command == 'all':
      show_all(contacts);
    else:
      print('Invalid command');


if __name__ == '__main__':
  main();