import os
import inspect


class generic_trainer:
    def __init__(self):
        self.models_path = None
        self.tensorboard_outputs = None
        self.dataset_path = None
        self.trainer_directory = os.path.dirname(inspect.getfile(self.__class__))

    def set_models_path(self, to_path):
        self.models_path = to_path

    def set_tensorboard_outputs_path(self, to_path):
        self.tensorboard_outputs = to_path

    def set_dataset_path(self, to_path):
        self.dataset_path = to_path

    def get_trainer_details(self):
        return self.__dict__

    def print_trainer_details(self):
        for key, value in self.__dict__.items():
            print("Property: {0}, value: {1}".format(str(key), str(value)))

    def define_graph(self):
        print("Initialized graph.")

    def define_variables(self):
        print("Initialized variables.")

    def define_hyperparameters(self):
        print("Initialized hyperparameters.")

    def begin_training(self):
        print("Begin training.")

    def prepare_datasets(self):
        print("Ensuring datasets are downloaded.")