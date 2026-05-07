# Fusion method performance comparison

## M3FD

### Early Fusion
300 epochs completed in 1.895 hours.
onnx model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-earlyfusion_8b1e2932/weights/best.onnx
2026-05-01 11:01:49
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA GeForce RTX 2080 Ti, 11012MiB)
YOLO11n-RGBT-earlyfusion summary (fused): 240 layers, 2,583,271 parameters, 0 gradients, 6.35 GFLOPs
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 628 images, 0 backgrounds, 0 corrupt: 100% 628/628 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   0% 0/40 [00:00<?, ?it/s]
2026-05-01 11:01:54
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  18% 7/40 [00:05<00:14,  2.21it/s]
2026-05-01 11:01:59
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 40/40 [00:09<00:00,  4.44it/s]
2026-05-01 11:02:04
                   all        628       4555      0.806      0.579      0.652       0.44
                person        446       1708      0.879      0.668      0.799      0.458
                   car        443       2588      0.861      0.786      0.854       0.61
                   bus         53         61      0.785      0.557      0.578      0.417
            motorcycle         55         58       0.67      0.328      0.355      0.227
                 truck        109        140      0.835      0.557      0.673      0.489
Speed: 0.5ms preprocess, 3.0ms inference, 0.0ms loss, 1.1ms postprocess per image


### Mid Fusion
300 epochs completed in 2.137 hours.
onnx model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-midfusion_4707fde3/weights/best.onnx
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA GeForce RTX 2080 Ti, 11012MiB)
YOLO11n-RGBT-midfusion summary (fused): 324 layers, 3,785,663 parameters, 0 gradients, 9.31 GFLOPs
2026-05-01 13:42:48
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 628 images, 0 backgrounds, 0 corrupt: 100% 628/628 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   8% 3/40 [00:03<00:49,  1.33s/it]
2026-05-01 13:42:53
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 40/40 [00:08<00:00,  4.77it/s]
2026-05-01 13:42:59
                   all        628       4555      0.788       0.62      0.671      0.458
                person        446       1708        0.8      0.761      0.814      0.478
                   car        443       2588       0.82      0.807      0.856      0.616
                   bus         53         61      0.781       0.59      0.622      0.454
            motorcycle         55         58      0.663       0.34      0.363      0.212
                 truck        109        140      0.875        0.6      0.702      0.529
Speed: 0.5ms preprocess, 3.5ms inference, 0.0ms loss, 1.8ms postprocess per image

### Mid P3 Fusion
300 epochs completed in 1.752 hours.
onnx model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-midP3fusion_b4558e7c/weights/best.onnx
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA RTX A5000, 24248MiB)
YOLO11n-RGBT-midP3fusion summary (fused): 272 layers, 2,690,111 parameters, 0 gradients, 8.13 GFLOPs
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 628 images, 0 backgrounds, 0 corrupt: 100% 628/628 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   2% 1/40 [00:00<00:32,  1.20it/s]
2026-05-02 21:43:21
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  65% 26/40 [00:06<00:01,  9.69it/s]
2026-05-02 21:43:26
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 40/40 [00:08<00:00,  4.97it/s]
                   all        628       4555       0.86      0.559      0.654      0.451
                person        446       1708       0.91      0.657       0.81      0.468
                   car        443       2588      0.883      0.787      0.864      0.621
                   bus         53         61      0.829      0.525       0.54      0.424
            motorcycle         55         58      0.753      0.276      0.342      0.219
                 truck        109        140      0.928      0.553      0.716      0.521
2026-05-02 21:43:32
Speed: 0.6ms preprocess, 3.6ms inference, 0.0ms loss, 1.0ms postprocess per image

