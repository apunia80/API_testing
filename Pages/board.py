from Pages.organisation import Organisation
import requests
import json
import constant


class Board:
    def __init__(self):
        pass

    def create_organisation(self):
        objorganisation = Organisation()
        response = objorganisation.create_organisation(constant.querystring)
        org_id = objorganisation.get_oragnistion_id(response)
        return org_id

    def create_board(self, org_id):
        constant.board_querystring["idOrganization"] = org_id

        board_response = requests.request("POST", constant.board_base_url, params=constant.board_querystring)
        return board_response

    def name_empty_board(self, org_id):
        constant.board_querystring["idOrganization"] = org_id

        board_response = requests.request("POST", constant.board_base_url, params=constant.name_empty_query)
        return board_response.status_code

    def get_board_id(self, board_response):
        boa_id = json.loads(board_response.text)
        return boa_id['id']

    def get_board_name(self, board_response):
        boa_name = json.loads(board_response.text)
        return boa_name['name']

    def get_board_status_code(self, board_response):
        return board_response.status_code

    def delete_board(self, board_id):  # DELETE API
        response = requests.request("DELETE", constant.board_base_url + "/" + board_id, params=constant.auth)

    def update_board_using_put(self, board_id):
        boardresponse = requests.request("PUT", constant.board_base_url + "/" + board_id,
                                         params=constant.negative_board_querystring)
        updatedname = json.loads(boardresponse.text)

        return updatedname['name']
