# coding: utf-8

"""
    SwiftAI - user service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from users_client.api.invited_user_api import InvitedUserApi


class TestInvitedUserApi(unittest.TestCase):
    """InvitedUserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InvitedUserApi()

    def tearDown(self) -> None:
        pass

    def test_check_invite_by_integrator_id_users_user_id_check_invite_integrator_id_get(self) -> None:
        """Test case for check_invite_by_integrator_id_users_user_id_check_invite_integrator_id_get

        Check Invite By Integrator Id
        """
        pass

    def test_check_invite_users_user_id_check_invite_get(self) -> None:
        """Test case for check_invite_users_user_id_check_invite_get

        Check Invite
        """
        pass

    def test_get_integrator_users_user_id_integrator_get(self) -> None:
        """Test case for get_integrator_users_user_id_integrator_get

        Get Integrator
        """
        pass

    def test_get_invited_users_users_integrator_id_invited_get(self) -> None:
        """Test case for get_invited_users_users_integrator_id_invited_get

        Get Invited Users
        """
        pass

    def test_invite_user_users_invite_post(self) -> None:
        """Test case for invite_user_users_invite_post

        Invite User
        """
        pass


if __name__ == '__main__':
    unittest.main()
