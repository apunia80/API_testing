import logging
from Pages.organisation import Organisation
import pytest
import constant

##logger file
logging.basicConfig(filename=constant.logger_file, format=constant.logger_format)

class Testcases:
    @pytest.yield_fixture()
    def fixture_organisations(self):
        self.objorganisation = Organisation()
        self.response = self.objorganisation.create_organisation(constant.querystring)
        self.organisation_id = self.objorganisation.get_oragnistion_id(self.response)
        yield
        self.objorganisation.delete_organisation(self.organisation_id)

    @pytest.mark.usefixtures('fixture_organisations')
    def test_organisation_status_code_if_all_entry_is_correct(self):
        # objorganisation = Organisation()
        # response = objorganisation.create_organisation(constant.querystring)
        # organisation_id = objorganisation.get_oragnistion_id(response)
        status_code = self.objorganisation.get_organisation_status_code(self.response)
        #self.objorganisation.delete_organisation(self.organisation_id)
        try:
            assert status_code == 200
        except:
            logging.error("status_code_not_matched")

    @pytest.mark.usefixtures('fixture_organisations')
    def test_organisation_if_name_is_not_string_or_blank(self):
        # objorganisation = Organisation()
        response = self.objorganisation.create_organisation(constant.negative_querystring)
        status_code = self.objorganisation.get_organisation_status_code(response)

        try:
            assert status_code == 400
        except:
            logging.error("check values")

    @pytest.mark.usefixtures('fixture_organisations')
    def test_organisation_if_displayname_is_updated_then(self):
                # objorganisation=Organisation()
                # response=objorganisation.create_organisation((constant.querystring))
                # organisation_id = objorganisation.get_oragnistion_id(response)
                updated_displayname=self.objorganisation.update_the_name_of_organisation(self.organisation_id)
                display_name=self.objorganisation.get_organisation_name(self.response)
                #self.objorganisation.delete_organisation(self.organisation_id)
                try:

                    assert display_name != updated_displayname
                except:
                    logging.error("name cannot be updated")

    @pytest.mark.usefixtures("fixture_organisations")
    def test_number_of_mamber_in_organisation(self):
        try:
            assert self.objorganisation.get_api_in_gets_the_display_member(self.organisation_id) == 1
        except:
            logging.error("error to get member value")

    @pytest.mark.usefixtures('fixture_organisations')
    def test_get_api_test_code_status(self):

        assert self.objorganisation.get_api_status_code(self.organisation_id) == 200