### Mid CMA 3 fusion
300 epochs completed in 1.787 hours.
ONNX model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-midCMA3fusion_698d0d4b/weights/best.onnx
2026-05-04 09:53:13
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA RTX A5000, 24248MiB)
YOLO11n-RGBT-midCMA3fusion summary (fused): 355 layers, 3,732,046 parameters, 0 gradients
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 628 images, 0 backgrounds, 0 corrupt: 100% 628/628 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  20% 8/40 [00:03<00:07,  4.13it/s]
2026-05-04 09:53:19
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 40/40 [00:05<00:00,  6.85it/s]
                   all        628       4555      0.801      0.598      0.652      0.449
                person        446       1708      0.862      0.708      0.811      0.477
                   car        443       2588       0.85      0.803      0.858       0.62
                   bus         53         61      0.737      0.557      0.599      0.441
            motorcycle         55         58      0.686      0.345      0.349      0.216
                 truck        109        140      0.871      0.577      0.643       0.49
Speed: 0.4ms preprocess, 3.5ms inference, 0.0ms loss, 0.7ms postprocess per image

### Mid CFT 3 Fusion
300 epochs completed in 3.148 hours.
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA RTX A5000, 24248MiB)
YOLO11n-RGBT-midCFT3fusion summary: 705 layers, 13,088,575 parameters, 0 gradients, 978.96 GFLOPs
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 628 images, 0 backgrounds, 0 corrupt: 100% 628/628 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   2% 1/40 [00:00<00:20,  1.93it/s]
2026-05-04 17:26:52
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 40/40 [00:06<00:00,  6.37it/s]
2026-05-04 17:26:58
2026-05-04 15:26:54,128 - clearml.Task - INFO - Completed model upload to azure://clearmlstorage.blob.core.windows.net/trainingartefacts/YOLO11-3DNet/yolo11nrgbt_3dnet_train.2257f92166ed49b694e33c3e3db993fc/models/best.pt
                   all        628       4555      0.815      0.586      0.649      0.439
                person        446       1708      0.851      0.724      0.819      0.483
                   car        443       2588      0.831      0.808      0.853      0.617
                   bus         53         61      0.827       0.47      0.535      0.375
            motorcycle         55         58      0.736      0.345      0.366      0.223
                 truck        109        140      0.828      0.585      0.671      0.496
Speed: 0.4ms preprocess, 4.8ms inference, 0.0ms loss, 1.0ms postprocess per image

### Late Fusion
300 epochs completed in 2.603 hours.
onnx model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-latefusion_7827a223/weights/best.onnx
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA GeForce RTX 2080 Ti, 11012MiB)
2026-05-01 11:46:41
YOLO11n-RGBT-latefusion summary (fused): 420 layers, 5,124,399 parameters, 0 gradients, 12.21 GFLOPs
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 628 images, 0 backgrounds, 0 corrupt: 100% 628/628 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   5% 2/40 [00:02<00:55,  1.46s/it]
2026-05-01 11:46:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  90% 36/40 [00:08<00:00,  8.25it/s]
2026-05-01 11:46:52
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 40/40 [00:09<00:00,  4.40it/s]
                   all        628       4555      0.803      0.623       0.69      0.467
                person        446       1708      0.848      0.707      0.808      0.473
                   car        443       2588      0.844      0.803      0.862      0.619
                   bus         53         61      0.703      0.607      0.628      0.485
            motorcycle         55         58      0.776      0.414      0.496      0.279
                 truck        109        140      0.845      0.585      0.657      0.477
Speed: 0.5ms preprocess, 4.2ms inference, 0.0ms loss, 1.0ms postprocess per image

### Score Fusion
300 epochs completed in 2.162 hours.
onnx model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-scorefusion_1534b0e8/weights/best.onnx
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA RTX A5000, 24248MiB)
2026-05-03 09:10:25
YOLO11n-RGBT-scorefusion summary (fused): 471 layers, 5,165,950 parameters, 0 gradients, 12.58 GFLOPs
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 628 images, 0 backgrounds, 0 corrupt: 100% 628/628 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  30% 12/40 [00:03<00:04,  6.53it/s]
2026-05-03 09:10:31
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 40/40 [00:06<00:00,  6.46it/s]
                   all        628       4555      0.784      0.582      0.664      0.445
                person        446       1708      0.833      0.728      0.809      0.472
                   car        443       2588       0.79      0.792      0.846      0.599
                   bus         53         61      0.823      0.475      0.601      0.439
            motorcycle         55         58      0.622       0.31      0.359      0.227
                 truck        109        140      0.851      0.607      0.703      0.489
