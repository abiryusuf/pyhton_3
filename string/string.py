# using three quotes for multiline 
u = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(u)

# get charater at position
a = "Abir Yusuf"
print(a[5])

# convert
y = 10
v = float(y)
print(v)

#loop 
for y in a:
    print(y)

# String length
x = "Living in New York"
print(len("Length " + x))

# Check String 
text = "The best thing in life are freedom"
if "Best" not in text:
    print("Yes, 'best' is present")
    
  
print("The " in text)

i = "abir"

for i in range(5):
    print(i)


def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_email
        return new_email
    return email
print(replace_domain("abir@yahoo.com", "abir@yahoo.com", "abir@gmail.com"))