#URL Slug Generator — A blog post title is "Hello World! This is My First Post".
#  How do you convert it to a URL-friendly slug like "hello-world!-this-is-my-first-post"?

post=input("enter your title:")
l=post.split(" ")
print("-".join(l).lower())