import inspect

from libs.datasets.squad.dataset_squad import dataset_squad
from libs.file_utils import file_utils
from libs.generic_trainer import generic_trainer
import os


class simple_rnn_trainer(generic_trainer):
    def __init__(self):
        super(self.__class__, self).__init__()
        models_path = os.path.join(self.trainer_directory, 'models')
        tensorboard_outputs = os.path.join(self.trainer_directory, 'checkpoints')

        for dirs in [models_path, tensorboard_outputs]:
            file_utils.ensure_folder_exists(dirs)

        self.set_models_path(models_path)
        self.set_tensorboard_outputs_path(tensorboard_outputs)

    def define_graph(self):
        pass

    def define_variables(self):
        pass

    def define_hyperparameters(self):
        pass

    def prepare_datasets(self):
        dataset_path = os.path.dirname(inspect.getfile(dataset_squad))
        dataset_squad.get_dataset_squad(dataset_path)
        self.set_dataset_path(dataset_path)

