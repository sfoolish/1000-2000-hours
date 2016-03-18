## TSP API 设计

### API 版本 

GET `/version` Get API version

### projects 增/删/改/查

GET `/projects` List test projects
```js
{
    "projects": [
        { project info details }，
        { ... }，
    ]
}
```

POST `/projects` Create a test project
```js
{
    "project": { project info details }
}
```

GET `/projects/detail` List details for all test projects (optional)

GET `/projects/{project_name e.g. yardstick}` Show details for a test project
```js
{
    "project": { project info details }
}
```

PUT `/projects/{project_name e.g. yardstick}` Update the editable attributes of a test project
```js
{
    "project": { "description": "new description" }
}
```

DELETE `/projects/{project_name e.g. yardstick}` Deletes a test project

**project info details**
```js
{
    "id": "",
    "name": "",
    "creation_date": "YYYY-MM-DD HH:MM:SS",
    "description":""
}
```

### test case 增/删/改/查/执行

GET `/projects/yardstick/cases` List test cases
```js
{
    "cases": [
        { case info details }，
        { ... }，
    ]
}
```
POST `/projects/yardstick/cases` Create a test case
```js
{
    "case": { case info details }
}
```

GET `/projects/yardstick/cases/detail` List details for all test cases (optional)

GET `/projects/yardstick/cases/{case_name or case_id}` Show details for a test case
```js
{
    "case": { case info details }
}
```

PUT `/projects/yardstick/cases/{case_name or case_id}` Update the editable attributes of a test case
```js
{
    "case": { "description": "new description" }
}
```

DELETE `/projects/yardstick/cases/{case_name or case_id}` Deletes a test case

** 多个用例同时执行的时候怎么办？ 每一次执行都有一个 id ，然后可以 id 查状态？ **

POST `/projects/yardstick/cases/{case_name or case_id}/action` execute a test case
```js
{
    "execute": null
}
```

POST `/projects/yardstick/cases/{case_name or case_id}/action` get execute status of a test case
```js
{
    "status": null
}
```

POST `/projects/yardstick/cases/action` execute several test cases(run as test suite)
```js
{
    "execute": {
        "cases": ["case_name", "..."],
        "environment": "environment_id"
    }
}
```

POST `/projects/yardstick/cases/action` get execute status of several test cases
```js
{
    "status": null
}
```

**case info details**
```js
{
    "name": "ping",
    "installer": "compass_",
    "scenario": "ODL_L2",
    "description": "",
    "creation_date": "YYYY-MM-DD HH:MM:SS",
    "checked": False
}
```
### NFVI 环境 增/删/改/查

GET `/environments` List cloud environments
```js
{
    "environments": [
        { environment info details }，
        { ... }，
    ]
}
```

POST `/environments` Create cloud environment
```js
{
    "environment": { environment info details }
}
```

GET `/environments/detail` List details for all cloud environments (optional)

GET `/environments/{environment_id}` Show details for a cloud environment
```js
{
    "environment": { environment info details }
}
```

PUT `/environments/{environment_id}` Update the editable attributes of a cloud environment
```
{
    "environment": { "description": "new description" }
}
```

DELETE `/environments/{environment_id}` Deletes a cloud environment

**environment info details**
```js
{
    "installer": "",
    "pod_name": "",
    "creation_date": "YYYY-MM-DD HH:MM:SS",
    "description": "",
    "env": {
        "OS_PASSWORD": "console",
        "OS_TENANT_NAME": "admin",
        "OS_AUTH_URL": "http://172.17.1.222:35357/v2.0",
        "OS_USERNAME": "admin",
        "OS_PASSWORD": "console",
        "EXTERNAL_NETWORK": "ext-net"
        "OS_VOLUME_API_VERSION": "2",
    }
}
```

### Test results

**TBD**
```js
{
    "_id": "",
    "project_name": "",
    "pod_name": "",
    "version": "",
    "installer": "",
    "description": "",
    "creation_date": "YYYY-MM-DD HH:MM:SS",
    "case_name": ""
    "details":{
       <- the results to be put here ->
    }
}
```

### 实时的log

**TBD**

## REF

* http://developer.openstack.org/api-ref-compute-v2.1.html
* http://docs.getcloudify.org/api/
* http://getcloudify.org/guide/2.7/restapi/restdoclet.html
* https://wiki.opnfv.org/collection_of_test_results
* http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
* http://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
