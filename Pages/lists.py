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

    def board(self, org_id):
        objboard = Board()
        board_response = objboard.create_board(org_id)
        board_id = objboard.get_board_id(board_response)
        return board_id

    def create_list_using_post_api(self, board_id):  ##1
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

    def set_name_field_empty(self, board_id):  ##2
        constant.list_querystring['idBoard'] = board_id
        negative_list_response = requests.request("POST", constant.list_base_url, params=constant.negative_list_query)
        return negative_list_response.status_code

    def change_position_of_the_list_by_put_api(self, list_id):
        #  3put/pos
        list_put_response = requests.request("PUT", constant.list_base_url + "/" + list_id + "/pos",
                                             params=constant.posquery)

        list_position = json.loads(list_put_response.text)
        return list_position['pos']

    def position_of_the_list(self, list_response):
        list_response_pos = json.loads(list_response.text)
        return list_response_pos['pos']

    def updated_name_of_the_list(self, list_id):  ##4putlistid
        list_put_response = requests.request("PUT", constant.list_base_url + "/" + list_id,
                                             params=constant.list_updated_name)
        print(list_put_response.status_code)
        list_name = json.loads(list_put_response.text)
        return list_name['name']

    def close_list_by_putclose_api(self, list_id):  # 5putclose
        list_put_response = requests.request("PUT", constant.list_base_url + "/" + list_id + "/closed",
                                             params=constant.close_put_list)

        close_status = json.loads(list_put_response.text)
        return close_status['closed']

    def set_soft_limit_of_card(self, list_id):  # 6softlimit api
        list_soft_response = requests.request("PUT", constant.list_base_url + "/" + list_id + "/softLimit",
                                              params=constant.softlimit_query)

        return list_soft_response.status_code

    def subscription_detail(self, list_id):  # 7th subscription detail api
        list_sub_detail = requests.request('PUT', constant.list_base_url + '/' + list_id + '/subscribed',
                                           params=constant.close_put_list)
        return list_sub_detail.status_code

    def get_api_to_check_sybscription_in_field(self, list_id):
        get_field_response = requests.request("GET", constant.list_base_url + '/' + list_id + '/subscribed',
                                              params=constant.auth)
        boolien_value = json.loads(get_field_response.text)

        return boolien_value['_value']

    def get_api_check_board_information(self,list_id):
        get_board_info= requests.request("GET", constant.list_base_url + '/' + list_id + '/board',
                                              params=constant.auth)
        return get_board_info.status_code

    def get_list_of_card_in_a_list(self,list_id):
        get_card_info = requests.request("GET", constant.list_base_url + '/' + list_id + '/cards',
                                          params=constant.auth)
        return get_card_info.status_code



