import re
from pathlib import Path
from collections import defaultdict


if __name__ == '__main__':

    # using regex named groups, we determine the pattern for the line
    # we want to match each line with a FROM: at the beginning, a space,
    # and a string with an @ sign
    pattern = r'(?P<from_prefix>from:)\s+(?P<email_address>\S+\@\S+)'

    # using the 're' regex library, we compile the pattern and ignore case
    compiled = re.compile(pattern, re.IGNORECASE)

    # we create a registry to store all found emails matching the pattern
    # the registry will be a 'defaultdict' data structure
    registry = defaultdict(int)

    # we store the path to the input file as a Path object because it
    # allows us to properly resolve it, and determine if it exists
    # when it does not exist, we exit the program
    input_file = Path(str(input('Enter file: ')).strip()).resolve() or None
    if not input_file.exists():
        print(f'File "{input_file}" does not exist.')
        exit()

    # assuming it exists, we read the content into a text 'content' variable
    with open(input_file, 'r') as scanned_file:
        content = scanned_file.read()

    # we use the compiled regex object to find all matching emails as a list
    matched = compiled.findall(content)

    # each matched email has a "From" and "email" part as a tuple
    # we iterate over each item, and increment its count
    for _from, _email in matched:
        registry[_email] += 1

    if registry:
        # use the "sorted" function to sort by count in DESC (reverse) order
        emails = sorted(registry.items(), key=lambda item: item[1], reverse=True)
        print(f'Top FROM email = "{emails[0][0]}", with {emails[0][1]} emails')
    else:
        print(f'No emails were found')