Speed: 0.4ms preprocess, 3.6ms inference, 0.0ms loss, 0.6ms postprocess per image

## RTDOD

### Early Fusion
300 epochs completed in 6.944 hours.
onnx model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-earlyfusion_db5ee497/weights/best.onnx
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA GeForce RTX 2080 Ti, 11012MiB)
YOLO11n-RGBT-earlyfusion summary (fused): 240 layers, 2,583,466 parameters, 0 gradients, 6.35 GFLOPs
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 1221 images, 201 backgrounds, 0 corrupt: 100% 1221/1221 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  64% 49/77 [00:22<00:02,  9.44it/s]
2026-05-02 14:13:55
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 77/77 [00:25<00:00,  3.06it/s]
                   all       1221      13737      0.833      0.708      0.784      0.489
                person        518       4741      0.904      0.774       0.88      0.583
                   car        676       6231      0.926      0.838      0.922      0.646
            motorcycle        615       1610      0.887       0.74      0.853      0.599
               bicycle        226        281       0.59      0.498      0.441      0.219
                   bus        118        241      0.863      0.679      0.832      0.466
                 truck        211        633      0.828       0.72      0.777      0.422
2026-05-02 14:14:01
Speed: 0.4ms preprocess, 2.9ms inference, 0.0ms loss, 1.9ms postprocess per image

### Mid Fusion
300 epochs completed in 7.967 hours.
onnx model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-midfusion_b9801ea8/weights/best.onnx
2026-05-02 15:15:39
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA GeForce RTX 2080 Ti, 11012MiB)
YOLO11n-RGBT-midfusion summary (fused): 324 layers, 3,785,858 parameters, 0 gradients, 9.31 GFLOPs
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 1221 images, 201 backgrounds, 0 corrupt: 100% 1221/1221 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  99% 76/77 [00:25<00:00,  9.55it/s]
2026-05-02 15:16:06
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 77/77 [00:26<00:00,  2.96it/s]
                   all       1221      13737      0.806      0.759      0.813      0.506
                person        518       4741      0.865      0.818      0.892      0.596
                   car        676       6231      0.895      0.859      0.917      0.639
            motorcycle        615       1610      0.838      0.784      0.859      0.614
               bicycle        226        281      0.615      0.506      0.516      0.257
                   bus        118        241      0.797       0.83      0.877      0.506
                 truck        211        633      0.823      0.758      0.814      0.425
Speed: 0.3ms preprocess, 3.6ms inference, 0.0ms loss, 2.1ms postprocess per image

### Mid P3 Fusion
300 epochs completed in 5.694 hours.
onnx model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-midP3fusion_8f1ac657/weights/best.onnx
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA RTX A5000, 24248MiB)
YOLO11n-RGBT-midP3fusion summary (fused): 272 layers, 2,690,306 parameters, 0 gradients, 8.13 GFLOPs
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 1221 images, 201 backgrounds, 0 corrupt: 100% 1221/1221 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   0% 0/77 [00:00<?, ?it/s]
2026-05-03 01:50:20
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   9% 7/77 [00:05<00:35,  1.95it/s]
2026-05-03 01:50:25
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 77/77 [00:09<00:00,  7.74it/s]
2026-05-03 01:50:30
                   all       1221      13737      0.828       0.75      0.815      0.509
                person        518       4741      0.881      0.811      0.895      0.601
                   car        676       6231      0.909      0.853      0.917      0.645
            motorcycle        615       1610      0.878       0.77      0.864      0.614
               bicycle        226        281      0.667      0.541      0.555      0.322
                   bus        118        241      0.812      0.788      0.865      0.465
                 truck        211        633      0.821      0.736      0.795      0.405
