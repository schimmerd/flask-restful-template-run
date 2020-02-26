import os

# Setting environment variables for prod or dev
# depends on the parameter in cloudbuild_dev/prod.yaml: RUN_MODE=dev or RUN_MODE=prod


class Options(object):

    def __init__(self):

        # General options:
        self.servie_revision = '{}-latest'
        self.project_id = '{}'

        # Dev options:
        self.dev_SERVICE_NAME = '{}-dev'
        self.dev_local_run = True # Todo Change to False in 'cloud' mode !!

        # Prod options:
        self.prod_SERVICE_NAME = '{}'
        self.prod_local_run = True # Todo Change to False in 'cloud' mode !!

        # Mode (from Environment):
        self.run_mode = os.getenv('RUN_MODE', 'dev').lower()

    # Method to avoid duplicated code:
    def __check_if_prod(self, dev_parameter, prod_parameter):
        parameter = dev_parameter
        if self.run_mode == 'prod':
            parameter = prod_parameter
        return parameter

    # Getter of options:
    def get_service_name(self):
        return self.__check_if_prod(dev_parameter=self.dev_SERVICE_NAME, prod_parameter=self.prod_SERVICE_NAME)

    def get_local_run(self):
        return self.__check_if_prod(dev_parameter=self.dev_local_run, prod_parameter=self.prod_local_run)

    def get_project_id(self):
        return self.project_id

    def get_service_revision(self):
        return self.servie_revision
