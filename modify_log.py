import datetime

log_file_path = "file.log"

with open(log_file_path, "x") as log_file:
    current_time = datetime.datetime.now()
    log_file.write(f"{current_time}: Log entry added by GitHub Actions\n")
    print(f"{current_time}: Log entry added by GitHub Actions\n")
