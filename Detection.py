import torch
import cv2

model = torch.hub.load('WongKinYiu/yolov7', 'custom', 'weights.pt', force_reload=True)

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    results = model(frame)

    for result in results.xyxy[0]:
        x1, y1, x2, y2, conf, cls = result.tolist()
        if conf > 0.1:
            if cls == 1:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, f'{model.names[int(cls)]} {conf:.2f}', (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 2)
            if cls == 2:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
                cv2.putText(frame, f'{model.names[int(cls)]} {conf:.2f}', (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 2)
            if cls == 3:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
                cv2.putText(frame, f'{model.names[int(cls)]} {conf:.2f}', (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 2)
            if cls == 4:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 0), 2)
                cv2.putText(frame, f'{model.names[int(cls)]} {conf:.2f}', (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 2)
            if cls == 5:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 255), 2)
                cv2.putText(frame, f'{model.names[int(cls)]} {conf:.2f}', (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 2)
            if cls == 6:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 255), 2)
                cv2.putText(frame, f'{model.names[int(cls)]} {conf:.2f}', (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 2)
            if cls == 7:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (120, 120, 120), 2)
                cv2.putText(frame, f'{model.names[int(cls)]} {conf:.2f}', (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 2)
            if cls == 8:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (100, 100, 255), 2)
                cv2.putText(frame, f'{model.names[int(cls)]} {conf:.2f}', (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 2)
            if cls == 9:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 100, 100), 2)
                cv2.putText(frame, f'{model.names[int(cls)]} {conf:.2f}', (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 2)
            if cls == 10:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (30, 100, 30), 2)
                cv2.putText(frame, f'{model.names[int(cls)]} {conf:.2f}', (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 2)
            if cls == 11:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (100, 120, 100), 2)
                cv2.putText(frame, f'{model.names[int(cls)]} {conf:.2f}', (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 2)
            if cls == 12:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (200, 0, 30), 2)
                cv2.putText(frame, f'{model.names[int(cls)]} {conf:.2f}', (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 2)

    frame = cv2.resize(frame, (1440, 1080)) 
    cv2.imshow('Chess', frame)

    if cv2.waitKey(1) == ord('q'):
        break