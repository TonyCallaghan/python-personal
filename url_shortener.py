import pyshorteners

url = input("Enter URL: ")
shortener = pyshorteners.Shortener()
print(shortener.tinyurl.short(url))
