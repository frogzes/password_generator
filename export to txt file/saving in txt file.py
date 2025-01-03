from datetime import datetime
from password import password

save_data = True

if save_data:
    data = password
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output = f"{current_time} - {data}\n"
    with open("passwords.txt", "a", encoding="utf-8") as file:
        file.write(output)

    print("Data saved successfully")
else:
    print("Saving is disabled.")