# users_client.PermissionApi

All URIs are relative to */user_service/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_permission_permissions_post**](PermissionApi.md#create_permission_permissions_post) | **POST** /permissions/ | Create Permission
[**delete_permission_permissions_permission_id_delete**](PermissionApi.md#delete_permission_permissions_permission_id_delete) | **DELETE** /permissions/{permission_id} | Delete Permission
[**get_permission_by_id_permissions_permission_id_get**](PermissionApi.md#get_permission_by_id_permissions_permission_id_get) | **GET** /permissions/{permission_id} | Get Permission By Id
[**get_permissions_permissions_get**](PermissionApi.md#get_permissions_permissions_get) | **GET** /permissions/ | Get Permissions


# **create_permission_permissions_post**
> PermissionSchema create_permission_permissions_post(permission_schema_add)

Create Permission

Create a new permission.  This endpoint allows for the creation of a new permission.

### Example


```python
import users_client
from users_client.models.permission_schema import PermissionSchema
from users_client.models.permission_schema_add import PermissionSchemaAdd
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
    api_instance = users_client.PermissionApi(api_client)
    permission_schema_add = users_client.PermissionSchemaAdd() # PermissionSchemaAdd | 

    try:
        # Create Permission
        api_response = api_instance.create_permission_permissions_post(permission_schema_add)
        print("The response of PermissionApi->create_permission_permissions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->create_permission_permissions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_schema_add** | [**PermissionSchemaAdd**](PermissionSchemaAdd.md)|  | 

### Return type

[**PermissionSchema**](PermissionSchema.md)

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

# **delete_permission_permissions_permission_id_delete**
> PermissionSchema delete_permission_permissions_permission_id_delete(permission_id)

Delete Permission

Delete a permission by ID.  This endpoint deletes a permission by its unique ID.

### Example


```python
import users_client
from users_client.models.permission_schema import PermissionSchema
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
    api_instance = users_client.PermissionApi(api_client)
    permission_id = 56 # int | 

    try:
        # Delete Permission
        api_response = api_instance.delete_permission_permissions_permission_id_delete(permission_id)
        print("The response of PermissionApi->delete_permission_permissions_permission_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->delete_permission_permissions_permission_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_id** | **int**|  | 

### Return type

[**PermissionSchema**](PermissionSchema.md)

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permission_by_id_permissions_permission_id_get**
> PermissionSchema get_permission_by_id_permissions_permission_id_get(permission_id)

Get Permission By Id

Retrieve a permission by ID.  This endpoint retrieves a permission by its unique ID.

### Example


```python
import users_client
from users_client.models.permission_schema import PermissionSchema
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
    api_instance = users_client.PermissionApi(api_client)
    permission_id = 56 # int | 

    try:
        # Get Permission By Id
        api_response = api_instance.get_permission_by_id_permissions_permission_id_get(permission_id)
        print("The response of PermissionApi->get_permission_by_id_permissions_permission_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->get_permission_by_id_permissions_permission_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_id** | **int**|  | 

### Return type

[**PermissionSchema**](PermissionSchema.md)

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

# **get_permissions_permissions_get**
> PaginationRequestPermissionSchema get_permissions_permissions_get(page=page, size=size, is_delete__in=is_delete__in, name=name, name__in=name__in, id=id, id__in=id__in, id__neq=id__neq)

Get Permissions

Get a paginated list of permissions.  This endpoint retrieves a paginated list of permissions based on provided filters.

### Example


```python
import users_client
from users_client.models.pagination_request_permission_schema import PaginationRequestPermissionSchema
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
    api_instance = users_client.PermissionApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    size = 25 # int |  (optional) (default to 25)
    is_delete__in = 'is_delete__in_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    name__in = 'name__in_example' # str |  (optional)
    id = 56 # int |  (optional)
    id__in = 'id__in_example' # str |  (optional)
    id__neq = 'id__neq_example' # str |  (optional)

    try:
        # Get Permissions
        api_response = api_instance.get_permissions_permissions_get(page=page, size=size, is_delete__in=is_delete__in, name=name, name__in=name__in, id=id, id__in=id__in, id__neq=id__neq)
        print("The response of PermissionApi->get_permissions_permissions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->get_permissions_permissions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 25]
 **is_delete__in** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **name__in** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **id__in** | **str**|  | [optional] 
 **id__neq** | **str**|  | [optional] 

### Return type

[**PaginationRequestPermissionSchema**](PaginationRequestPermissionSchema.md)

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

