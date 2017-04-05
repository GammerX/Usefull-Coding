# Remove left space(s) in string

'''def avd_1st_space(string):
    return string.split(None, 0)[0]

str = "       Hello, i\'m a horse !"

print(avd_1st_space(str))'''

# Code above has been replace by this instead

str = "       Hello, i\'m a horse !"
str.lstrip()

# [OUTPUT] --> "Hello, i'm a horse !"
