"""
nav.py by Pipythonmc

A simple script that strips css comments from wiki_style.css and appends it to a copy of nav.md saved as navigation.md
"""

# A warning to the reader of this code: Please don't try to understand the comment stripping functionality, as it can cause braincell loss. Even I can't read it 10 minutes after writing it.

print('[+] Loading wiki_style.css')

style_original = open('wiki_style.css', 'r').read()
style_stripped = ""
possible_comment = False
in_comment = False
escaped = False

print('[+] Stripping comments')

for i, c in enumerate(style_original):
    if escaped:
        style_stripped += c
        escaped = False
        continue

    if c == "\\":
        style_stripped += c
        escaped = True
        continue

    if in_comment:
        # Currently inside a comment
        if possible_comment:
            # In this case, it means we saw a *
            if c == "/":
                # Comment ended
                in_comment = False
            possible_comment = False # Will be false either way
        else:
            if c == "*":
                possible_comment = True
            # Otherwise, discard character
    else:
        # Outside of a comment
        if possible_comment:
            # We saw a /
            if c == "*":
                # Comment started
                in_comment = True
            else:
                # Replace the / because
                style_stripped += "/"
            possible_comment = False
        else:
            if c == "/":
                possible_comment = True
            else:
                style_stripped += c

print('[+] Concatenating stripped css and nav.md')

nav = open('nav.md', 'r').read()

if not nav.endswith('\n'):
    nav += '\n'

nav += '\n'
nav += '<style>\n'
nav += style_stripped
nav += '</style>'

print('[+] Saving...')

with open('navigation.md', 'w') as f:
    f.write(nav)

print('[+] Done!')
