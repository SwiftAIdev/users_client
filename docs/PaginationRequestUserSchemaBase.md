# PaginationRequestUserSchemaBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**size** | **int** |  | 
**total** | **int** |  | 
**data** | [**List[UserSchemaBase]**](UserSchemaBase.md) |  | 

## Example

```python
from users_client.models.pagination_request_user_schema_base import PaginationRequestUserSchemaBase

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationRequestUserSchemaBase from a JSON string
pagination_request_user_schema_base_instance = PaginationRequestUserSchemaBase.from_json(json)
# print the JSON string representation of the object
print(PaginationRequestUserSchemaBase.to_json())

# convert the object into a dict
pagination_request_user_schema_base_dict = pagination_request_user_schema_base_instance.to_dict()
# create an instance of PaginationRequestUserSchemaBase from a dict
pagination_request_user_schema_base_from_dict = PaginationRequestUserSchemaBase.from_dict(pagination_request_user_schema_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


