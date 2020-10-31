# LDT-HACK-2020
THE LEADERS OF THE DIGITAL TRANSFORMATION HACATON 2020

>imagine that this is the "wiki" tab

## Endpoints with examples

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
