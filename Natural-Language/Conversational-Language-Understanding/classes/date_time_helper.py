from datetime import datetime, timedelta, date, timezone

class DateTimeHelper:
    """
    Helper class for date and time related operations used in conversational language understanding.
    """
    def get_time(self, location):
        # Note: To keep things simple, we'll ignore daylight savings time and support only a few cities.
        # In a real app, you'd likely use a web service API (or write  more complex code!)
        # Hopefully this simplified example is enough to get the the idea that you
        # use LU to determine the intent and entities, then implement the appropriate logic
        if location.lower() == 'local':
            now = datetime.now()
            return '{}:{:02d}'.format(now.hour, now.minute)
        elif location.lower() == 'london':
            utc = datetime.now(timezone.utc)
            return '{}:{:02d}'.format(utc.hour, utc.minute)
        elif location.lower() == 'sydney':
            time = datetime.now(timezone.utc) + timedelta(hours=11)
            return '{}:{:02d}'.format(time.hour, time.minute)
        elif location.lower() == 'new york':
            time = datetime.now(timezone.utc) + timedelta(hours=-5)
            return '{}:{:02d}'.format(time.hour, time.minute)
        elif location.lower() == 'nairobi':
            time = datetime.now(timezone.utc) + timedelta(hours=3)
            return '{}:{:02d}'.format(time.hour, time.minute)
        elif location.lower() == 'tokyo':
            time = datetime.now(timezone.utc) + timedelta(hours=9)
            return '{}:{:02d}'.format(time.hour, time.minute)
        elif location.lower() == 'delhi':
            time = datetime.now(timezone.utc) + timedelta(hours=5.5)
            return '{}:{:02d}'.format(time.hour, time.minute)
        else:
            return "I don't know what time it is in {}".format(location)

    def get_date(self, day):
        # To keep things simple, assume the named day is in the current week (Sunday to Saturday)
        weekdays = {
            "monday": 0,
            "tuesday": 1,
            "wednesday": 2,
            "thursday": 3,
            "friday": 4,
            "saturday": 5,
            "sunday": 6
        }
        today = date.today()
        day = day.lower()
        if day == 'today':
            return today.strftime("%m/%d/%Y")
        elif day in weekdays:
            todayNum = today.weekday()
            weekDayNum = weekdays[day]
            offset = weekDayNum - todayNum
            return (today + timedelta(days=offset)).strftime("%m/%d/%Y")
        return 'I can only determine dates for today or named days of the week.'

    def get_day(self, date_string):
        # Note: To keep things simple, dates must be entered in US format (MM/DD/YYYY)
        try:
            date_object = datetime.strptime(date_string, "%m/%d/%Y")
            return date_object.strftime("%A")
        except Exception:
            return 'Enter a date in MM/DD/YYYY format.'
