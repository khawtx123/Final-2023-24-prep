import re

# Example string for demonstration
example_string = "He@llo, 123 world! This is a sample string with some numbers: 42, 987."

# re.search()
match_search = re.search(r'H', example_string)
print("re.search:")
if match_search:
    print(f"Match found: {match_search.group()}")
else:
    print("No match found.")

# re.match()
match_start = re.match(r'\w+', example_string)
print("\nre.match:")
if match_start:
    print(f"Match found at the beginning: {match_start.group()}")
else:
    print("No match found at the beginning.")

# re.findall()
matches_findall = re.findall(r'\d+', example_string)
print("\nre.findall:")
print(f"All matches: {matches_findall}")

# re.sub()
modified_string = re.sub(r'\d+', 'X', example_string)
print("\nre.sub:")
print(f"Modified string: {modified_string}")

# re.compile()
pattern = re.compile(r'@')
match_compiled = pattern.search(example_string)
print("\nre.compile:")
if match_compiled:
    print(f"Match found using compiled pattern: {match_compiled.group()}")
else:
    print("No match found.")

# re.split()
split_result = re.split(r'\W+', example_string)
print("\nre.split:")
print(f"Split result: {split_result}")
