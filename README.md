# LDT-HACK-2020
THE LEADERS OF THE DIGITAL TRANSFORMATION HACKATON 2020

>imagine that this is the "wiki" tab

## Endpoints with examples

### /auth/users/set_password/
>Changes password

#### method: POST

response example:
```
{
    "new_password": "Alpine12",
    "re_new_password": "Alpine12"
    "current_password": "123",
}
```

### /api/lk
>Returns lk

#### method: GET

response example:
```
{
    "data": {
        "id": 6,
        "first_name": "",
        "middle_name": "",
        "last_name": "123",
        "email": "",
        "school": "",
        "date_of_birth": "2000-01-01"
    }
}
```

### /api/get_status
>Returns one of the three current user statuses

#### method: GET

response example:
```
"TEACHER"
```
or
```
"STUDENT"
```
or
```
"USER IS NOT IN THE GROUP"
```

### /api/my_classes
>Returns a list of classes available to the current user

#### method: GET

response example:
```
[
    {
        "id": 2,
        "name": "Class A"
    },
    {
        "id": 4,
        "name": "Class B"
    },
    {
        "id": 5,
        "name": "Class C"
    }
]
```

### /api/classes/<int:pk>/
>Returns current class with blocks and tasks

#### method: GET

response example:
```
{
    "id": 7,
    "name": "Класс 13",
    "sprints": [
        {
            "id": 9,
            "name": "Блок 13",
            "tasks": [
                {
                    "id": 20,
                    "name": "Задание 13",
                    "task_detail": [
                        {
                            "id": 16,
                            "is_done": true,
                            "last_code": "code"
                        }
                    ]
                },
                {
                    "id": 21,
                    "name": "Задание 14",
                    "task_detail": [
                        {
                            "id": 17,
                            "is_done": true,
                            "last_code": "code too"
                        }
                    ]
                }
            ]
        },
        {
            "id": 10,
            "name": "Блок 21",
            "tasks": []
        }
    ]
}
```


### /api/classes/<int:pk>/new_block
>Creates new block in the current class

#### method: POST

Args:
"name": "str"
"grade": "id" (take it from URL)

returns HTTP_201_CREATED or HTTP_400_BAD_REQUEST


### /api/blocks/<int:pk>/delete
>Deletes current block by it's id in the URL

#### method: DELETE

just send this request to URL, that contains block's id

returns 1 or HTTP_400_BAD_REQUEST


### /api/blocks/<int:pk>/change
>Changes current block

#### method: PUT

Args:
"name": str (optionaly)

returns HTTP_200_OK or HTTP_400_BAD_REQUEST


### /api/tasks/20
>Returns current task and it's details for current user

#### method: GET

response example:
```
{
    "id": 20,
    "name": "Example name",
    "theory": "Theory",
    "mission": "Practice",
    "task_detail": [
        {
            "id": 16,
            "is_done": true,
            "last_code": "a=1"
        }
    ],
    "languages": [
        "python"
    ]
}
```

### /api/blocks/<int:pk>/new_task
>Creates new task in current block

#### method: POST

Args:

"name": "ex name"

"theory": "ex theory"

"mission": "ex mission"

"sprint": "" (block id - tak it from URL)

"languages": "python3, cpp" (now available: python3, cpp, c)

```
"tests": [
    {
        "question": "example question",
        "answer": "example answer",
        "is_visible": true
    },
    {...}
],
```

returns 1 if success


### /api/tasks/<int:pk>/change
>changes current task and returns new changed task

#### method: PUT

Args: (send only args that you want to change)

"name": "ex name"

"theory": "ex theory"

"mission": "ex mission"

"sprint": "" (block id - tak it from URL)

"languages": "python3, cpp" (now available: python3, cpp, c)

"task_id": 7 (take it from URL)

```
"tests": [
    {
        "question": "example question",
        "answer": "example answer",
        "is_visible": true
    },
    {...}
],
```
```
{
    "id": 20,
    "name": "ex name",
    "theory": "Теория",
    "mission": "ex practice",
    "sprint": {
        "id": 9,
        "name": "Блок 13",
        "grade": {
            "id": 7,
            "name": "Класс 13",
            "grades": [
                1,
                2,
                3,
                5,
                6,
                7,
                8
            ]
        }
    }
}
```

### /api/tasks/<int:pk>/delete
>deletes current task

#### method: DELETE

just send this request to URL, that contains tasks's id

returns 1 if success


### /api/tasks/<int:pk>/send_code
>Returns an object with status of the request and list of test. In each test you can check it's number in order and status (true or false)

#### method: POST


Args:

"language": "cpp" (now available: python3, cpp, c)

"time_limit_millis": 1000

"task_id": 7 (take it from URL)

"code": "#include <iostream>↵↵using namespace std;↵↵int main() {↵int a,b;↵cin >> a >> b;↵cout << a + b;↵↵}"

course code:
```
#include <iostream>

using namespace std;

int main() {
int a,b;
cin >> a >> b;
cout << a + b;

}
```


response example:
```
{
    "status": true,
    "tests": [
        {
            "test_num": 0,
            "status": true,
            "error": "task_Start: execv(1): /home/ejudge/solves/1/19/in 0<input.txt\nStatus: OK\nCPUTime: 5\nRealTime: 6\nVMSize: 434176\n"
        },
        {
            "test_num": 1,
            "status": false,
            "error": "task_Start: execv(1): /home/ejudge/solves/1/19/in 0<input.txt\nStatus: OK\nCPUTime: 3\nRealTime: 5\nVMSize: 2412544\n"
        }
    ]
}
```
