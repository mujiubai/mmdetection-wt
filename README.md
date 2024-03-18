# 环境安装：
conda create --name mmlab python=3.8 -y
conda activate mmlab
pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/cu111/torch_stable.html
pip install tensorboard
pip install -U openmim
mim install mmengine
mim install "mmcv>=2.0.0"
pip install pycocotools
pip install shapely
pip install terminaltables
pip install scipy


## 分布式训练
CUDA_VISIBLE_DEVICES=2,8 bash tools/dist_train.sh configs/faster_rcnn/faster-rcnn_r50_fpn_1x_coco.py 2

## 测试

python tools/test.py configs/faster_rcnn/faster-rcnn_r50_fpn_1x_coco.py work_dirs/faster-rcnn_r50_fpn_1x_coco/epoch_12.pth