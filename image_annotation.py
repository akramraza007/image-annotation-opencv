import cv2

# Helper function to convert string input like "100,200" into a tuple (100, 200)
def parse_tuple(input_str):
    return tuple(map(int, input_str.strip().split(',')))

# Prompt user to enter the path to the image file
image_location = input("Enter the location of the image: ")
image = cv2.imread(image_location)  # Load the image using OpenCV

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image. Please check the path and reenter the correct path.")
else:
    # Prompt user to choose a drawing option
    op = input("Choose an option:\n1. To draw the line\n2. To draw rectangle\n3. To draw circle\n4. To Enter the text.\n")

    # Option 1: Draw a line
    if op == "1":
        pt1 = parse_tuple(input("Enter the starting point. eg('x1,x2'): "))
        pt2 = parse_tuple(input("Enter the ending point. eg('y1,y2'): "))
        color = parse_tuple(input("Enter the color code. eg(255,255,255): "))
        thickness = int(input("Enter the thickness of the line: "))
        cv2.line(image, pt1, pt2, color, thickness)  # Draw the line

        # Prompt to show or save the image
        opt = input("Choose an option:\n1. Show\n2. Save")
        if opt == "1":
            cv2.imshow("Line", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif opt == "2":
            save_name = input("Enter the filename to save(e.g, 'output.png')")
            save = cv2.imwrite(save_name, image)
            if save:
                print(f"Image saved as {save_name}")
            else:
                print("Error: Could not save the image. Please try again....")
        else:
            print("Wrong input. Please enter 1 for show or 2 for save.")

    # Option 2: Draw a rectangle
    elif op == "2":
        pt1 = parse_tuple(input("Enter the top corner point. eg('x1,x2'): "))
        pt2 = parse_tuple(input("Enter the ending corner point. eg('y1,y2'): "))
        color = parse_tuple(input("Enter the color code. eg(255,255,255): "))
        thickness = int(input("Enter the thickness of the line: "))
        cv2.rectangle(image, pt1, pt2, color, thickness)  # Draw the rectangle

        opt = input("Choose an option:\n1. Show\n2. Save")
        if opt == "1":
            cv2.imshow("Rectangle", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif opt == "2":
            save_name = input("Enter the filename to save(e.g, 'output.png')")
            save = cv2.imwrite(save_name, image)
            if save:
                print(f"Image saved as {save_name}")
            else:
                print("Error: Could not save the image. Please try again....")
        else:
            print("Wrong input. Please enter 1 for show or 2 for save.")

    # Option 3: Draw a circle
    elif op == "3":
        center = parse_tuple(input("Enter the center of the circle. eg('c1,c2'): "))
        radius = int(input("Enter the radius of the circle: "))
        color = parse_tuple(input("Enter the color code. eg(255,255,255): "))
        thickness = int(input("Enter the thickness of the line: "))
        cv2.circle(image, center, radius, color, thickness)  # Draw the circle

        opt = input("Choose an option:\n1. Show\n2. Save")
        if opt == "1":
            cv2.imshow("Circle", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif opt == "2":
            save_name = input("Enter the filename to save(e.g, 'output.png')")
            save = cv2.imwrite(save_name, image)
            if save:
                print(f"Image saved as {save_name}")
            else:
                print("Error: Could not save the image. Please try again....")
        else:
            print("Wrong input. Please enter 1 for show or 2 for save.")

    # Option 4: Add text to the image
    elif op == "4":
        text = input("Enter the text: ")
        org = parse_tuple(input("Enter the origin. eg('x1,x2'): "))
        fontscale = float(input("Enter the font Size: "))
        color = parse_tuple(input("Enter the color. eg(255,255,255): "))
        thickness = int(input("Enter the thickness: "))
        cv2.putText(image, text, org, cv2.FONT_HERSHEY_SIMPLEX, fontscale, color, thickness)  # Add text

        opt = input("Choose an option:\n1. Show\n2. Save")
        if opt == "1":
            cv2.imshow("Text", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif opt == "2":
            save_name = input("Enter the filename to save(e.g, 'output.png')")
            save = cv2.imwrite(save_name, image)
            if save:
                print(f"Image saved as {save_name}")
            else:
                print("Error: Could not save the image. Please try again....")
        else:
            print("Wrong input. Please enter 1 for show or 2 for save.")

    # Invalid option handling
    else:
        print("Wrong input.")