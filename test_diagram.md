# Testing for superuser

The superuser package contains three services with the following public procedures:

- **Organization**
  - ```get```
- **SignUpApproval**
  - ```setPermission```
- **User**
  - ```authorize```
  - ```get```
  - ```getNewUsers```

## Organization service
### ```com.tygasmart.superuser.Organization.get```
#### Conditions:
- C1: 
#### Expected outputs:
- E1:

## SignUpApproval service

### ```com.tygasmart.superuser.SignUpApproval.setPermission```
#### Conditions:
- C1: 
#### Expected outputs:
- E1:

## User service

### ```com.tygasmart.superuser.User.authorize```
#### Conditions:
- C1: 
#### Expected outputs:
- E1:

### ```com.tygasmart.superuser.User.get```

#### Successful return 
```json
{
  "status": {
    "code": 0,
    "title": "SUCCESS",
    "message": "Process is valid"
  },
  "data": [
    {
      "clientRequested": Boolean,
      "moverRequested": Boolean,
      "isApproved": Boolean,
      ("approvalDate": DateTime),
      "isRejected": Boolean,
      ("rejectionDate": DateTime),
      "isPending": Boolean,
      "isEmailVerified": Boolean,
      "submitDate": DateTime,
      "organizationId": String,
      "userId": String,
      "email": String,
      "firstName": String,
      "lastName": String,
      "imageUrl": String,
    }
  ]
}
```

#### Conditions:
- C1: The request is made by a _superuser_ user.
- C2: The procedure receives any of _```userId```_, _```email```_, _```client```_, _```mover```_, _```approved```_, _```rejected```_, _```pending```_ or a combination of any of them as parameters.
- C3: The procedure receives a _```limit```_ and a _```page```_ as parameters.
  
#### Expected outputs:
- E1: A list of all new requests with user information from the **_AdminRequest_** and **_User_** types.
- E2: A filtered list of requests with user information from the **_AdminRequest_** and **_User_** types.
- E3: A list of all new users limited to _```limit```_ number of records from the _```page```_ page of the **_AdminRequest_** type with a pending status.
- E4: A filtered list of new users limited to _```limit```_ number of records from the _```page```_ page of the **_AdminRequest_** type with a pending status.
- E5: An ```Unauthorized Request``` exception.

```mermaid
---
title: Expected behavior of com.tygasmart.superuser.User.get
---
flowchart TB
  C1((C1)); C2((C2)); C3((C3))
  E1((E1)); E2((E2)); E3((E3)); E4((E4)); E5((E5))

  C1-->E1
  linkStyle 0 stroke: blue
  C1 & C2-->E2
  linkStyle 1,2 stroke: green
  C1 & C3-->E3
  linkStyle 3,4 stroke: yellow
  C1 & C2 & C3-->E4
  linkStyle 5,6,7 stroke: red
  C2 & C3-.->E5
  style E5 stroke:red
  linkStyle 8,9 stroke: orange
```


### ```com.tygasmart.superuser.User.getNewUser```
#### Successful return

```json
{
  "status": {
    "code": 0,
    "title": "SUCCESS",
    "message": "Process is valid"
  },
  "data": [
    {
      "clientRequested": Boolean,
      "moverRequested": Boolean,
      "isPending": Boolean,
      "isEmailVerified": Boolean,
      "submitDate": DateTime,
      "organizationId": String,
      "userId": String,
      "email": String,
      "firstName": String,
      "lastName": String
    }
  ]
}
```

#### Conditions: 
- C1: The request is made by a _superuser_ user.
- C2: The procedure receives any of _```userId```_, _```email```_ or both as parameters.
- C3: The procedure receives a _```limit```_ and a _```page```_ as paramters.

#### Expected outputs:
- E1: A list of all new requests with requester information from the **_AdminRequest_** and **_User_** types with a pending status.
- E2: A filtered list of new requests with requester information from the **_AdminRequest_** and **_User_** types with a pending status.
- E3: A list of all new requests with requester information limited to a _```limit```_ number of records of the _```page```_ page from the **_AdminRequest_** and **_User_** types with a pending status.
- E4: A filtered list of new requests with requester information limited to a _```limit```_ number of records of the _```page```_ page from the **_AdminRequest_** and **_User_** types with a pending status.
- E5: An ```Unauthorized_Request``` exception.

```mermaid
---
title:  Expected behavior of com.tygasmart.superuser.User.getNewUser
---
flowchart TB
  C1((C1)); C2((C2)); C3((C3))
  E1((E1)); E2((E2)); E3((E3)); E4((E4)); E5((E5))

  C1-->E1
  linkStyle 0 stroke: blue
  C1 & C2-->E2
  linkStyle 1,2 stroke: green
  C1 & C3-->E3
  linkStyle 3,4 stroke: yellow
  C1 & C2 & C3-->E4
  linkStyle 5,6,7 stroke: red
  C2 & C3-.->E5
  style E5 stroke:red
  linkStyle 8,9 stroke: orange
```