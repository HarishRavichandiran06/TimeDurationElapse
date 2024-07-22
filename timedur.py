from datetime import datetime, time

# Helper function to convert str to time object

def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M").time()

# Input time strings

start_time_str = input("Enter the start time(HH:MM): ")
end_time_str = input("Enter the End time(HH:MM): ")

#  convert the time to strings to time objects

start_time = parse_time(start_time_str)
end_time = parse_time(end_time_str)

# convert the time objects to datetime objects with dummy dates

start_datetime = datetime.combine(datetime.today(), start_time)
end_datetime = datetime.combine(datetime.today(), end_time)

# calculate the duration

if end_datetime < start_datetime:
    end_datetime += timedelta(days=1)

total_duration = end_datetime - start_datetime

hours = total_duration.seconds // 3600
minutes = (total_duration.seconds % 3600) //60

# print the result

print(f"Duration : {total_duration}")
print(f"Duration in hours and minutes : {hours} hours, {minutes} minutes")

