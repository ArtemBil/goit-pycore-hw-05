import re;
from functools import reduce;

def generator_numbers(text: str):
  convert_to_number = lambda x: float(x) if '.' in x else int(x);
  numberMatches = re.findall(r"(\d+\.?\d+|\d+)", text);
  numbers = list(map(convert_to_number, numberMatches));

  for num in numbers:
    yield num;


def sum_profit(text: str, func):
  generator = func(text);
  
  return reduce(lambda a, b: a + b, generator);


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.";
total_income = sum_profit(text, generator_numbers);
print(f"Загальний дохід: {total_income}");
