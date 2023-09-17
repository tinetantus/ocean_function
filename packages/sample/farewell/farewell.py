import os

db_name = str(os.getenv('DB_NAME'))


def main(args):
    # name = args.get("name", "stranger")
    greeting = "Farewell " + db_name + "!"
    print(greeting)
    return {"body": greeting}