import logging
from Pages.organisation import Organisation
import pytest
import constant
from Pages.board import Board
from Pages.lists import Lists

logging.basicConfig(filename=constant.logger_file, format=constant.logger_format)


class TestLists:
    @pytest.yield_fixture()
    def list_fixture(self):
        self.objlist = Lists()
        self.objboard = Board()
        self.objorganisation = Organisation()
        self.org_id = self.objlist.organisation()
        self.board_id = self.objlist.board(self.org_id)

        self.list_response = self.objlist.create_list_using_post_api(self.board_id)
        self.list_id = self.objlist.list_id(self.list_response)
        yield

        self.objboard.delete_board(self.board_id)
        self.objorganisation.delete_organisation(self.org_id)

    @pytest.mark.usefixtures('list_fixture')
    def test_creation_of_list(self):
        response = self.objlist.create_list_using_post_api(self.board_id)
        try:
            assert response.status_code == constant.test_successful
        except:
            logging.error("list not created succesfully")

    def test_status_code_when_name_field_is_empty(self):
        objlist = Lists()
        objboard = Board()
        objorganisation = Organisation()
        org_id = objlist.organisation()
        board_id = objlist.board(org_id)

        negative_list_response = objlist.set_name_field_empty(board_id)
        objboard.delete_board(board_id)
        objorganisation.delete_organisation(org_id)
        try:
            assert negative_list_response == constant.negative_case
        except:
            logging.error(" in list it runs with blank name input")

    @pytest.mark.usefixtures('list_fixture')
    def test_check_position_is_changed_or_not(self):
        changed_pos = self.objlist.create_list_using_post_api(self.list_id)
        actual_pos = self.objlist.position_of_the_list(self.list_response)
        try:
            assert changed_pos != actual_pos
        except:
            logging.error("in list position not changed")

    @pytest.mark.usefixtures('list_fixture')
    def test_name_is_updated_or_not(self):
        updated_name = self.objlist.updated_name_of_the_list(self.list_id)
        actual_name = self.objlist.list_name(self.list_response)
        try:
            assert updated_name != actual_name
        except:
            logging.error("list name not updated")

    @pytest.mark.usefixtures('list_fixture')
    def test_put_close_archive_the_list(self):
        try:
            assert self.objlist.close_list_by_putclose_api(self.list_id) == constant.true
        except:
            logging.error("in list request not archived")

    @pytest.mark.usefixtures('list_fixture')
    def test_softlimit_status_code_run_or_not_running(self):
        try:
            assert self.objlist.set_soft_limit_of_card(self.list_id)
        except:
            logging.error("in list softlimit cannot be updated")

    @pytest.mark.usefixtures('list_fixture')
    def test_subscription_api_status_code(self):
        try:
            assert self.objlist.subscription_detail(self.list_id) == constant.test_successful
        except:
            logging.error("in list subscription not done")

    @pytest.mark.usefixtures('list_fixture')
    def test_subscription_boolien_value_the_list_is_subscribed_or_not(self):
        try:
            assert self.objlist.get_api_to_check_sybscription_in_field(self.list_id)==constant.true
        except:
            logging.error("in list channel is not subscribed")

    @pytest.mark.usefixtures('list_fixture')
    def test_get_board_gives_information_about_board_in_which_list_is_present(self):
        try:
            assert self.objlist.get_api_check_board_information(self.list_id) == constant.test_successful
        except:
            logging.error("information cannot be fatched")

    @pytest.mark.usefixtures('list_fixture')
    def test_get_all_information_about_cards(self):
        try:
            assert self.objlist.get_list_of_card_in_a_list(self.list_id) == constant.test_successful

        except:
            logging.error("list card information cannot fetched")



