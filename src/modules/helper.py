import json
import uuid
import pytz

from datetime import datetime


def get_time(time_zone='UTC'):
    """
    Creating a timestamp object
    Args:
     time_zone: UTC
    Returns:
        current timestamp
    """
    tz = pytz.timezone(time_zone)
    return datetime.now(tz)


def get_uuid():
    """
    Creating an unique id
    Returns: str, uuid4
    """
    return str(uuid.uuid4())


def decode_data(req):
    """
    Converts the requests_data into a dictionary
    Args:
        req: b'str'
    Returns:
        error: None if no error; str with error message if any error
        data: dict of request_data if no error; None if any error
    """
    try:
        data = json.loads(req.decode('utf-8'))
        return None, data
    except Exception as exc:
        return 'Service unable to decode data: {}'.format(exc), None


def check_is_valid(**kwargs):
    """
    Checks if incoming request is valid (not None)
    Args:
        kwargs: *
    Returns:
        error: None if no error/no invalid request params; str with error message if any error
    """
    try:
        black_list = []
        for key, value in kwargs.items():
            if value is None:
                black_list.append(key)
            if value == "":
                black_list.append(key)
        if len(black_list) > 0:
            return "Following parameters should not be None or '': {}".format(", ".join(black_list))
        return None
    except Exception as exc:
        return 'Service unable to validate incoming request: {}'.format(exc)