Speed: 0.2ms preprocess, 1.4ms inference, 0.0ms loss, 0.5ms postprocess per image

### Mid CMA3 Fusion
300 epochs completed in 6.385 hours.
ONNX model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-midCMA3fusion_8b739b3c/weights/best.onnx
2026-05-04 14:39:47
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA RTX A5000, 24248MiB)
YOLO11n-RGBT-midCMA3fusion summary (fused): 355 layers, 3,732,241 parameters, 0 gradients
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 1221 images, 201 backgrounds, 0 corrupt: 100% 1221/1221 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   3% 2/77 [00:02<01:42,  1.37s/it]
2026-05-04 14:39:53
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  62% 48/77 [00:08<00:01, 15.32it/s]
2026-05-04 14:39:58
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 77/77 [00:10<00:00,  7.03it/s]
                   all       1221      13737      0.858      0.741      0.817      0.501
                person        518       4741      0.886      0.791       0.89      0.589
                   car        676       6231      0.924      0.849       0.92      0.645
            motorcycle        615       1610       0.89       0.75      0.859      0.613
               bicycle        226        281       0.72      0.544      0.567      0.297
                   bus        118        241      0.886      0.768      0.859      0.461
                 truck        211        633      0.843      0.741      0.805      0.399
Speed: 0.2ms preprocess, 2.0ms inference, 0.0ms loss, 0.9ms postprocess per image

### Mid CFT3 Fusion
300 epochs completed in 11.104 hours.
ONNX export skipped (EXPORT_ONNX=0)
2026-05-04 23:31:55,281 - clearml.Task - INFO - Completed model upload to azure://clearmlstorage.blob.core.windows.net/trainingartefacts/YOLO11-3DNet/yolo11nrgbt_3dnet_train.c1ab6c74aca3424590b2d02340c20996/models/best.pt
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA RTX A5000, 24248MiB)
YOLO11n-RGBT-midCFT3fusion summary: 705 layers, 13,088,770 parameters, 0 gradients, 978.96 GFLOPs
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 1221 images, 201 backgrounds, 0 corrupt: 100% 1221/1221 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   1% 1/77 [00:00<00:34,  2.21it/s]
2026-05-05 01:32:05
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  38% 29/77 [00:07<00:03, 12.75it/s]
2026-05-05 01:32:10
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 77/77 [00:11<00:00,  6.97it/s]
2026-05-05 01:32:16
                   all       1221      13737      0.841       0.75      0.817       0.51
                person        518       4741      0.899       0.79      0.887       0.59
                   car        676       6231      0.913      0.845      0.917      0.646
            motorcycle        615       1610      0.876      0.771      0.861      0.609
               bicycle        226        281      0.674      0.543      0.547      0.296
                   bus        118        241      0.877      0.788      0.873      0.504
                 truck        211        633      0.807      0.764      0.815      0.418
Speed: 0.2ms preprocess, 4.2ms inference, 0.0ms loss, 1.1ms postprocess per image

### Late Fusion
300 epochs completed in 9.195 hours.
onnx model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-latefusion_6fd7b832/weights/best.onnx
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA GeForce RTX 2080 Ti, 11012MiB)
2026-05-02 16:28:36
YOLO11n-RGBT-latefusion summary (fused): 420 layers, 5,124,786 parameters, 0 gradients, 12.21 GFLOPs
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 1221 images, 201 backgrounds, 0 corrupt: 100% 1221/1221 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  16% 12/77 [00:20<00:30,  2.13it/s]
2026-05-02 16:28:57
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 77/77 [00:26<00:00,  2.94it/s]
2026-05-02 16:29:03
                   all       1221      13737      0.834      0.726      0.811      0.509
                person        518       4741      0.898       0.79      0.894      0.605
                   car        676       6231      0.917      0.847      0.922      0.646
            motorcycle        615       1610      0.873      0.729      0.852      0.615
               bicycle        226        281      0.614      0.463      0.517      0.265
                   bus        118        241      0.868      0.793      0.883      0.517
                 truck        211        633      0.836      0.736      0.796      0.403
