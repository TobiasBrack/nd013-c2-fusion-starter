# Mid-Term Project: 3D Object Detection
## Section 1 : Compute Lidar Point-Cloud from Range Image
### Visualize range image channels (ID_S1_EX1)
Frame 0
![Range Image Output 0](ex_plots\range_image_output_0.png)
Frame 1
![Range Image Output 1](ex_plots\range_image_output_1.png)

### Visualize lidar point-cloud (ID_S1_EX2)
Frame 0
![LIdar Point Cloud](ex_plots\Lidar_Point_Cloud.png)
## Section 2 : Create Birds-Eye View from Lidar PCL
### Convert sensor coordinates to BEV-map coordinates (ID_S2_EX1)
Frame 0
![BEV-map](ex_plots\BEV_frame0.png)
### Compute intensity layer of the BEV map (ID_S2_EX2)
Frame 0
![intensity layer](ex_plots\intens_frame0.png)
### Compute height layer of the BEV map (ID_S2_EX3)
Frame 0
![height layer](ex_plots\height_map_frame0.png)

## Section 3 : Model-based Object Detection in BEV Image
### Add a second model from a GitHub repo (ID_S3_EX1)
### Extract 3D bounding boxes from model response (ID_S3_EX2)
Frame 50
![height layer](ex_plots\3D_boundingbox.png)

 ## Section 4 : Performance Evaluation for Object Detection

### Compute intersection-over-union between labels and detections (ID_S4_EX1)
### Compute false-negatives and false-positives (ID_S4_EX2)
### Compute precision and recall (ID_S4_EX3)
Plausibility check: 

`configs_det.use_labels_as_objects = True`
![Precision and Recall](ex_plots\uselabelsasobjects_true.png)
precision = 1.0, recall = 1.0

`configs_det.use_labels_as_objects = False`
![Precision and Recall](ex_plots\uselabelsasobjects_false.png)
precision = 0.9506578947368421, recall = 0.9444444444444444
