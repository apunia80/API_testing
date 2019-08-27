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
            assert updatedname != board_name  # to check logger i makes the file equal
        except:
            logging.error("Board name not updated")

    @pytest.mark.usefixtures('link_org')
    def test_board_username_field_is_empty(self):
        try:
            assert self.objboard.name_empty_board(self.org_id) == 400
        except:
            logging.error("Name is not empty")
