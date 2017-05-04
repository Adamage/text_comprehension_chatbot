import os
from libs.file_utils import file_utils

squad_url = 'https://rajpurkar.github.io/SQuAD-explorer/dataset/'
files_ext = 'json'


class dataset_squad:
    @staticmethod
    def get_dataset_squad(save_to):
        for dataset_fragment in ['train-v1.1', 'dev-v1.1']:
            dataset_fragment += "." + files_ext
            full_path = os.path.join(save_to, dataset_fragment)
            if os.path.isfile(full_path):
                print('File already exists: {0}'.format(dataset_fragment))
            else:
                file_utils.download_file(url=squad_url + dataset_fragment,
                                         output_file_name=full_path)

if __name__ == "__main__":
    dataset_squad.get_dataset_squad("")
