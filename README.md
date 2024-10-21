# users-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.0.0
- Generator version: 7.9.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import users_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import users_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import users_client
from users_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /user_service/api
# See configuration.py for a list of all supported configuration parameters.
configuration = users_client.Configuration(
    host = "/user_service/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = users_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with users_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_client.AuthApi(api_client)
    username = 'username_example' # str | 
    password = 'password_example' # str | 
    grant_type = 'grant_type_example' # str |  (optional)
    scope = '' # str |  (optional) (default to '')
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Auth:Users.Login
        api_response = api_instance.auth_users_login(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        print("The response of AuthApi->auth_users_login:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->auth_users_login: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to */user_service/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**auth_users_login**](docs/AuthApi.md#auth_users_login) | **POST** /v1/auth/login | Auth:Users.Login
*AuthApi* | [**auth_users_logout**](docs/AuthApi.md#auth_users_logout) | **POST** /v1/auth/logout | Auth:Users.Logout
*InvitedUserApi* | [**check_invite_by_integrator_id_users_user_id_check_invite_integrator_id_get**](docs/InvitedUserApi.md#check_invite_by_integrator_id_users_user_id_check_invite_integrator_id_get) | **GET** /users/{user_id}/check-invite/{integrator_id} | Check Invite By Integrator Id
*InvitedUserApi* | [**check_invite_users_user_id_check_invite_get**](docs/InvitedUserApi.md#check_invite_users_user_id_check_invite_get) | **GET** /users/{user_id}/check-invite | Check Invite
*InvitedUserApi* | [**get_integrator_users_user_id_integrator_get**](docs/InvitedUserApi.md#get_integrator_users_user_id_integrator_get) | **GET** /users/{user_id}/integrator | Get Integrator
*InvitedUserApi* | [**get_invited_users_users_integrator_id_invited_get**](docs/InvitedUserApi.md#get_invited_users_users_integrator_id_invited_get) | **GET** /users/{integrator_id}/invited | Get Invited Users
*InvitedUserApi* | [**invite_user_users_invite_post**](docs/InvitedUserApi.md#invite_user_users_invite_post) | **POST** /users/invite | Invite User
*InvitedUserApi* | [**v1_add_invited_user**](docs/InvitedUserApi.md#v1_add_invited_user) | **POST** /v1/users/invite | Users:Add Invited User
*InvitedUserApi* | [**v1_check_invited_user**](docs/InvitedUserApi.md#v1_check_invited_user) | **GET** /v1/users/{user_id}/check-invite | Users:Check Invited User
*InvitedUserApi* | [**v1_check_invited_user_by_integrator**](docs/InvitedUserApi.md#v1_check_invited_user_by_integrator) | **GET** /v1/users/{user_id}/check-invite/{integrator_id} | Users:Check Invited User By Integrator
*InvitedUserApi* | [**v1_get_integrator**](docs/InvitedUserApi.md#v1_get_integrator) | **GET** /v1/users/{user_id}/integrator | Users:Get Integrator
*InvitedUserApi* | [**v1_get_invited_users**](docs/InvitedUserApi.md#v1_get_invited_users) | **GET** /v1/users/{integrator_id}/invited | Users:Get Invited Users
*PermissionApi* | [**create_permission_permissions_post**](docs/PermissionApi.md#create_permission_permissions_post) | **POST** /permissions/ | Create Permission
*PermissionApi* | [**delete_permission_permissions_permission_id_delete**](docs/PermissionApi.md#delete_permission_permissions_permission_id_delete) | **DELETE** /permissions/{permission_id} | Delete Permission
*PermissionApi* | [**get_permission_by_id_permissions_permission_id_get**](docs/PermissionApi.md#get_permission_by_id_permissions_permission_id_get) | **GET** /permissions/{permission_id} | Get Permission By Id
*PermissionApi* | [**get_permissions_permissions_get**](docs/PermissionApi.md#get_permissions_permissions_get) | **GET** /permissions/ | Get Permissions
*PermissionApi* | [**v1_create_permission**](docs/PermissionApi.md#v1_create_permission) | **POST** /v1/permissions | Permissions:Create Permission
*PermissionApi* | [**v1_delete_permission**](docs/PermissionApi.md#v1_delete_permission) | **DELETE** /v1/permissions/{permission_id} | Permissions:Delete Permission
*PermissionApi* | [**v1_get_permission_by_id**](docs/PermissionApi.md#v1_get_permission_by_id) | **GET** /v1/permissions/{permission_id} | Permissions:Get Permission By Id
*PermissionApi* | [**v1_get_permissions**](docs/PermissionApi.md#v1_get_permissions) | **GET** /v1/permissions | Permissions:Get Permissions
*RolesApi* | [**add_permission_to_role_roles_role_id_permissions_permission_id_post**](docs/RolesApi.md#add_permission_to_role_roles_role_id_permissions_permission_id_post) | **POST** /roles/{role_id}/permissions/{permission_id} | Add Permission To Role
*RolesApi* | [**add_permissions_to_role_roles_role_id_permissions_post**](docs/RolesApi.md#add_permissions_to_role_roles_role_id_permissions_post) | **POST** /roles/{role_id}/permissions | Add Permissions To Role
*RolesApi* | [**create_role_roles_post**](docs/RolesApi.md#create_role_roles_post) | **POST** /roles/ | Create Role
*RolesApi* | [**delete_role_roles_role_id_delete**](docs/RolesApi.md#delete_role_roles_role_id_delete) | **DELETE** /roles/{role_id} | Delete Role
*RolesApi* | [**get_role_by_id_roles_role_id_get**](docs/RolesApi.md#get_role_by_id_roles_role_id_get) | **GET** /roles/{role_id} | Get Role By Id
*RolesApi* | [**get_roles_roles_get**](docs/RolesApi.md#get_roles_roles_get) | **GET** /roles/ | Get Roles
*RolesApi* | [**remove_permission_to_role_roles_role_id_permissions_permission_id_delete**](docs/RolesApi.md#remove_permission_to_role_roles_role_id_permissions_permission_id_delete) | **DELETE** /roles/{role_id}/permissions/{permission_id} | Remove Permission To Role
*RolesApi* | [**v1_add_permission_by_role**](docs/RolesApi.md#v1_add_permission_by_role) | **POST** /v1/roles/{role_id}/permissions/{permission_id} | Roles:Add Permission By Role
*RolesApi* | [**v1_add_permissions_by_role**](docs/RolesApi.md#v1_add_permissions_by_role) | **POST** /v1/roles/{role_id}/permissions | Roles:Add Permissions By Role
*RolesApi* | [**v1_create_role**](docs/RolesApi.md#v1_create_role) | **POST** /v1/roles | Roles:Create Role
*RolesApi* | [**v1_get_role_by_id**](docs/RolesApi.md#v1_get_role_by_id) | **GET** /v1/roles/{role_id} | Roles:Get Role By Id
*RolesApi* | [**v1_get_roles**](docs/RolesApi.md#v1_get_roles) | **GET** /v1/roles | Roles:Get Roles
*RolesApi* | [**v1_remove_permission_by_role**](docs/RolesApi.md#v1_remove_permission_by_role) | **DELETE** /v1/roles/{role_id}/permissions/{permission_id} | Roles:Remove Permission By Role
*RolesApi* | [**v1_remove_role**](docs/RolesApi.md#v1_remove_role) | **DELETE** /v1/roles/{role_id} | Roles:Remove Role
*UsersApi* | [**change_user_email_users_user_id_change_email_post**](docs/UsersApi.md#change_user_email_users_user_id_change_email_post) | **POST** /users/{user_id}/change_email | Change User Email
*UsersApi* | [**change_user_password_users_user_id_change_password_post**](docs/UsersApi.md#change_user_password_users_user_id_change_password_post) | **POST** /users/{user_id}/change_password | Change User Password
*UsersApi* | [**create_user_users_post**](docs/UsersApi.md#create_user_users_post) | **POST** /users | Create User
*UsersApi* | [**get_user_by_id_users_user_id_get**](docs/UsersApi.md#get_user_by_id_users_user_id_get) | **GET** /users/{user_id} | Get User By Id
*UsersApi* | [**get_users_users_get**](docs/UsersApi.md#get_users_users_get) | **GET** /users/ | Get Users
*UsersApi* | [**login_user_users_login_post**](docs/UsersApi.md#login_user_users_login_post) | **POST** /users/login | Login User
*UsersApi* | [**register_user_users_user_id_register_post**](docs/UsersApi.md#register_user_users_user_id_register_post) | **POST** /users/{user_id}/register | Register User
*UsersApi* | [**update_user_users_user_id_put**](docs/UsersApi.md#update_user_users_user_id_put) | **PUT** /users/{user_id} | Update User
*UsersApi* | [**v1_change_email**](docs/UsersApi.md#v1_change_email) | **POST** /v1/users/{user_id}/change_email | Users:Change Email
*UsersApi* | [**v1_change_password**](docs/UsersApi.md#v1_change_password) | **POST** /v1/users/{user_id}/change_password | Users:Change Password
*UsersApi* | [**v1_check_register**](docs/UsersApi.md#v1_check_register) | **GET** /v1/users/{user_id}/check_register | Users:Check Register
*UsersApi* | [**v1_create_user**](docs/UsersApi.md#v1_create_user) | **POST** /v1/users | Users:Create User
*UsersApi* | [**v1_get_me**](docs/UsersApi.md#v1_get_me) | **GET** /v1/users/me | Users:Get Me
*UsersApi* | [**v1_get_role_by_user_id**](docs/UsersApi.md#v1_get_role_by_user_id) | **GET** /v1/users/{user_id}/role | Users:Get Role By User Id
*UsersApi* | [**v1_get_user_by_id**](docs/UsersApi.md#v1_get_user_by_id) | **GET** /v1/users/{user_id} | Users:Get User By Id
*UsersApi* | [**v1_get_users**](docs/UsersApi.md#v1_get_users) | **GET** /v1/users | Users:Get Users
*UsersApi* | [**v1_register**](docs/UsersApi.md#v1_register) | **POST** /v1/users/{user_id}/register | Users:Register
*UsersApi* | [**v1_update_user**](docs/UsersApi.md#v1_update_user) | **PUT** /v1/users/{user_id} | Users:Update User
*DefaultApi* | [**health_check_health_get**](docs/DefaultApi.md#health_check_health_get) | **GET** /health | Health Check


## Documentation For Models

 - [BearerResponse](docs/BearerResponse.md)
 - [Detail](docs/Detail.md)
 - [ErrorModel](docs/ErrorModel.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [HealthCheckDetailsSchema](docs/HealthCheckDetailsSchema.md)
 - [HealthCheckResponse](docs/HealthCheckResponse.md)
 - [InviteUserSchemaAdd](docs/InviteUserSchemaAdd.md)
 - [PaginationRequestPermissionSchema](docs/PaginationRequestPermissionSchema.md)
 - [PaginationRequestRoleSchema](docs/PaginationRequestRoleSchema.md)
 - [PaginationRequestUserSchemaBase](docs/PaginationRequestUserSchemaBase.md)
 - [PermissionSchema](docs/PermissionSchema.md)
 - [PermissionSchemaAdd](docs/PermissionSchemaAdd.md)
 - [ResultRequest](docs/ResultRequest.md)
 - [RoleSchema](docs/RoleSchema.md)
 - [RoleSchemaAdd](docs/RoleSchemaAdd.md)
 - [RoleSchemaAddPermission](docs/RoleSchemaAddPermission.md)
 - [ServiceErrorPydantic](docs/ServiceErrorPydantic.md)
 - [StatusDatabase](docs/StatusDatabase.md)
 - [StatusRedis](docs/StatusRedis.md)
 - [TypeErrorEnum](docs/TypeErrorEnum.md)
 - [UserSchemaAdd](docs/UserSchemaAdd.md)
 - [UserSchemaBase](docs/UserSchemaBase.md)
 - [UserSchemaChangeEmail](docs/UserSchemaChangeEmail.md)
 - [UserSchemaChangePassword](docs/UserSchemaChangePassword.md)
 - [UserSchemaLogin](docs/UserSchemaLogin.md)
 - [UserSchemaRegister](docs/UserSchemaRegister.md)
 - [UserSchemaUpdate](docs/UserSchemaUpdate.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="HTTPBearer"></a>
### HTTPBearer

- **Type**: Bearer authentication

<a id="OAuth2PasswordBearer"></a>
### OAuth2PasswordBearer

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: N/A


## Author




