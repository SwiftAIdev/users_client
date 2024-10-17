# users_client.RolesApi

All URIs are relative to */user_service/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_permission_to_role_roles_role_id_permissions_permission_id_post**](RolesApi.md#add_permission_to_role_roles_role_id_permissions_permission_id_post) | **POST** /roles/{role_id}/permissions/{permission_id} | Add Permission To Role
[**add_permissions_to_role_roles_role_id_permissions_post**](RolesApi.md#add_permissions_to_role_roles_role_id_permissions_post) | **POST** /roles/{role_id}/permissions | Add Permissions To Role
[**create_role_roles_post**](RolesApi.md#create_role_roles_post) | **POST** /roles/ | Create Role
[**delete_role_roles_role_id_delete**](RolesApi.md#delete_role_roles_role_id_delete) | **DELETE** /roles/{role_id} | Delete Role
[**get_role_by_id_roles_role_id_get**](RolesApi.md#get_role_by_id_roles_role_id_get) | **GET** /roles/{role_id} | Get Role By Id
[**get_roles_roles_get**](RolesApi.md#get_roles_roles_get) | **GET** /roles/ | Get Roles
[**remove_permission_to_role_roles_role_id_permissions_permission_id_delete**](RolesApi.md#remove_permission_to_role_roles_role_id_permissions_permission_id_delete) | **DELETE** /roles/{role_id}/permissions/{permission_id} | Remove Permission To Role
[**v1_add_permission_by_role**](RolesApi.md#v1_add_permission_by_role) | **POST** /v1/roles/{role_id}/permissions/{permission_id} | Roles:Add Permission By Role
[**v1_add_permissions_by_role**](RolesApi.md#v1_add_permissions_by_role) | **POST** /v1/roles/{role_id}/permissions | Roles:Add Permissions By Role
[**v1_create_role**](RolesApi.md#v1_create_role) | **POST** /v1/roles | Roles:Create Role
[**v1_get_role_by_id**](RolesApi.md#v1_get_role_by_id) | **GET** /v1/roles/{role_id} | Roles:Get Role By Id
[**v1_get_roles**](RolesApi.md#v1_get_roles) | **GET** /v1/roles | Roles:Get Roles
[**v1_remove_permission_by_role**](RolesApi.md#v1_remove_permission_by_role) | **DELETE** /v1/roles/{role_id}/permissions/{permission_id} | Roles:Remove Permission By Role
[**v1_remove_role**](RolesApi.md#v1_remove_role) | **DELETE** /v1/roles/{role_id} | Roles:Remove Role


# **add_permission_to_role_roles_role_id_permissions_permission_id_post**
> RoleSchema add_permission_to_role_roles_role_id_permissions_permission_id_post(role_id, permission_id)

Add Permission To Role

Add a permission to a role by ID.  This endpoint allows adding a permission to an existing role.

### Example


```python
import users_client
from users_client.models.role_schema import RoleSchema
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
    api_instance = users_client.RolesApi(api_client)
    role_id = 56 # int | 
    permission_id = 56 # int | 

    try:
        # Add Permission To Role
        api_response = api_instance.add_permission_to_role_roles_role_id_permissions_permission_id_post(role_id, permission_id)
        print("The response of RolesApi->add_permission_to_role_roles_role_id_permissions_permission_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->add_permission_to_role_roles_role_id_permissions_permission_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**|  | 
 **permission_id** | **int**|  | 

### Return type

[**RoleSchema**](RoleSchema.md)

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

# **add_permissions_to_role_roles_role_id_permissions_post**
> RoleSchema add_permissions_to_role_roles_role_id_permissions_post(role_id, role_schema_add_permission)

Add Permissions To Role

Add a permission to a role by ID.  This endpoint allows adding a permission to an existing role.

### Example


```python
import users_client
from users_client.models.role_schema import RoleSchema
from users_client.models.role_schema_add_permission import RoleSchemaAddPermission
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
    api_instance = users_client.RolesApi(api_client)
    role_id = 56 # int | 
    role_schema_add_permission = users_client.RoleSchemaAddPermission() # RoleSchemaAddPermission | 

    try:
        # Add Permissions To Role
        api_response = api_instance.add_permissions_to_role_roles_role_id_permissions_post(role_id, role_schema_add_permission)
        print("The response of RolesApi->add_permissions_to_role_roles_role_id_permissions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->add_permissions_to_role_roles_role_id_permissions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**|  | 
 **role_schema_add_permission** | [**RoleSchemaAddPermission**](RoleSchemaAddPermission.md)|  | 

### Return type

[**RoleSchema**](RoleSchema.md)

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

# **create_role_roles_post**
> RoleSchema create_role_roles_post(role_schema_add)

Create Role

Create a new role.  This endpoint allows for the creation of a new role.

### Example


```python
import users_client
from users_client.models.role_schema import RoleSchema
from users_client.models.role_schema_add import RoleSchemaAdd
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
    api_instance = users_client.RolesApi(api_client)
    role_schema_add = users_client.RoleSchemaAdd() # RoleSchemaAdd | 

    try:
        # Create Role
        api_response = api_instance.create_role_roles_post(role_schema_add)
        print("The response of RolesApi->create_role_roles_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->create_role_roles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_schema_add** | [**RoleSchemaAdd**](RoleSchemaAdd.md)|  | 

### Return type

[**RoleSchema**](RoleSchema.md)

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
**204** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_roles_role_id_delete**
> RoleSchema delete_role_roles_role_id_delete(role_id)

Delete Role

Delete a role by ID.  This endpoint deletes a role by its unique ID.

### Example


```python
import users_client
from users_client.models.role_schema import RoleSchema
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
    api_instance = users_client.RolesApi(api_client)
    role_id = 56 # int | 

    try:
        # Delete Role
        api_response = api_instance.delete_role_roles_role_id_delete(role_id)
        print("The response of RolesApi->delete_role_roles_role_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->delete_role_roles_role_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**|  | 

### Return type

[**RoleSchema**](RoleSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**204** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_by_id_roles_role_id_get**
> RoleSchema get_role_by_id_roles_role_id_get(role_id)

Get Role By Id

Retrieve a role by ID.  This endpoint retrieves a role by its unique ID.

### Example


```python
import users_client
from users_client.models.role_schema import RoleSchema
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
    api_instance = users_client.RolesApi(api_client)
    role_id = 56 # int | 

    try:
        # Get Role By Id
        api_response = api_instance.get_role_by_id_roles_role_id_get(role_id)
        print("The response of RolesApi->get_role_by_id_roles_role_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_role_by_id_roles_role_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**|  | 

### Return type

[**RoleSchema**](RoleSchema.md)

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

# **get_roles_roles_get**
> PaginationRequestRoleSchema get_roles_roles_get(page=page, size=size, is_delete=is_delete, is_delete__in=is_delete__in, name=name, id=id, id__in=id__in, id__neq=id__neq)

Get Roles

Get a paginated list of roles.  This endpoint retrieves a paginated list of roles based on provided filters.

### Example


```python
import users_client
from users_client.models.pagination_request_role_schema import PaginationRequestRoleSchema
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
    api_instance = users_client.RolesApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    size = 25 # int |  (optional) (default to 25)
    is_delete = True # bool |  (optional)
    is_delete__in = 'is_delete__in_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    id = 56 # int |  (optional)
    id__in = 'id__in_example' # str |  (optional)
    id__neq = 'id__neq_example' # str |  (optional)

    try:
        # Get Roles
        api_response = api_instance.get_roles_roles_get(page=page, size=size, is_delete=is_delete, is_delete__in=is_delete__in, name=name, id=id, id__in=id__in, id__neq=id__neq)
        print("The response of RolesApi->get_roles_roles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_roles_roles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 25]
 **is_delete** | **bool**|  | [optional] 
 **is_delete__in** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **id__in** | **str**|  | [optional] 
 **id__neq** | **str**|  | [optional] 

### Return type

[**PaginationRequestRoleSchema**](PaginationRequestRoleSchema.md)

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

# **remove_permission_to_role_roles_role_id_permissions_permission_id_delete**
> RoleSchema remove_permission_to_role_roles_role_id_permissions_permission_id_delete(role_id, permission_id)

Remove Permission To Role

Remove a permission to a role by ID.  This endpoint allows adding a permission to an existing role.

### Example


```python
import users_client
from users_client.models.role_schema import RoleSchema
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
    api_instance = users_client.RolesApi(api_client)
    role_id = 56 # int | 
    permission_id = 56 # int | 

    try:
        # Remove Permission To Role
        api_response = api_instance.remove_permission_to_role_roles_role_id_permissions_permission_id_delete(role_id, permission_id)
        print("The response of RolesApi->remove_permission_to_role_roles_role_id_permissions_permission_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->remove_permission_to_role_roles_role_id_permissions_permission_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**|  | 
 **permission_id** | **int**|  | 

### Return type

[**RoleSchema**](RoleSchema.md)

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

# **v1_add_permission_by_role**
> RoleSchema v1_add_permission_by_role(role_id, permission_id)

Roles:Add Permission By Role

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import users_client
from users_client.models.role_schema import RoleSchema
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
    api_instance = users_client.RolesApi(api_client)
    role_id = 56 # int | 
    permission_id = 56 # int | 

    try:
        # Roles:Add Permission By Role
        api_response = api_instance.v1_add_permission_by_role(role_id, permission_id)
        print("The response of RolesApi->v1_add_permission_by_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->v1_add_permission_by_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**|  | 
 **permission_id** | **int**|  | 

### Return type

[**RoleSchema**](RoleSchema.md)

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

# **v1_add_permissions_by_role**
> RoleSchema v1_add_permissions_by_role(role_id, role_schema_add_permission)

Roles:Add Permissions By Role

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import users_client
from users_client.models.role_schema import RoleSchema
from users_client.models.role_schema_add_permission import RoleSchemaAddPermission
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
    api_instance = users_client.RolesApi(api_client)
    role_id = 56 # int | 
    role_schema_add_permission = users_client.RoleSchemaAddPermission() # RoleSchemaAddPermission | 

    try:
        # Roles:Add Permissions By Role
        api_response = api_instance.v1_add_permissions_by_role(role_id, role_schema_add_permission)
        print("The response of RolesApi->v1_add_permissions_by_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->v1_add_permissions_by_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**|  | 
 **role_schema_add_permission** | [**RoleSchemaAddPermission**](RoleSchemaAddPermission.md)|  | 

### Return type

[**RoleSchema**](RoleSchema.md)

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

# **v1_create_role**
> RoleSchema v1_create_role(role_schema_add)

Roles:Create Role

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import users_client
from users_client.models.role_schema import RoleSchema
from users_client.models.role_schema_add import RoleSchemaAdd
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
    api_instance = users_client.RolesApi(api_client)
    role_schema_add = users_client.RoleSchemaAdd() # RoleSchemaAdd | 

    try:
        # Roles:Create Role
        api_response = api_instance.v1_create_role(role_schema_add)
        print("The response of RolesApi->v1_create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->v1_create_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_schema_add** | [**RoleSchemaAdd**](RoleSchemaAdd.md)|  | 

### Return type

[**RoleSchema**](RoleSchema.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

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
**204** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_role_by_id**
> RoleSchema v1_get_role_by_id(role_id)

Roles:Get Role By Id

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import users_client
from users_client.models.role_schema import RoleSchema
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
    api_instance = users_client.RolesApi(api_client)
    role_id = 56 # int | 

    try:
        # Roles:Get Role By Id
        api_response = api_instance.v1_get_role_by_id(role_id)
        print("The response of RolesApi->v1_get_role_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->v1_get_role_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**|  | 

### Return type

[**RoleSchema**](RoleSchema.md)

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

# **v1_get_roles**
> PaginationRequestRoleSchema v1_get_roles(page=page, size=size, is_delete=is_delete, is_delete__in=is_delete__in, name=name, id=id, id__in=id__in, id__neq=id__neq)

Roles:Get Roles

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import users_client
from users_client.models.pagination_request_role_schema import PaginationRequestRoleSchema
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
    api_instance = users_client.RolesApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    size = 25 # int |  (optional) (default to 25)
    is_delete = True # bool |  (optional)
    is_delete__in = 'is_delete__in_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    id = 56 # int |  (optional)
    id__in = 'id__in_example' # str |  (optional)
    id__neq = 'id__neq_example' # str |  (optional)

    try:
        # Roles:Get Roles
        api_response = api_instance.v1_get_roles(page=page, size=size, is_delete=is_delete, is_delete__in=is_delete__in, name=name, id=id, id__in=id__in, id__neq=id__neq)
        print("The response of RolesApi->v1_get_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->v1_get_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 25]
 **is_delete** | **bool**|  | [optional] 
 **is_delete__in** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **id__in** | **str**|  | [optional] 
 **id__neq** | **str**|  | [optional] 

### Return type

[**PaginationRequestRoleSchema**](PaginationRequestRoleSchema.md)

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

# **v1_remove_permission_by_role**
> RoleSchema v1_remove_permission_by_role(role_id, permission_id)

Roles:Remove Permission By Role

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import users_client
from users_client.models.role_schema import RoleSchema
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
    api_instance = users_client.RolesApi(api_client)
    role_id = 56 # int | 
    permission_id = 56 # int | 

    try:
        # Roles:Remove Permission By Role
        api_response = api_instance.v1_remove_permission_by_role(role_id, permission_id)
        print("The response of RolesApi->v1_remove_permission_by_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->v1_remove_permission_by_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**|  | 
 **permission_id** | **int**|  | 

### Return type

[**RoleSchema**](RoleSchema.md)

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

# **v1_remove_role**
> bool v1_remove_role(role_id)

Roles:Remove Role

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
    api_instance = users_client.RolesApi(api_client)
    role_id = 56 # int | 

    try:
        # Roles:Remove Role
        api_response = api_instance.v1_remove_role(role_id)
        print("The response of RolesApi->v1_remove_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->v1_remove_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**|  | 

### Return type

**bool**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**204** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

