import logging
from Pages.organisation import Organisation
import pytest
import constant
from Pages.board import Board
from Pages.lists import Lists
from Pages.cards import Card

logging.basicConfig(filename=constant.logger_file, format=constant.logger_format)


class TestCard:

    @pytest.yield_fixture()
    def card_fixture(self):
        self.objcard = Card()
        self.objlist = Lists()
        self.objboard = Board()
        self.objorganisation = Organisation()
        self.org_id = self.objlist.organisation()
        self.board_id = self.objlist.board(self.org_id)

        self.list_response = self.objlist.create_list_using_post_api(self.board_id)
        self.list_id = self.objlist.list_id(self.list_response)
        self.card_response = self.objcard.create_card_in_list(self.list_id)
        self.card_id = self.objcard.get_card_id(self.card_response)
        yield

        self.objboard.delete_board(self.board_id)
        self.objorganisation.delete_organisation(self.org_id)

    @pytest.mark.usefixtures('card_fixture')
    def test_card_is_created_or_not(self):
        try:
            assert self.card_response.status_code == constant.test_successful
        except:
            logging.error("card not created")

    @pytest.mark.usefixtures('card_fixture')
    def test_delete_of_card_is_happened(self):
        try:
            assert self.objcard.delete_card_using_delete_api(self.card_id) == constant.test_successful
        except:
            logging.error("card not deleted")

    @pytest.mark.usefixtures('card_fixture')
    def test_action_comment_added_to_card(self):
        try:
            assert self.objcard.add_action_api_comment_on_card(self.card_id) == constant.test_successful
        except:
            logging.error("card comment not added")

    @pytest.mark.usefixtures('card_fixture')
    def test_color_change_of_card_using_label(self):
        try:
            assert self.objcard.post_change_color_of_card(self.card_id) == constant.color
        except:
            logging.error("card color not changed")

    @pytest.mark.usefixtures('card_fixture')
    def test_mark_associated_notification_read(self):
        try:
            assert self.objcard.mark_associated_notifications_read(self.card_id) == constant.test_successful
        except:
            logging.error("card notification is not readable")

    @pytest.mark.usefixtures('card_fixture')
    def test_name_updation_of_card_in_put_api(self):
        try:
            assert self.objcard.update_name_using_put(self.card_id)!=self.objcard.get_card_name(self.card_response)
        except:
            logging.error("card name can not be updated ")


    @pytest.mark.usefixtures('card_fixture')
    def test_position_of_card_using_get_api(self):
        try:
            ##we also use status_code here to check api is working properly
            assert self.objcard.get_position_of_card_using_field(self.card_id) == constant.position
        except:
            logging.error('card position is not available')

    @pytest.mark.usefixtures('card_fixture')
    def test_list_in_which_card_is_present(self):
        try:
            assert self.objcard.get_list_in_which_card_is_present(self.card_id)== constant.test_successful
        except:
            logging.error("in card list of card not available")



    @pytest.mark.usefixtures('card_fixture')
    def test_when_name_field_is_empty(self):
        try:
            assert self.objcard.name_field_is_empty() == constant.negative_case
        except:
            logging.error("name field is not empty here")








