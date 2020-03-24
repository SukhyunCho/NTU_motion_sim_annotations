import json
import numpy as np

json_name = 'sample.json'

with open(json_name, 'r') as json_file:
    json_data = json.load(json_file)

### Basic information of the json file
# print(json_data['info'])
# print(json_data['video'])
# print(json_data['annotations'])
# print(json_data['categories'])

### Joints in a frame
### json_data['annotations'][0]['objects'][frame_num]['keypoints']
# print(json_data['annotations'][0]['objects'][0]['keypoints'])

### As coco joint format
print(np.asarray(json_data['annotations'][0]['objects'][0]['keypoints']).reshape(17,3))
