import os

import json
import matplotlib.pyplot as plt

from fsdet.utils import io as utils_io


# After every experiment you have to delete the content of the 'experiment_folder'
# otherwise it also displays the other experiments in the plot

PROJ_ROOT = str(utils_io.get_project_root())
experiment_folder = os.path.join(PROJ_ROOT, 'checkpoints/coco/faster_rcnn/faster_rcnn_R_101_FPN_base')


def load_json_arr(json_path):
    lines = []
    with open(json_path, 'r') as f:
        for line in f:
            lines.append(json.loads(line))
    return lines


experiment_metrics = load_json_arr(experiment_folder + '/metrics.json')

plt.plot(
    [x['iteration'] for x in experiment_metrics],
    [x['total_loss'] for x in experiment_metrics])
plt.legend(['total_loss'], loc='upper left')
plt.show()

