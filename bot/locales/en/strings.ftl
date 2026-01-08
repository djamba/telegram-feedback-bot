no = No
user-info =
    Name: { $name }
    ID: { NUMBER($id, useGrouping: 0) }
    Username: { $username }

user-banned = ID { NUMBER($id, useGrouping: 0) } has been added to the blocklist. The user will be notified that they are blocked if they try to send a message.
user-shadowbanned = ID { NUMBER($id, useGrouping: 0) } has been shadowbanned. The user will not be notified that they are blocked if they try to send a message.
user-unbanned = ID { NUMBER($id, useGrouping: 0) } has been unblocked.

no-banned = There are no blocked users.
list-banned-title = Blocklist:
list-shadowbanned-title = Shadowblock list:

sent-confirmation = Message sent!

command-help = Bot usage guide
command-who = Get user information
command-ban = Block a user
command-shadowban = Shadowban a user
command-unban = Unblock a user
command-list-banned = List blocked users

intro =
    This bot allows you to ask questions or provide feedback regarding the NeuroSocrates service (@NeuroSocratesBot).

help =
    This bot allows you to ask questions or provide feedback regarding the NeuroSocrates service (@NeuroSocratesBot).
    Type your question or suggestion in the chat, and we will get back to you as soon as possible.
