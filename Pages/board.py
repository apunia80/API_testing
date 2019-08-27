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

    def create_board(self, org_id):  # 1st api
        constant.board_querystring["idOrganization"] = org_id

        board_response = requests.request("POST", constant.board_base_url, params=constant.board_querystring)
        return board_response

    def name_empty_board(self, org_id):  # 2nd api
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

    def delete_board(self, board_id):  # 3rd DELETE API
        response = requests.request("DELETE", constant.board_base_url + "/" + board_id, params=constant.auth)

    def update_board_using_put(self, board_id):  # 4th api
        boardresponse = requests.request("PUT", constant.board_base_url + "/" + board_id,
                                         params=constant.negative_board_querystring)
        updatedname = json.loads(boardresponse.text)

        return updatedname['name']

    def create_labels_in_the_board(self, board_id):
        response_label = requests.request("POST", constant.board_base_url + "/" + board_id + constant.blabel,
                                          params=constant.blabelquery)

        label_color = json.loads(response_label.text)
        return label_color['color']

        return response_label

    def get_info_about_create_list_inboard(self, board_id):
        get_list_response = requests.request("GET", constant.board_base_url + "/" + board_id + constant.blist,
                                             params=constant.blistcheckquery)
        return get_list_response.status_code

    def show_sidebar_in_board_put(self, board_id):
        get_info = requests.request("PUT", constant.board_base_url + '/' + board_id + constant.sidebarq,
                                    params=constant.sidebarquery)

        return get_info.status_code
