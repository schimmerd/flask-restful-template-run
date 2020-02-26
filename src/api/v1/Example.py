from flask_restful import Resource
from flask import request
from src.modules.helper import get_uuid, decode_data, check_is_valid


class ExampleClass(Resource):

    def __init__(self, logger):
        self.logger = logger

    def get(self):
        try:
            trace_id = get_uuid()
            self.logger.update_trace_id(trace_id)
            self.logger.update_request_header(api_request=request)

            # Do something fancy stuff :)
            #############################

            return 200
        except Exception as exc:
            msg = "Backend Error: {}".format(exc)
            self.logger.error(msg)
            return msg, 500

    def post(self):
        try:
            # Init new trace_id for logger:
            trace_id = get_uuid()
            self.logger.update_trace_id(trace_id)
            self.logger.update_request_header(api_request=request)

            # Decode data
            error, data = decode_data(req=request.data)
            if error:
                self.logger.error(error)
                return error, 400

            # Validate request
            # **kwargs parameter
            error, data = check_is_valid(id=data.get("ident"))
            if error:
                self.logger.error(error)
                return error, 400

            # Do something fancy stuff :)
            #############################

            return 200
        except Exception as exc:
            msg = "Backend Error: {}".format(exc)
            self.logger.error(msg)
            return msg, 500

