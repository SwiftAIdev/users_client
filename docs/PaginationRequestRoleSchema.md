# PaginationRequestRoleSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**size** | **int** |  | 
**total** | **int** |  | 
**data** | [**List[RoleSchema]**](RoleSchema.md) |  | 

## Example

```python
from users_client.models.pagination_request_role_schema import PaginationRequestRoleSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationRequestRoleSchema from a JSON string
pagination_request_role_schema_instance = PaginationRequestRoleSchema.from_json(json)
# print the JSON string representation of the object
print(PaginationRequestRoleSchema.to_json())

# convert the object into a dict
pagination_request_role_schema_dict = pagination_request_role_schema_instance.to_dict()
# create an instance of PaginationRequestRoleSchema from a dict
pagination_request_role_schema_from_dict = PaginationRequestRoleSchema.from_dict(pagination_request_role_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


