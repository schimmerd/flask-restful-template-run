import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from src.api.v1.Example import ExampleClass
from mms.logger.cloud_run_logger import CloudRunLogger

import config

# Init Flask:
app = Flask(__name__)
api = Api(app)
CORS(app)

# Create Logger:
logger = CloudRunLogger(project_id=config.PROJECT_ID,
                        local_run=config.LOCAL_RUN)


api.add_resource(ExampleClass, "/api/v1/example", resource_class_args=(logger,))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))