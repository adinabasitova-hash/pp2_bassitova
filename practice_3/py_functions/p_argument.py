def describePet(name, animal, age):
  """Prints a short pet description using positinal arguments(order matters here)"""
  print(f"My {animal} {name} is {age}years old")

  describePet('Dixie', 'cat', 3)

#Here is a function with default argument
def make_coffee(size="medium", sugar=True):
    """Makes a coffee with a given size and sugar preference, both optional."""
    print(f"Making a {size} coffee, sugar: {sugar}")

make_coffee()
make_coffee(size="large", sugar=False)