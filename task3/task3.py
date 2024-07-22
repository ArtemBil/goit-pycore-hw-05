import sys;
import re;
from collections import Counter; 

base_filename, *params = sys.argv;

if len(params) == 0:
  print('No parameters provided. Required at least path/to/error.log file provided');
  exit(1);

error_log_file_path = params[0];
error_level = params[1] if len(params) > 1 else None
# regexp matches pattern 'yyy-mm-dd h:m:s ERRORLEVEL ERROR MESSAGE.'
regexp = re.compile(r'(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s(\w+)\s([\w+\s.?]+)');
error_levels = ('INFO', 'DEBUG', 'ERROR', 'WARNING');

def load_logs(file_path: str) -> list:
  try:
    with open(file_path, 'r') as reader:
      return reader.read().splitlines();
  except FileNotFoundError as e:
    print('File not found. Please check the path to file you provided.');
    exit(1);

def parse_log_line(line: str) -> dict:
  try:
    datetime, error_level, error_msg = re.search(regexp, line).groups();

    return {
      "datetime": datetime,
      "error_level": error_level,
      "error_msg": error_msg,
    }
  except (AttributeError) as e:
    print('Looks like the syntax is broken. Please check and correct it.');
    exit(1);
    
def filter_logs_by_level(level: str) -> list:
  def inner(log: dict):
    return log['error_level'] == level;
  
  return inner;

def count_logs_by_level(logs: list) -> dict:
  logs_counter = Counter();
  
  for error in logs:
    logs_counter[error['error_level']] += 1;

  return dict(logs_counter);

def display_log_counts(counts: dict[str, str]) -> str:
  headers = ['Рівень логування', 'Кількість'];
  print ('\n' + headers[0], '|', headers[1]);
  print('-' * len(headers[0]) + ' | ' + '-' * len(headers[1]));

  for error_lvl, count in counts.items():
    print(error_lvl.ljust(len(headers[0])), '|', count);

  if error_level is not None and error_level.upper() in error_levels:
    filtered_errors_by_level = list(filter(filter_logs_by_level(error_level.upper()), parsed_error_logs));
    
    print(f'\nДеталі логів для рівня {error_level.upper()}:');
    for error_info in filtered_errors_by_level:
      print(f'{error_info['datetime']} - {error_info['error_msg']}');


# Load the errors array
errors = load_logs(error_log_file_path);
# Parse errors
parsed_error_logs = list(map(parse_log_line, errors));
# # Create an error leveles dictionary
counted_logs_by_level = count_logs_by_level(parsed_error_logs);
# # Render the parsing reuslt
display_log_counts(counted_logs_by_level);