_base_ = [
    '../_base_/models/faster-rcnn_r50_fpn.py',
    '../_base_/datasets/coco_detection.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

dataset_type = 'CocoDataset'
data_root = 'data/coco/'
# metainfo = {
#     'classes': ('xyr', 'rmz', 'qf',"zj","hnpt","bt","fzthxm","hhytj"),
#     'palette': [
#         (220, 20, 60), (119, 11, 32), (0, 0, 142), (0, 0, 230), (106, 0, 228),
#          (0, 60, 100), (0, 80, 100), (0, 0, 70)
#     ]
# }
class_name=('xyr', 'rmz', 'qf',"zj","hnpt","bt","fzthxm","hhytj")
num_classes=len(class_name)
metainfo=dict(classes=class_name)


train_dataloader = dict(
    batch_size=2,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    batch_sampler=dict(type='AspectRatioBatchSampler'),
    dataset=dict(
        type=dataset_type,
        metainfo=dict(classes=class_name),
        data_root=data_root,
        ann_file='annotations/instances_train2017.json',
        data_prefix=dict(img='train2017/'),
        filter_cfg=dict(filter_empty_gt=True, min_size=32),))
val_dataloader = dict(
    batch_size=1,
    num_workers=2,
    persistent_workers=True,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        metainfo=dict(classes=class_name),
        data_root=data_root,
        ann_file='annotations/instances_val2017.json',
        data_prefix=dict(img='val2017/'),
        test_mode=True,))
test_dataloader = val_dataloader