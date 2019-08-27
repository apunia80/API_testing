import constant
import json

import requests


class Organisation:
    def __init__(self):
        pass

    def create_organisation(self, query):  # 1st API POST

        response = requests.request('POST', constant.post_organisation_url,
                                    params=query)

        return response

    def get_oragnistion_id(self, response):
        org_id = json.loads(response.text)
        return org_id['id']

    def get_organisation_name(self, response):
        resp = json.loads(response.text)
        return resp['displayName']

    def get_organisation_status_code(self, response):
        return response.status_code

    def get_api_in_gets_the_display_member(self, organisation_id):  ##get api
        getresponse = requests.request('GET',
                                       constant.post_organisation_url + "/" + organisation_id + '/' + constant.membercount,
                                       params={"key": constant.consumer_Key, "token": constant.access_Token})
        member_value = json.loads(getresponse.text)
        return member_value['_value']

    def get_api_status_code(self,organisation_id):
        getresponse = requests.request('GET',
                                       constant.post_organisation_url + "/" + organisation_id,
                                       params={"key": constant.consumer_Key, "token": constant.access_Token})

        return getresponse.status_code

    def update_the_name_of_organisation(self, organisation_id):  ##2nd api PUT
        updatedresponse = requests.request('PUT', constant.post_organisation_url + "/" + organisation_id,
                                           params={"displayName": constant.updated_name, "key": constant.consumer_Key,
                                                   "token": constant.access_Token})
        updateddisplayname = json.loads(updatedresponse.text)

        return updateddisplayname['displayName']

    def delete_organisation(self, organisation_id):  # 4rd api Delete
        res1 = requests.request('DELETE', constant.post_organisation_url + "/" + organisation_id,
                                params={"key": constant.consumer_Key, "token": constant.access_Token}
                                )
