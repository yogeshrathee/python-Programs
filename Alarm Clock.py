import time
import winsound


def set_alarm():
    alarm_time = input("Enter the alarm time in HH:MM format: ")

    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Time to wake up!")
            winsound.Beep(1000, 1000)  # Beep sound for 1 second
            break
        time.sleep(60)  # Check every minute


if __name__ == "__main__":
    set_alarm()
