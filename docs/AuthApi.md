# users_client.AuthApi

All URIs are relative to */user_service/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_access_tokens_db_login_v1_auth_login_post**](AuthApi.md#auth_access_tokens_db_login_v1_auth_login_post) | **POST** /v1/auth/login | Auth:Access-Tokens-Db.Login
[**auth_access_tokens_db_logout_v1_auth_logout_post**](AuthApi.md#auth_access_tokens_db_logout_v1_auth_logout_post) | **POST** /v1/auth/logout | Auth:Access-Tokens-Db.Logout


# **auth_access_tokens_db_login_v1_auth_login_post**
> BearerResponse auth_access_tokens_db_login_v1_auth_login_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)

Auth:Access-Tokens-Db.Login

### Example

* Bearer Authentication (HTTPBearer):

```python
import users_client
from users_client.models.bearer_response import BearerResponse
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
        # Auth:Access-Tokens-Db.Login
        api_response = api_instance.auth_access_tokens_db_login_v1_auth_login_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        print("The response of AuthApi->auth_access_tokens_db_login_v1_auth_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_access_tokens_db_login_v1_auth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **password** | **str**|  | 
 **grant_type** | **str**|  | [optional] 
 **scope** | **str**|  | [optional] [default to &#39;&#39;]
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**BearerResponse**](BearerResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_access_tokens_db_logout_v1_auth_logout_post**
> object auth_access_tokens_db_logout_v1_auth_logout_post()

Auth:Access-Tokens-Db.Logout

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: HTTPBearer
configuration = users_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with users_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_client.AuthApi(api_client)

    try:
        # Auth:Access-Tokens-Db.Logout
        api_response = api_instance.auth_access_tokens_db_logout_v1_auth_logout_post()
        print("The response of AuthApi->auth_access_tokens_db_logout_v1_auth_logout_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_access_tokens_db_logout_v1_auth_logout_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