Speed: 0.3ms preprocess, 4.3ms inference, 0.0ms loss, 2.8ms postprocess per image

### Score Fusion
300 epochs completed in 7.410 hours.
onnx model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-scorefusion_bba4ac03/weights/best.onnx
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA RTX A5000, 24248MiB)
YOLO11n-RGBT-scorefusion summary (fused): 471 layers, 5,166,340 parameters, 0 gradients, 12.58 GFLOPs
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 1221 images, 201 backgrounds, 0 corrupt: 100% 1221/1221 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   3% 2/77 [00:02<01:24,  1.12s/it]
2026-05-03 14:36:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  47% 36/77 [00:07<00:03, 13.26it/s]
2026-05-03 14:36:05
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 77/77 [00:10<00:00,  7.04it/s]
                   all       1221      13737      0.808       0.71      0.773      0.482
                person        518       4741      0.879      0.772      0.871       0.57
                   car        676       6231      0.809      0.851      0.892      0.632
            motorcycle        615       1610      0.866      0.728      0.831      0.592
               bicycle        226        281      0.694      0.488      0.478      0.252
                   bus        118        241      0.875      0.699       0.84      0.455
                 truck        211        633      0.723       0.72      0.725      0.394
2026-05-03 14:36:11
Speed: 0.2ms preprocess, 2.3ms inference, 0.0ms loss, 0.7ms postprocess per image


## Visdrone Dronevehicle

### Early Fusion
300 epochs completed in 7.850 hours.
onnx model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-earlyfusion_2386ffa3/weights/best.onnx
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA RTX A5000, 24248MiB)
YOLO11n-RGBT-earlyfusion summary (fused): 240 layers, 2,582,881 parameters, 0 gradients, 6.34 GFLOPs
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 1469 images, 2 backgrounds, 0 corrupt: 100% 1469/1469 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  52% 48/92 [04:50<00:05,  8.64it/s]
2026-05-02 15:21:22
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 92/92 [04:54<00:00,  3.20s/it]
2026-05-02 15:21:28
                   all       1469      24490      0.905      0.907      0.945      0.693
                   car       1401      21313      0.946      0.967      0.985      0.711
                 truck        588       2388      0.844      0.817      0.883      0.613
                   bus        291        789      0.926      0.935      0.969      0.754
Speed: 7.6ms preprocess, 23.8ms inference, 0.0ms loss, 3.3ms postprocess per image

### Mid Fusion
300 epochs completed in 10.664 hours.
onnx model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-midfusion_8fdbb0fb/weights/best.onnx
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA RTX A5000, 24248MiB)
YOLO11n-RGBT-midfusion summary (fused): 324 layers, 3,785,273 parameters, 0 gradients, 9.31 GFLOPs
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 1469 images, 2 backgrounds, 0 corrupt: 100% 1469/1469 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  40% 37/92 [00:27<00:05,  9.90it/s]
2026-05-02 18:00:58
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 92/92 [00:32<00:00,  2.82it/s]
2026-05-02 18:01:04
                   all       1469      24490      0.916       0.91      0.948      0.697
                   car       1401      21313      0.951      0.964      0.986      0.717
                 truck        588       2388      0.851      0.831      0.888      0.617
                   bus        291        789      0.945      0.935      0.969      0.757
Speed: 0.4ms preprocess, 4.9ms inference, 0.0ms loss, 4.7ms postprocess per image

### Mid P3 Fusion
300 epochs completed in 9.255 hours.
onnx model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-midP3fusion_c559f2cd/weights/best.onnx
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA RTX A5000, 24248MiB)
2026-05-03 05:24:48
YOLO11n-RGBT-midP3fusion summary (fused): 272 layers, 2,689,721 parameters, 0 gradients, 8.13 GFLOPs
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 1469 images, 2 backgrounds, 0 corrupt: 100% 1469/1469 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  78% 72/92 [00:30<00:01, 13.62it/s]
2026-05-03 05:25:20
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 92/92 [00:31<00:00,  2.90it/s]
                   all       1469      24490      0.921      0.908      0.951      0.707
                   car       1401      21313      0.956      0.968      0.987      0.725
                 truck        588       2388      0.857      0.825      0.895      0.629
                   bus        291        789      0.948      0.932       0.97      0.766
