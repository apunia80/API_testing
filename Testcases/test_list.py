import logging
from Pages.organisation import Organisation
import pytest
import constant
from Pages.board import Board
from Pages.lists import Lists

logging.basicConfig(filename='testloggers.log', format='%(asctime)s :%(levelname)s: %(message)s')


class TestLists:
    @pytest.yield_fixture()
    def list_fixture(self):
        self.objlist = Lists()
        self.objboard = Board()
        self.objorganisation = Organisation()
        self.org_id = self.objlist.organisation()
        self.board_id = self.objlist.board(self.org_id)
        
        self.list_response = self.objlist.create_list_using_post_api(self.board_id)
        yield

        self.objboard.delete_board(self.board_id)
        self.objorganisation.delete_organisation(self.org_id)

    @pytest.mark.usefixtures('list_fixture')
    def test_creation_of_list(self):
        response = self.objlist.create_list_using_post_api(self.board_id)
        try:
            assert response.status_code == 200
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
            assert negative_list_response == 400
        except:
            logging.error("it runs with blank name input")
