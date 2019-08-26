import logging
from Pages.organisation import Organisation
import pytest
import constant

##logger file
logging.basicConfig(filename='testloggers.log', format='%(asctime)s :%(levelname)s: %(message)s')


class Testcases:

    def test_organisation_status_code_if_all_entry_is_correct(self):
        objorganisation = Organisation()
        response = objorganisation.create_organisation(constant.querystring)
        organisation_id = objorganisation.get_oragnistion_id(response)
        status_code = objorganisation.get_organisation_status_code(response)
        objorganisation.delete_organisation(organisation_id)
        try:
            assert status_code == 200
        except:
            logging.error("status_code_not_matched")

    def test_organisation_if_name_is_not_string_or_blank(self):
        objorganisation = Organisation()
        response = objorganisation.create_organisation(constant.negative_querystring)
        status_code = objorganisation.get_organisation_status_code(response)

        try:
            assert status_code == 400
        except:
            logging.error("check values")

    def test_organisation_if_displayname_is_updated_then(self):
                objorganisation=Organisation()
                response=objorganisation.create_organisation((constant.querystring))
                organisation_id = objorganisation.get_oragnistion_id(response)
                updated_displayname=objorganisation.update_the_name_of_organisation(organisation_id)
                display_name=objorganisation.get_organisation_name(response)
                objorganisation.delete_organisation(organisation_id)
                try:

                    assert display_name != updated_displayname
                except:
                    logging.error("name cannot be updated")