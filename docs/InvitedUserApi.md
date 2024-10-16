# users_client.InvitedUserApi

All URIs are relative to */user_service/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_invite_by_integrator_id_users_user_id_check_invite_integrator_id_get**](InvitedUserApi.md#check_invite_by_integrator_id_users_user_id_check_invite_integrator_id_get) | **GET** /users/{user_id}/check-invite/{integrator_id} | Check Invite By Integrator Id
[**check_invite_users_user_id_check_invite_get**](InvitedUserApi.md#check_invite_users_user_id_check_invite_get) | **GET** /users/{user_id}/check-invite | Check Invite
[**get_integrator_users_user_id_integrator_get**](InvitedUserApi.md#get_integrator_users_user_id_integrator_get) | **GET** /users/{user_id}/integrator | Get Integrator
[**get_invited_users_users_integrator_id_invited_get**](InvitedUserApi.md#get_invited_users_users_integrator_id_invited_get) | **GET** /users/{integrator_id}/invited | Get Invited Users
[**invite_user_users_invite_post**](InvitedUserApi.md#invite_user_users_invite_post) | **POST** /users/invite | Invite User
[**v1_add_invited_user**](InvitedUserApi.md#v1_add_invited_user) | **POST** /v1/users/invite | Users:Add Invited User
[**v1_check_invited_user**](InvitedUserApi.md#v1_check_invited_user) | **GET** /v1/users/{user_id}/check-invite | Users:Check Invited User
[**v1_check_invited_user_by_integrator**](InvitedUserApi.md#v1_check_invited_user_by_integrator) | **GET** /v1/users/{user_id}/check-invite/{integrator_id} | Users:Check Invited User By Integrator
[**v1_get_integrator**](InvitedUserApi.md#v1_get_integrator) | **GET** /v1/users/{user_id}/integrator | Users:Get Integrator
[**v1_get_invited_users**](InvitedUserApi.md#v1_get_invited_users) | **GET** /v1/users/{integrator_id}/invited | Users:Get Invited Users


# **check_invite_by_integrator_id_users_user_id_check_invite_integrator_id_get**
> ResultRequest check_invite_by_integrator_id_users_user_id_check_invite_integrator_id_get(user_id, integrator_id)

Check Invite By Integrator Id

Check user invitation.  This endpoint verifies if a user was invited by a specific integrator.

### Example


```python
import users_client
from users_client.models.result_request import ResultRequest
from users_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /user_service/api
# See configuration.py for a list of all supported configuration parameters.
configuration = users_client.Configuration(
    host = "/user_service/api"
)


# Enter a context with an instance of the API client
with users_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_client.InvitedUserApi(api_client)
    user_id = 'user_id_example' # str | 
    integrator_id = 'integrator_id_example' # str | 

    try:
        # Check Invite By Integrator Id
        api_response = api_instance.check_invite_by_integrator_id_users_user_id_check_invite_integrator_id_get(user_id, integrator_id)
        print("The response of InvitedUserApi->check_invite_by_integrator_id_users_user_id_check_invite_integrator_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitedUserApi->check_invite_by_integrator_id_users_user_id_check_invite_integrator_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **integrator_id** | **str**|  | 

### Return type

[**ResultRequest**](ResultRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_invite_users_user_id_check_invite_get**
> ResultRequest check_invite_users_user_id_check_invite_get(user_id)

Check Invite

Check user invitation.  This endpoint verifies if a user was invited by a specific integrator.

### Example


```python
import users_client
from users_client.models.result_request import ResultRequest
from users_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /user_service/api
# See configuration.py for a list of all supported configuration parameters.
configuration = users_client.Configuration(
    host = "/user_service/api"
)


# Enter a context with an instance of the API client
with users_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_client.InvitedUserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Check Invite
        api_response = api_instance.check_invite_users_user_id_check_invite_get(user_id)
        print("The response of InvitedUserApi->check_invite_users_user_id_check_invite_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitedUserApi->check_invite_users_user_id_check_invite_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**ResultRequest**](ResultRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integrator_users_user_id_integrator_get**
> UserSchemaBase get_integrator_users_user_id_integrator_get(user_id)

Get Integrator

Get integrator by user ID.  This endpoint retrieves the integrator associated with a specific user.

### Example


```python
import users_client
from users_client.models.user_schema_base import UserSchemaBase
from users_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /user_service/api
# See configuration.py for a list of all supported configuration parameters.
configuration = users_client.Configuration(
    host = "/user_service/api"
)


# Enter a context with an instance of the API client
with users_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_client.InvitedUserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get Integrator
        api_response = api_instance.get_integrator_users_user_id_integrator_get(user_id)
        print("The response of InvitedUserApi->get_integrator_users_user_id_integrator_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitedUserApi->get_integrator_users_user_id_integrator_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserSchemaBase**](UserSchemaBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**204** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invited_users_users_integrator_id_invited_get**
> PaginationRequestUserSchemaBase get_invited_users_users_integrator_id_invited_get(integrator_id, page=page, size=size)

Get Invited Users

Get invited users.  This endpoint retrieves a paginated list of users invited by a specific user.

### Example


```python
import users_client
from users_client.models.pagination_request_user_schema_base import PaginationRequestUserSchemaBase
from users_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /user_service/api
# See configuration.py for a list of all supported configuration parameters.
configuration = users_client.Configuration(
    host = "/user_service/api"
)


# Enter a context with an instance of the API client
with users_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_client.InvitedUserApi(api_client)
    integrator_id = 'integrator_id_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    size = 25 # int |  (optional) (default to 25)

    try:
        # Get Invited Users
        api_response = api_instance.get_invited_users_users_integrator_id_invited_get(integrator_id, page=page, size=size)
        print("The response of InvitedUserApi->get_invited_users_users_integrator_id_invited_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitedUserApi->get_invited_users_users_integrator_id_invited_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integrator_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 25]

### Return type

[**PaginationRequestUserSchemaBase**](PaginationRequestUserSchemaBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**204** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_user_users_invite_post**
> ResultRequest invite_user_users_invite_post(invite_user_schema_add)

Invite User

Invite a new user.  This endpoint allows inviting a new user.

### Example


```python
import users_client
from users_client.models.invite_user_schema_add import InviteUserSchemaAdd
from users_client.models.result_request import ResultRequest
from users_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /user_service/api
# See configuration.py for a list of all supported configuration parameters.
configuration = users_client.Configuration(
    host = "/user_service/api"
)


# Enter a context with an instance of the API client
with users_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_client.InvitedUserApi(api_client)
    invite_user_schema_add = users_client.InviteUserSchemaAdd() # InviteUserSchemaAdd | 

    try:
        # Invite User
        api_response = api_instance.invite_user_users_invite_post(invite_user_schema_add)
        print("The response of InvitedUserApi->invite_user_users_invite_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitedUserApi->invite_user_users_invite_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_user_schema_add** | [**InviteUserSchemaAdd**](InviteUserSchemaAdd.md)|  | 

### Return type

[**ResultRequest**](ResultRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**204** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_add_invited_user**
> ResultRequest v1_add_invited_user(invite_user_schema_add)

Users:Add Invited User

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import users_client
from users_client.models.invite_user_schema_add import InviteUserSchemaAdd
from users_client.models.result_request import ResultRequest
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: HTTPBearer
configuration = users_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with users_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_client.InvitedUserApi(api_client)
    invite_user_schema_add = users_client.InviteUserSchemaAdd() # InviteUserSchemaAdd | 

    try:
        # Users:Add Invited User
        api_response = api_instance.v1_add_invited_user(invite_user_schema_add)
        print("The response of InvitedUserApi->v1_add_invited_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitedUserApi->v1_add_invited_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_user_schema_add** | [**InviteUserSchemaAdd**](InviteUserSchemaAdd.md)|  | 

### Return type

[**ResultRequest**](ResultRequest.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**204** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_check_invited_user**
> ResultRequest v1_check_invited_user(user_id)

Users:Check Invited User

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import users_client
from users_client.models.result_request import ResultRequest
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: HTTPBearer
configuration = users_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with users_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_client.InvitedUserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Users:Check Invited User
        api_response = api_instance.v1_check_invited_user(user_id)
        print("The response of InvitedUserApi->v1_check_invited_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitedUserApi->v1_check_invited_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**ResultRequest**](ResultRequest.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**204** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_check_invited_user_by_integrator**
> ResultRequest v1_check_invited_user_by_integrator(user_id, integrator_id)

Users:Check Invited User By Integrator

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import users_client
from users_client.models.result_request import ResultRequest
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: HTTPBearer
configuration = users_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with users_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_client.InvitedUserApi(api_client)
    user_id = 'user_id_example' # str | 
    integrator_id = 'integrator_id_example' # str | 

    try:
        # Users:Check Invited User By Integrator
        api_response = api_instance.v1_check_invited_user_by_integrator(user_id, integrator_id)
        print("The response of InvitedUserApi->v1_check_invited_user_by_integrator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitedUserApi->v1_check_invited_user_by_integrator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **integrator_id** | **str**|  | 

### Return type

[**ResultRequest**](ResultRequest.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**204** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_integrator**
> UserSchemaBase v1_get_integrator(user_id)

Users:Get Integrator

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import users_client
from users_client.models.user_schema_base import UserSchemaBase
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: HTTPBearer
configuration = users_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with users_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_client.InvitedUserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Users:Get Integrator
        api_response = api_instance.v1_get_integrator(user_id)
        print("The response of InvitedUserApi->v1_get_integrator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitedUserApi->v1_get_integrator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserSchemaBase**](UserSchemaBase.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**204** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_invited_users**
> PaginationRequestUserSchemaBase v1_get_invited_users(integrator_id, page=page, size=size)

Users:Get Invited Users

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import users_client
from users_client.models.pagination_request_user_schema_base import PaginationRequestUserSchemaBase
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: HTTPBearer
configuration = users_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with users_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_client.InvitedUserApi(api_client)
    integrator_id = 'integrator_id_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    size = 25 # int |  (optional) (default to 25)

    try:
        # Users:Get Invited Users
        api_response = api_instance.v1_get_invited_users(integrator_id, page=page, size=size)
        print("The response of InvitedUserApi->v1_get_invited_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitedUserApi->v1_get_invited_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integrator_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 25]

### Return type

[**PaginationRequestUserSchemaBase**](PaginationRequestUserSchemaBase.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**204** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

