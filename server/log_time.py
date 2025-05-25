import datetime

def log_session(task: str):
    now = datetime.datetime.now()
    log_entry = f"{now.strftime('%Y-%m-%d %H:%M:%S')} - {task}\n"
    
    with open("logs/time_log.txt", "a") as log_file:
        log_file.write(log_entry)
    
    print(f"🕒 Logged: {task}")

if __name__ == "__main__":
    task = input("Enter what you're working on: ")
    log_session(task)
