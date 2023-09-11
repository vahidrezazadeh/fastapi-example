import datetime

import pytz

from settings import settings

class TimeZoneUtils:
    def __init__(self, timezone_str=settings.DATETIME_TIMEZONE):
        self.timezone = pytz.timezone(timezone_str)

    def get_timezone_datetime(self) -> datetime.datetime:
        """
        Get time zone time

        :return:
        """
        return datetime.datetime.now(self.timezone)

    def get_timezone_timestamp(self) -> int:
        """
        Get time zone timestamp (seconds)

        :return:
        """
        return int(self.get_timezone_datetime().timestamp())

    def get_timezone_milliseconds(self) -> int:
        """
      Get time zone timestamp (millisecond)

        :return:
        """
        return int(self.get_timezone_datetime().timestamp() * 1000)

    def datetime_to_timezone_str(self, dt: datetime.datetime, format_str: str = settings.DATETIME_FORMAT) -> str:
        """
        Convert datetime object to time zone time string

        :param dt:
        :param format_str:
        :return:
        """
        return dt.astimezone(self.timezone).strftime(format_str)

    def datetime_to_timezone_datetime(self, dt: datetime.datetime) -> datetime.datetime:
        """
        Convert datetime object to datetime time zone object

        :param dt:
        :return:
        """
        return dt.astimezone(self.timezone)

    @staticmethod
    def datetime_to_timezone_utc(dt: datetime.datetime) -> datetime.datetime:
        """
        datetime object to datetime UTC object

        :param dt:
        :return:
        """
        return dt.astimezone(pytz.utc)

    def datetime_to_timezone_timestamp(self, dt: datetime.datetime) -> int:
        """
        Convert datetime object to time zone timestamp (seconds)

        :param dt:
        :return:
        """
        return int(dt.astimezone(self.timezone).timestamp())

    def datetime_to_timezone_milliseconds(self, dt: datetime.datetime) -> int:
        """
        datetime object to time zone timestamp (milliseconds)

        :param dt:
        :return:
        """
        return int(dt.astimezone(self.timezone).timestamp() * 1000)

    def str_to_timezone_utc(self, time_str: str, format_str: str = settings.DATETIME_FORMAT) -> datetime.datetime:
        """
        Convert time string to time zone datetime UTC object

        :param time_str:
        :param format_str:
        :return:
        """
        dt = datetime.datetime.strptime(time_str, format_str).replace(tzinfo=self.timezone)
        return self.datetime_to_timezone_utc(dt)

    def str_to_timezone_datetime(self, time_str: str, format_str: str = settings.DATETIME_FORMAT) -> datetime.datetime:
        """
        Convert time string to datetime time zone object

        :param time_str:
        :param format_str:
        :return:
        """
        return datetime.datetime.strptime(time_str, format_str).replace(tzinfo=self.timezone)

    def utc_datetime_to_timezone_datetime(self, utc_time: datetime.datetime) -> datetime.datetime:
        """
        Convert datetime UTC object to datetime time zone object

        :param utc_time:
        :return:
        """
        return utc_time.replace(tzinfo=pytz.utc).astimezone(self.timezone)

    def utc_timestamp_to_timezone_datetime(self, timestamp: int) -> datetime.datetime:
        """
        Timestamp to datetime time zone object

        :param timestamp:
        :return:
        """
        utc_datetime = datetime.datetime.utcfromtimestamp(timestamp).replace(tzinfo=pytz.utc)
        return self.datetime_to_timezone_datetime(utc_datetime)

    def get_timezone_expire_time(self, expires_delta: datetime.timedelta) -> datetime.datetime:
        """
        Get time zone expiration time

        :param expires_delta:
        :return:
        """
        return self.get_timezone_datetime() + expires_delta

    def get_timezone_expire_seconds(self, expire_datetime: datetime.datetime) -> int:
        """
        Get the time interval (seconds) from the specified time to the current time

        :param expire_datetime: a datetime object specifying the time
        :return: time interval (seconds)
        """
        timezone_datetime = self.get_timezone_datetime()
        expire_datetime = self.datetime_to_timezone_datetime(expire_datetime)
        if expire_datetime < timezone_datetime:
            return 0
        return int((expire_datetime - timezone_datetime).total_seconds())


timezone_utils = TimeZoneUtils()