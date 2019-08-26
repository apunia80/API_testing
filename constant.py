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
auth={"key": consumer_Key, "token": access_Token}

# board
board_base_url = "https://api.trello.com/1/boards/"
board_querystring = {"name": "Ankit", "defaultLabels": "true", "defaultLists": "true",
                     "keepFromSource": "none", "prefs_permissionLevel": "private", "prefs_voting": "disabled",
                     "prefs_comments": "members", "prefs_invitations": "members", "prefs_selfJoin": "true",
                     "prefs_cardCovers": "true", "prefs_background": "blue", "prefs_cardAging": "regular",
                     "key": consumer_Key, "token": access_Token}
