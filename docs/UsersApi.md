# users_client.UsersApi

All URIs are relative to */user_service/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_user_email_users_user_id_change_email_post**](UsersApi.md#change_user_email_users_user_id_change_email_post) | **POST** /users/{user_id}/change_email | Change User Email
[**change_user_password_users_user_id_change_password_post**](UsersApi.md#change_user_password_users_user_id_change_password_post) | **POST** /users/{user_id}/change_password | Change User Password
[**create_user_users_post**](UsersApi.md#create_user_users_post) | **POST** /users | Create User
[**get_user_by_id_users_user_id_get**](UsersApi.md#get_user_by_id_users_user_id_get) | **GET** /users/{user_id} | Get User By Id
[**get_users_users_get**](UsersApi.md#get_users_users_get) | **GET** /users/ | Get Users
[**login_user_users_login_post**](UsersApi.md#login_user_users_login_post) | **POST** /users/login | Login User
[**register_user_users_user_id_register_post**](UsersApi.md#register_user_users_user_id_register_post) | **POST** /users/{user_id}/register | Register User
[**update_user_users_user_id_put**](UsersApi.md#update_user_users_user_id_put) | **PUT** /users/{user_id} | Update User


# **change_user_email_users_user_id_change_email_post**
> UserSchemaBase change_user_email_users_user_id_change_email_post(user_id, user_schema_change_email)

Change User Email

Change a user's email by ID.  This endpoint allows changing the email of an existing user.

### Example


```python
import users_client
from users_client.models.user_schema_base import UserSchemaBase
from users_client.models.user_schema_change_email import UserSchemaChangeEmail
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
    api_instance = users_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    user_schema_change_email = users_client.UserSchemaChangeEmail() # UserSchemaChangeEmail | 

    try:
        # Change User Email
        api_response = api_instance.change_user_email_users_user_id_change_email_post(user_id, user_schema_change_email)
        print("The response of UsersApi->change_user_email_users_user_id_change_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->change_user_email_users_user_id_change_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_schema_change_email** | [**UserSchemaChangeEmail**](UserSchemaChangeEmail.md)|  | 

### Return type

[**UserSchemaBase**](UserSchemaBase.md)

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_password_users_user_id_change_password_post**
> UserSchemaBase change_user_password_users_user_id_change_password_post(user_id, user_schema_change_password)

Change User Password

Change a user's password by ID.  This endpoint allows changing the password of an existing user.

### Example


```python
import users_client
from users_client.models.user_schema_base import UserSchemaBase
from users_client.models.user_schema_change_password import UserSchemaChangePassword
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
    api_instance = users_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    user_schema_change_password = users_client.UserSchemaChangePassword() # UserSchemaChangePassword | 

    try:
        # Change User Password
        api_response = api_instance.change_user_password_users_user_id_change_password_post(user_id, user_schema_change_password)
        print("The response of UsersApi->change_user_password_users_user_id_change_password_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->change_user_password_users_user_id_change_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_schema_change_password** | [**UserSchemaChangePassword**](UserSchemaChangePassword.md)|  | 

### Return type

[**UserSchemaBase**](UserSchemaBase.md)

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_users_post**
> UserSchemaBase create_user_users_post(user_schema_add)

Create User

Create a new user.  This endpoint allows for the creation of a new user.

### Example


```python
import users_client
from users_client.models.user_schema_add import UserSchemaAdd
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
    api_instance = users_client.UsersApi(api_client)
    user_schema_add = users_client.UserSchemaAdd() # UserSchemaAdd | 

    try:
        # Create User
        api_response = api_instance.create_user_users_post(user_schema_add)
        print("The response of UsersApi->create_user_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_schema_add** | [**UserSchemaAdd**](UserSchemaAdd.md)|  | 

### Return type

[**UserSchemaBase**](UserSchemaBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id_users_user_id_get**
> UserSchemaBase get_user_by_id_users_user_id_get(user_id)

Get User By Id

Retrieve a user by ID.  This endpoint retrieves a user by their unique ID.

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
    api_instance = users_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get User By Id
        api_response = api_instance.get_user_by_id_users_user_id_get(user_id)
        print("The response of UsersApi->get_user_by_id_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_by_id_users_user_id_get: %s\n" % e)
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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_users_get**
> PaginationRequestUserSchemaBase get_users_users_get(page=page, size=size, surname=surname, name=name, email=email, email__not=email__not, third_party_id=third_party_id, invite_code=invite_code, id=id, id__in=id__in, id__neq=id__neq, is_active=is_active)

Get Users

Get a paginated list of users.  This endpoint retrieves a paginated list of users based on provided filters.

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
    api_instance = users_client.UsersApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    size = 25 # int |  (optional) (default to 25)
    surname = 'surname_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    email = 'email_example' # str |  (optional)
    email__not = 'email__not_example' # str |  (optional)
    third_party_id = 'third_party_id_example' # str |  (optional)
    invite_code = 'invite_code_example' # str |  (optional)
    id = 56 # int |  (optional)
    id__in = 'id__in_example' # str |  (optional)
    id__neq = 56 # int |  (optional)
    is_active = True # bool |  (optional)

    try:
        # Get Users
        api_response = api_instance.get_users_users_get(page=page, size=size, surname=surname, name=name, email=email, email__not=email__not, third_party_id=third_party_id, invite_code=invite_code, id=id, id__in=id__in, id__neq=id__neq, is_active=is_active)
        print("The response of UsersApi->get_users_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_users_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 25]
 **surname** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **email** | **str**|  | [optional] 
 **email__not** | **str**|  | [optional] 
 **third_party_id** | **str**|  | [optional] 
 **invite_code** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **id__in** | **str**|  | [optional] 
 **id__neq** | **int**|  | [optional] 
 **is_active** | **bool**|  | [optional] 

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_user_users_login_post**
> UserSchemaBase login_user_users_login_post(user_schema_login)

Login User

Log in a user.  This endpoint allows a user to log in with the provided credentials.

### Example


```python
import users_client
from users_client.models.user_schema_base import UserSchemaBase
from users_client.models.user_schema_login import UserSchemaLogin
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
    api_instance = users_client.UsersApi(api_client)
    user_schema_login = users_client.UserSchemaLogin() # UserSchemaLogin | 

    try:
        # Login User
        api_response = api_instance.login_user_users_login_post(user_schema_login)
        print("The response of UsersApi->login_user_users_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->login_user_users_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_schema_login** | [**UserSchemaLogin**](UserSchemaLogin.md)|  | 

### Return type

[**UserSchemaBase**](UserSchemaBase.md)

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user_users_user_id_register_post**
> UserSchemaBase register_user_users_user_id_register_post(user_id, user_schema_register)

Register User

Register a user.  This endpoint registers a new user with the provided information.

### Example


```python
import users_client
from users_client.models.user_schema_base import UserSchemaBase
from users_client.models.user_schema_register import UserSchemaRegister
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
    api_instance = users_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    user_schema_register = users_client.UserSchemaRegister() # UserSchemaRegister | 

    try:
        # Register User
        api_response = api_instance.register_user_users_user_id_register_post(user_id, user_schema_register)
        print("The response of UsersApi->register_user_users_user_id_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->register_user_users_user_id_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_schema_register** | [**UserSchemaRegister**](UserSchemaRegister.md)|  | 

### Return type

[**UserSchemaBase**](UserSchemaBase.md)

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_users_user_id_put**
> UserSchemaBase update_user_users_user_id_put(user_id, user_schema_update)

Update User

Update a user by ID.  This endpoint updates the details of an existing user.

### Example


```python
import users_client
from users_client.models.user_schema_base import UserSchemaBase
from users_client.models.user_schema_update import UserSchemaUpdate
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
    api_instance = users_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    user_schema_update = users_client.UserSchemaUpdate() # UserSchemaUpdate | 

    try:
        # Update User
        api_response = api_instance.update_user_users_user_id_put(user_id, user_schema_update)
        print("The response of UsersApi->update_user_users_user_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user_users_user_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_schema_update** | [**UserSchemaUpdate**](UserSchemaUpdate.md)|  | 

### Return type

[**UserSchemaBase**](UserSchemaBase.md)

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

