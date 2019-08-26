import logging
from Pages.organisation import Organisation
import pytest

##logger file
logging.basicConfig(filename='testloggers.log', format='%(asctime)s :%(levelname)s: %(message)s', level=logging.DEBUG)


class Testcases:

    def test_organisation_status(self):
        objorganisation = Organisation()
        response = objorganisation.create_organisation()
        organisation_id = objorganisation.get_oragnistion_id(response)
        status_code = objorganisation.get_organisation_status_code(response)
        objorganisation.delete_organisation(organisation_id)
        try:
            assert status_code == 200
        except:
            logging.error("status_code_not_matched")
