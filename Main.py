import time
import fbchat

usrname = ""
pwod = ""
client = fbchat.Client(usrname, pwod)

print("logged in as", client.getEmails())

frndname = ""
#Return a list of friends friends with the name 
friendlist = client.searchForUsers(frndname,10)
#Select top resut 
friend = friendlist[0]

sent = client.sendMessage("Bot logging in!", thread_id=friend.uid)
if sent:
    print("Message sent successfully!")