Speed: 0.4ms preprocess, 4.6ms inference, 0.0ms loss, 2.9ms postprocess per image

### Mid CFT3 Fusion
300 epochs completed in 31.108 hours.
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA GeForce RTX 2080 Ti, 11012MiB)
2026-05-05 04:37:58
YOLO11n-RGBT-midCFT3fusion summary: 705 layers, 13,088,185 parameters, 0 gradients
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 1469 images, 2 backgrounds, 0 corrupt: 100% 1469/1469 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   1% 1/92 [00:00<01:25,  1.07it/s]
2026-05-05 04:38:05
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   2% 2/92 [00:06<05:05,  3.40s/it]
2026-05-05 04:38:15
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):   4% 4/92 [00:20<08:23,  5.73s/it]
2026-05-05 04:38:21
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  55% 51/92 [00:27<00:05,  7.89it/s]
2026-05-05 04:38:27
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  99% 91/92 [00:32<00:00,  8.23it/s]
2026-05-05 04:38:32
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 92/92 [00:32<00:00,  2.83it/s]
                   all       1469      24490      0.928      0.898      0.947      0.696
                   car       1401      21313      0.955      0.962      0.985      0.718
                 truck        588       2388      0.875      0.795      0.885      0.611
                   bus        291        789      0.955      0.937      0.972      0.758

### Late Fusion
300 epochs completed in 11.966 hours.
onnx model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-latefusion_3a493382/weights/best.onnx
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA RTX A5000, 24248MiB)
YOLO11n-RGBT-latefusion summary (fused): 420 layers, 5,123,625 parameters, 0 gradients, 12.20 GFLOPs
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 1469 images, 2 backgrounds, 0 corrupt: 100% 1469/1469 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  70% 64/92 [00:26<00:02, 11.64it/s]
2026-05-02 19:18:54
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 92/92 [00:29<00:00,  3.15it/s]
                   all       1469      24490      0.921      0.899      0.944      0.696
                   car       1401      21313      0.959      0.959      0.986      0.718
                 truck        588       2388      0.861      0.802      0.882      0.612
                   bus        291        789      0.945      0.937      0.964      0.756
Speed: 0.3ms preprocess, 6.4ms inference, 0.0ms loss, 2.8ms postprocess per image

### Score Fusion
300 epochs completed in 12.995 hours.
onnx model exported to workspace/dataset_rgbt/Results/yolo11n-RGBT-scorefusion_c6ceb1b6/weights/best.onnx
2026-05-03 20:13:35
Ultralytics 8.3.75 🚀 Python-3.10.12 torch-2.1.0a0+32f93b1 CUDA:0 (NVIDIA RTX A5000, 24248MiB)
YOLO11n-RGBT-scorefusion summary (fused): 471 layers, 5,165,170 parameters, 0 gradients, 12.57 GFLOPs
val: Scanning /root/.clearml/venvs-builds/3.10/task_repository/3d-net-clearml.git/workspace/dataset_rgbt/visible/val.cache... 1469 images, 2 backgrounds, 0 corrupt: 100% 1469/1469 [00:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95):  95% 87/92 [00:29<00:00, 11.51it/s]
2026-05-03 20:14:07
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 92/92 [00:29<00:00,  3.08it/s]
                   all       1469      24490      0.914      0.878      0.937      0.684
                   car       1401      21313       0.94      0.955      0.982      0.712
                 truck        588       2388      0.857      0.773      0.866        0.6
                   bus        291        789      0.945      0.907      0.962      0.741
Speed: 0.4ms preprocess, 6.1ms inference, 0.0ms loss, 2.6ms postprocess per image
