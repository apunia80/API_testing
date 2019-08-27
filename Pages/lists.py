from Pages.board import Board
from Pages.organisation import Organisation
import constant
import requests
import json


class Lists:
    def __init__(self):
        pass

    def organisation(self):
        objboard = Board()
        org_id = objboard.create_organisation()
        return org_id
    def board(self,org_id):
        objboard=Board()
        board_response = objboard.create_board(org_id)
        board_id = objboard.get_board_id(board_response)
        return board_id

    def create_list_using_post_api(self, board_id):
        constant.list_querystring['idBoard'] = board_id
        list_response = requests.request("POST", constant.list_base_url, params=constant.list_querystring)
        return list_response

    def list_id(self, list_response):
        list_id = json.loads(list_response.text)
        return list_id['id']

    def list_name(self, list_response):
        list_name = json.loads(list_response.text)
        return list_name['name']

    def list_status_code(self, list_response):
        list_status_code = list_response.status_code
        return list_status_code

    def set_name_field_empty(self,board_id):
        constant.list_querystring['idBoard'] = board_id
        negative_list_response = requests.request("POST", constant.list_base_url, params=constant.negative_list_query)
        return negative_list_response.status_code




''''
list=Lists()
org_id=list.organisation()
board_id=list.board(org_id)
list_response=list.create_list_using_post_api(board_id)
print(list.list_id(list_response))
print(list.list_name(list_response))
print(list.list_status_code(list_response))
objboard=Board()
objboard.delete_board(board_id)
objorganisation=Organisation()

objorganisation.delete_organisation(org_id)
'''
