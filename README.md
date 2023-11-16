# libello

# Worktree

# Features

### Basic Functions

- ~~Can get a single todo using `todo_id` in DB~~
- ~~Can get all existing todos on DB~~
- ~~Can modify an existing todo in DB~~
- ~~Can add new todo in DB~~
- ~~Can delete existing todo in DB~~
- User can login to the app
- User can logout to the app
- User can view all their tasks by category
- User can add, update, delete tasks in the app
- User should not be able to delete other tasks for other users


### Target Functionalities

- ~~Add categories to todo (Not yet started, Ongoing, Done, Cancelled, Will not do, Stale)~~
- ~~Add separate category for Stale (Yes/No)~~
- Get existing todos by category
- ~~Add deadline to todos~~
- Move todos to to stale when past deadline
- Add ownership to todo
- Create accounts with separate todos
- Add logging in/out functions
- Research Flask-alchemy (Checkout DigitalOcean Flask-Postgres-SQLAlchemy guide)
- Finalize DB for todos and users

### Directory
```
├── app
│   └── lib
│   |    ├── constants.py
│   |    ├── db_methods.py
│   |    └── todo_parser.py
|   |    └── utils.py
|   └── main
|   |    └── routes.py
|   └── models
|   |    └── todos.py
|   └── schema
|   |    └── todo_schema.py
|   └── todos
|        └── routes.py 
|
├── config.py
├── init_db.py
├── README.md
├── requirements.txt
└── run.py
```