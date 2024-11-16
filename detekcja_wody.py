import cv2



def detect_water(image_path, output_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Cant load")
        return
    
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    print(hsv_image)
    
    lower_blue = np.array([90, 50, 50])  
    upper_blue = np.array([130, 255, 255])  
    

    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    print("\n\n\n")
    #print(mask)

    result = cv2.bitwise_and(image, image, mask=mask)
    print(result)
    
    cv2.imwrite(output_path, result)
    print(f"Zapisano wynikowy obraz do: {output_path}")
    
    cv2.imshow("Original Image", image)
    cv2.imshow("Detected Water", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect_water("jezioraHimalaje.png", "output_water_detected.jpg")

