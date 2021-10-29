import pyshorteners

url = ""
#insira a url que deseja encurtar

link = pyshorteners.Shortener()

shorten_url = link.tinyurl.short(url)
print(f'\n{shorten+url}')
