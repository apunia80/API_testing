import constant
import json

import requests


class Organisation:
    def __init__(self):
        pass

    def create_organisation(self, query):
        response = requests.request('POST', constant.post_organisation_url,
                                    params=query)

        return response

    def get_oragnistion_id(self, response):
        resp = json.loads(response.text)
        organisation_id = resp['id']
        return organisation_id

    def get_organisation_name(self, response):
        resp = json.loads(response.text)
        displayname = resp['displayName']
        return displayname

    def get_organisation_status_code(self, response):
        statusid = response.status_code
        return statusid

    def update_the_name_of_organisation(self, organisation_id):
        updatedresponse = requests.request('PUT', constant.post_organisation_url + "/" + organisation_id,
                                           params={"displayName": "happyshappy", "key": constant.consumer_Key,
                                                   "token": constant.access_Token})
        resp = json.loads(updatedresponse.text)
        updateddisplayname = resp['displayName']
        return updateddisplayname

    def delete_organisation(self, organisation_id):
        res1 = requests.request('DELETE', constant.post_organisation_url + "/" + organisation_id,
                                params={"key": constant.consumer_Key, "token": constant.access_Token}
                                )
