from Pages.lists import Lists
from Pages.board import Board
from Pages.organisation import Organisation
import constant
import json
import requests


class Card:
    def __init__(self):
        pass

    def get_list_id(self, board_id):
        objlist = Lists()
        list_response = objlist.create_list_using_post_api(board_id)
        list_id = objlist.list_id(list_response)
        return list_id

    def get_list_name(self, board_id):
        objlist = Lists()
        list_response = objlist.create_list_using_post_api(board_id)
        get_list_name = objlist.list_name(list_response)
        return get_list_name

    def create_card_in_list(self, list_id):  # 1stapi
        constant.card_querystring['idList'] = list_id
        card_response = requests.request("POST", constant.card_base_url, params=constant.card_querystring)
        return card_response

    def get_card_id(self, card_response):
        card_id = json.loads(card_response.text)
        return card_id['id']

    def get_card_name(self, card_response):
        card_name = json.loads(card_response.text)
        return card_name['name']

    def get_status_code_of_card(self, card_response):
        return card_response.status_code

    def delete_card_using_delete_api(self, card_id):
        response = requests.request("DELETE", constant.card_base_url + "/" + card_id, params=constant.auth)
        return response.status_code

    def add_action_api_comment_on_card(self, card_id):
        action_response = requests.request("POST", constant.card_base_url + "/" + card_id + constant.action_api_url,
                                           params=constant.action_query)

        return action_response.status_code

    def post_change_color_of_card(self, card_id):
        change_color = requests.request("POST", constant.card_base_url + '/' + card_id + constant.labels,
                                        params=constant.label_color_query)
        # print(change_color)
        color_of_card = json.loads(change_color.text)
        return color_of_card['color']

    def mark_associated_notifications_read(self, card_id):
        mark = requests.request("POST", constant.card_base_url + '/' + card_id + constant.mark_ass,
                                params=constant.auth)
        return mark.status_code

    def update_name_using_put(self, card_id):
        updated_name = requests.request("PUT", constant.card_base_url + '/' + card_id,
                                        params=constant.list_updated_name)
        final_updated_name = json.loads(updated_name.text)
        return final_updated_name['name']

    def get_position_of_card_using_field(self, card_id):
        card_detail = requests.request("GET", constant.card_base_url + "/" + card_id + constant.field,
                                         params=constant.auth)
        card_position=json.loads(card_detail.text)
        return card_position['_value']

    def get_list_in_which_card_is_present(self,card_id):
        card_info=requests.request("GET", constant.card_base_url + "/" + card_id + constant.pos,
                                         params=constant.listq)
        return card_info.status_code

    def name_field_is_empty(self):
        create_card= requests.request("POST", constant.card_base_url, params=constant.empty_name_query)
        return create_card.status_code


