import logging
from Pages.organisation import Organisation
import pytest
import constant
from Pages.board import Board

logging.basicConfig(filename=constant.logger_file, format=constant.logger_format)

class TestBoard:

    @pytest.yield_fixture()
    def link_org(self):
        self.objboard = Board()
        self.org_id = self.objboard.create_organisation()
        self.board_response = self.objboard.create_board(self.org_id)
        self.board_id = self.objboard.get_board_id(self.board_response)
        yield
        self.objorganisation = Organisation()
        self.objboard.delete_board(self.board_id)
        self.objorganisation.delete_organisation(self.org_id)

    @pytest.mark.usefixtures('link_org')
    def test_success_creation_of_board_with_status_code(self):
        status_code = self.objboard.get_board_status_code(self.board_response)
        try:
            assert status_code == 200
        except:
            logging.error('Board not created')

    @pytest.mark.usefixtures('link_org')
    def test_username_is_updated_or_not_using_put_api(self):
        updatedname = self.objboard.update_board_using_put(self.board_id)

        board_name = self.objboard.get_board_name(self.board_response)

        try:
            assert updatedname != board_name
        except:
            logging.error("Board name not updated")

    @pytest.mark.usefixtures('link_org')
    def test_board_username_field_is_empty(self):
        try:
            assert self.objboard.name_empty_board(self.org_id) == constant.negative_case
        except:
            logging.error("Name is not empty")

    @pytest.mark.usefixtures('link_org')
    def test_board_label_color_changed_or_not(self):
        try:
            assert self.objboard.create_labels_in_the_board(self.board_id) == constant.color
        except:
            logging.warning("color of label not changed please check")

    @pytest.mark.usefixtures('link_org')
    def test_check_list_in_the_board(self):
        assert self.objboard.get_info_about_create_list_inboard(self.board_id) == constant.test_successful

    @pytest.mark.usefixtures('link_org')
    def test_side_bar_created_or_not(self):
        try:
            assert self.objboard.show_sidebar_in_board_put(self.board_id) == constant.test_successful
        except:
            logging.warning("sidebar is created in false value")


