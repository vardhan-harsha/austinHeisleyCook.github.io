import webbrowser
import sys

usersearch = sys.argv[1]
webbrowser.open("http://www.google.com/search?q=" + usersearch + "&page=1")
print("search is complete")


 
