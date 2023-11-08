import datetime

log_file_path = "file.log"

with open(log_file_path, "a") as log_file:
    current_time = datetime.datetime.now()
    log_file.write(f"{current_time}: Log entry added by GitHub Actions\n")
