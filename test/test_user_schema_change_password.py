# coding: utf-8

"""
    SwiftAI - user service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from users_client.models.user_schema_change_password import UserSchemaChangePassword

class TestUserSchemaChangePassword(unittest.TestCase):
    """UserSchemaChangePassword unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserSchemaChangePassword:
        """Test UserSchemaChangePassword
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSchemaChangePassword`
        """
        model = UserSchemaChangePassword()
        if include_optional:
            return UserSchemaChangePassword(
                current_password = '',
                new_password = '',
                repeat_password = ''
            )
        else:
            return UserSchemaChangePassword(
                current_password = '',
                new_password = '',
                repeat_password = '',
        )
        """

    def testUserSchemaChangePassword(self):
        """Test UserSchemaChangePassword"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
