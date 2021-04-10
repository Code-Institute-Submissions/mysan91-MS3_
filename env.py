import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "QlRJzdRRG1")
os.environ.setdefault(
    "MONGO_URI", "mongodb+srv://milestone3:<milestone3>@milestone.3exkg.mongodb.net/Task_manager?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "task_manager")
