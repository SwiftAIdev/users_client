# coding: utf-8

"""
    SwiftAI - user service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from users_client.models.result_request import ResultRequest

class TestResultRequest(unittest.TestCase):
    """ResultRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResultRequest:
        """Test ResultRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResultRequest`
        """
        model = ResultRequest()
        if include_optional:
            return ResultRequest(
                result = True
            )
        else:
            return ResultRequest(
                result = True,
        )
        """

    def testResultRequest(self):
        """Test ResultRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
