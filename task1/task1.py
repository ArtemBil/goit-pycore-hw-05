def caching_fibonacci():
  cache: dict = {};

  def fibonacci(n: int):
    if n <= 0: 
      return 0;
    
    if n == 1: 
      return 1;

    if cache.get(n):
      return cache.get(n);

    cache[n] = fibonacci(n - 1) + fibonacci(n - 2);
    
    return cache.get(n);
  return fibonacci;

calculate_fibonacci = caching_fibonacci();

print(calculate_fibonacci(10));
print(calculate_fibonacci(15));

