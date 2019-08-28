import logging
from Pages.organisation import Organisation
import pytest
import constant
from logger_file import *


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

        status_code = self.objorganisation.get_organisation_status_code(self.response)

        try:
            assert status_code == constant.test_successful
        except:
            logger.error("status_code_not_matched")

    @pytest.mark.usefixtures('fixture_organisations')
    def test_organisation_if_name_is_not_string_or_blank(self):
        # objorganisation = Organisation()
        response = self.objorganisation.create_organisation(constant.negative_querystring)
        status_code = self.objorganisation.get_organisation_status_code(response)

        try:
            assert status_code == constant.negative_case
        except:
            logger.error("check values")

    @pytest.mark.usefixtures('fixture_organisations')
    def test_organisation_if_displayname_is_updated_then(self):

        updated_displayname = self.objorganisation.update_the_name_of_organisation(self.organisation_id)
        display_name = self.objorganisation.get_organisation_name(self.response)

        try:

            assert display_name != updated_displayname
        except:
            logger.error("name cannot be updated")

    @pytest.mark.usefixtures("fixture_organisations")
    def test_number_of_mamber_in_organisation(self):
        try:
            assert self.objorganisation.get_api_in_gets_the_display_member(self.organisation_id) == constant.bmamber
        except:
            logger.error("error to get member value")

    @pytest.mark.usefixtures('fixture_organisations')
    def test_get_api_test_code_status(self):

        try:
            assert self.objorganisation.get_api_status_code(self.organisation_id) == constant.test_successful
        except:
            logger.error("status code canot be fetched")

    @pytest.mark.usefixtures('fixture_organisations')
    def test_status_code_if_organisation_id_is_wrong(self):
        try:
            organisation_id = '123455626782'
            assert self.objorganisation.get_api_status_code(organisation_id) == constant.negative_case_id_error
        except:
            logger.error("status code fetched right while org_id_is_not correct")

    @pytest.mark.usefixtures('fixture_organisations')
    def test_status_code_for_deletion_of_organisation_using_delete_api(self):
        try:
            assert self.objorganisation.delete_organisation(self.organisation_id) == constant.test_successful
        except:
            logger.error("organisation not deleted")

    @pytest.mark.usefixtures('fixture_organisations')
    def test_inside_team_a_new_collection_is_created_or_not(self):
        try:
            assert self.objorganisation.create_new_collection_in_team_using_post_tages(
            self.organisation_id) == constant.test_successful

        except:
            logger.error("organisqation inside a team collection is not created")
