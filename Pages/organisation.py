import constant
import json

import requests


# organisation creation


class Organisation:
    def __init__(self):
        pass

    def create_organisation(self):
        response = requests.request('POST', constant.post_organisation_url,
                                    params=constant.querystring)

        return response

        res = json.loads(response.text)
        organisation_id = res['id']

        x = response.status_code
        print(x)
        return organisation_id

    def get_oragnistion_id(self, response):
        resp = json.loads(response.text)
        organisation_id = resp['id']
        return organisation_id

    def get_organisation_status_code(self, response):
        statusid = response.status_code
        return statusid

    def delete_organisation(self, organisation_id):
        res1 = requests.request('DELETE', constant.post_organisation_url + "/" + organisation_id,
                                params={"key": constant.consumer_Key, "token": constant.access_Token}
                                )
