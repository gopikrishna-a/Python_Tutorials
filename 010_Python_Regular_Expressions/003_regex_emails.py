import re

def find_email(input):
    emails = []
    pattern = re.compile(r'^([a-z0-9_\.-]+)@([a-z0-9_\.-]+)\.([a-z\.]{2,6})$')
    match = pattern.search(input)
    return match


print(find_emails('a..gopikrishna@gmail.com')) 