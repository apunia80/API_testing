##Authentication
consumer_Key = '7608e5e8c1392a43e02abb894b95988c'
consumer_Secret = '4e44b19387ab076c60cacb8f533d5cc2f4a0c28fb15e79f3555a4cd6a0364969'
access_Token = '91ec19c534029807bc5e740cffc5910de802d2c2207f921c20497d0b1878afba'
token_Secret = '4e44b19387ab076c60cacb8f533d5cc2f4a0c28fb15e79f3555a4cd6a0364969'

# organisation
post_organisation_url = 'https://api.trello.com/1/organizations'
querystring = {"displayName": "Ankit", "key": consumer_Key, "token": access_Token}
negative_querystring = {"displayName": "", "key": consumer_Key, "token": access_Token}

updated_name = 'happyshappy'

auth = {"key": consumer_Key, "token": access_Token}

# board
board_base_url = "https://api.trello.com/1/boards/"
board_querystring = {"name": "Ankit", "defaultLabels": "true", "defaultLists": "true",
                     "keepFromSource": "none", "prefs_permissionLevel": "private", "prefs_voting": "disabled",
                     "prefs_comments": "members", "prefs_invitations": "members", "prefs_selfJoin": "true",
                     "prefs_cardCovers": "true", "prefs_background": "blue", "prefs_cardAging": "regular",
                     "key": consumer_Key, "token": access_Token}

negative_board_querystring = {"name": "Punia", "key": consumer_Key, "token": access_Token}

name_empty_query = {"name": "", "defaultLabels": "true", "defaultLists": "true",
                    "keepFromSource": "none", "prefs_permissionLevel": "private", "prefs_voting": "disabled",
                    "prefs_comments": "members", "prefs_invitations": "members", "prefs_selfJoin": "true",
                    "prefs_cardCovers": "true", "prefs_background": "blue", "prefs_cardAging": "regular",
                    "key": consumer_Key, "token": access_Token}

membercount = "billableMemberCount"

list_base_url = "https://api.trello.com/1/lists"

list_querystring = {"name": "listcreated", "key": consumer_Key, "token": access_Token}
negative_list_query = {"name": "", "key": consumer_Key, "token": access_Token}
posquery = {"value": "top", "key": consumer_Key, "token": access_Token}
list_updated_name = {"name": "cdscdscs", "key": consumer_Key, "token": access_Token}
close_put_list = {"value": "true", "key": consumer_Key, "token": access_Token}
softlimit_query = {"value": "10", "key": consumer_Key, "token": access_Token}
# subscription_query = {"value":"10,"key":consumer_Key,"token":access_Token}
logger_file = "testloggers.log"

logger_format = '%(asctime)s :%(levelname)s: %(message)s'

# card
card_base_url = 'https://api.trello.com/1/cards'
card_querystring = {"name": "dsajdhasjdsakjd", "keepFromSource": "all", "key": consumer_Key, "token": access_Token}
action_api_url = "/actions/comments"
action_query = {"text": "new text added to card", "key": consumer_Key, "token": access_Token}
labels = "/labels"
label_color_query = {"color": "yellow", "key": consumer_Key, "token": access_Token}
mark_ass="/markAssociatedNotificationsRead"
field="/pos"
listq={"fields":"all","key":consumer_Key,"token":access_Token}
empty_name_query={"name": "", "keepFromSource": "all", "key": consumer_Key, "token": access_Token}
pos='/pos'
