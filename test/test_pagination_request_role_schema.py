# coding: utf-8

"""
    SwiftAI - user service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from users_client.models.pagination_request_role_schema import PaginationRequestRoleSchema

class TestPaginationRequestRoleSchema(unittest.TestCase):
    """PaginationRequestRoleSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginationRequestRoleSchema:
        """Test PaginationRequestRoleSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginationRequestRoleSchema`
        """
        model = PaginationRequestRoleSchema()
        if include_optional:
            return PaginationRequestRoleSchema(
                page = 56,
                size = 56,
                total = 56,
                data = [
                    users_client.models.role_schema.RoleSchema(
                        id = 56, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_delete = True, 
                        name = '', 
                        permissions = [
                            users_client.models.permission_schema.PermissionSchema(
                                id = 56, 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                is_delete = True, 
                                name = '', )
                            ], )
                    ]
            )
        else:
            return PaginationRequestRoleSchema(
                page = 56,
                size = 56,
                total = 56,
                data = [
                    users_client.models.role_schema.RoleSchema(
                        id = 56, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_delete = True, 
                        name = '', 
                        permissions = [
                            users_client.models.permission_schema.PermissionSchema(
                                id = 56, 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                is_delete = True, 
                                name = '', )
                            ], )
                    ],
        )
        """

    def testPaginationRequestRoleSchema(self):
        """Test PaginationRequestRoleSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()