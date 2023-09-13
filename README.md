# libello

# Worktree

# Features

### Basic Functions

- [] Can get a single todo using `todo_id`
- [] Can get all existing todos on DB
- [] Can modify an existing todo 
- [] Can add new todo
- [] Can delete existing todo

### Target Functionalities

- [] Add categories to todo (Not yet started, Ongoing, Done, Cancelled, Will not do, Stale)
- [] Add separate category for Stale (Yes/No)
- [] Get existing todos by category
- [] Add deadline to todos
- [] Move todos to to stale when past deadline
- [] Add ownership to todo
- [] Create accounts with separate todos
- [] Add logging in/out functions
- [] Research Flask-alchemy (Checkout DigitalOcean Flask-Postgres-SQLAlchemy guide)
- [] Finalize DB for todos and users

### Directory

config
api
    -v1
        -resources
            -controller
                -todo_controller
            -models
                -todo_model
        -routes
lib
    -constants
    -db_methods
app.py