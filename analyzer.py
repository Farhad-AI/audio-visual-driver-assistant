class Analyzer:
    img = None
    def __init__(self):
        self.model = YOLO("Traffic-Light-Detection-YOLOv8-main/weights/v9 - 64 epochs.pt")
        self.class_names = ["green", "red", "yellow"]
        
    def analyze(self, rectangulars_info): 
        Analyzer.img =  cv2.imread(Model.file_address) 
        analyze_results = []
        for i in range(len(rectangulars_info)):
            y1, y2 = int(rectangulars_info[i][-1][1]), int(rectangulars_info[i][-1][3])
            x1, x2 = int(rectangulars_info[i][-1][0]), int(rectangulars_info[i][-1][0])
            cropped_img = Analyzer.img[y1-50:y2+50, x1-50:x2+50]
            results = self.model(cropped_img, )
            for r in results:
                boxes = r.boxes
                for box in boxes:
                    #confidence = math.ceil((box.conf[0]*100))/100
                    #print("Confidence --->",confidence)
                    cls = int(box.cls[0])
                    #print("Class name -->", self.class_names[cls])
                    analyze_results.append(self.class_names[cls])
        return analyze_results