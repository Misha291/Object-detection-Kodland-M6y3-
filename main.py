!pip install ImageAI

!wget https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/yolov3.pt

from imageai.Detection import ObjectDetection

def detect_object_on_road (input_image, output_image, model_path):
  detector = ObjectDetection()
  detector.setModelTypeAsYOLOv3()
  detector.setModelPath(model_path)
  detector.loadModel()

  detections = detector.detectObjectsFromImage(
  input_image= input_image, 
  output_image_path= output_image, 
  minimum_percentage_probability=30)

  return detections

def analiz_objects(detections):
  road_objects = []

  if len(detections)>0:
    for detection in detections:
      if detection["name"] in ["car", "motorbike", "bicycle", "person", "bus", 'train', 'truck','traffic_light', 'stop_sign']:
              road_objects.append(detection)
  return road_objects

def print_ruls():
  print("это")
  print("программа")
  print("детектирования")
  print("объектов")
  print("!")

input_image = "i.jpeg"
output_image = "output_image.jpeg"
detections = detect_object_on_road(input_image, output_image, "/content/yolov3.pt")
road_objects = analiz_objects(detections)
if len(road_objects) > 0:
  print("Обнаруженные участники дорожного движения:")
  for obj in road_objects:
      print(obj["name"], " : ", obj["percentage_probability"], " : ", obj["box_points"])
else:
   print("Ни одного участника дорожного движения не обнаружено!")
