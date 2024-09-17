# coding: utf-8

"""
    SwiftAI - user service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from users_client.models.user_schema_base import UserSchemaBase

class TestUserSchemaBase(unittest.TestCase):
    """UserSchemaBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserSchemaBase:
        """Test UserSchemaBase
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSchemaBase`
        """
        model = UserSchemaBase()
        if include_optional:
            return UserSchemaBase(
                id = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                is_delete = True,
                surname = '',
                name = '',
                domain = '',
                email = '',
                invite_code = '',
                third_party_id = '',
                is_active = True,
                is_integrator = True
            )
        else:
            return UserSchemaBase(
                third_party_id = '',
        )
        """

    def testUserSchemaBase(self):
        """Test UserSchemaBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()