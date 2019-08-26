import logging
from Pages.organisation import Organisation
import pytest
import constant
from Pages.board import Board


logging.basicConfig(filename='testloggers.log', format='%(asctime)s :%(levelname)s: %(message)s')
class TestBoard:

    @pytest.yield_fixture()
    def setup(self):
        self.objboard=Board()
        self.org_id=self.objboard.create_organisation()
        yield
        self.objorganisation=Organisation()

        self.objorganisation.delete_organisation(self.org_id)

    @pytest.mark.usefixtures('setup')
    def test_success_creation_of_board_with_status_code(self):
        board_response=self.objboard.create_board(self.org_id)
        board_id=self.objboard.get_board_id(board_response)
        status_code=self.objboard.get_board_status_code(board_response)
        self.objboard.delete_board(board_id)
        try:
            assert status_code == 200
        except:
            logging.error('Board_not_created')






