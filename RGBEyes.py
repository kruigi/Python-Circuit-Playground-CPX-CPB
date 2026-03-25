from gpiozero import RGBLED
right_eye_led = RGBLED(red="BOARD3", green="BOARD5", blue="BOARD7")
left_eye_led = RGBLED(red="BOARD8", green="BOARD10", blue="BOARD12")
command = {"robot": "Moby","features": {"eyes": {"set_right_rgb_eye_color": [255, 0, 0]}}}


def get_command():
    return {"robot": "Moby", "features": {"eyes": {"set_right_rgb_eye_color": [255, 0, 0]}}}

eye_rgb = command["features"]["eyes"]["set_right_rgb_eye_color"]
eye_red, eye_green, eye_blue = eye_rgb
print(eye_red, eye_green, eye_blue)



def rgb_eyes(eye, eye_rgb):
    r = eye_rgb[0] / 255
    g = eye_rgb[1] / 255
    b = eye_rgb[2] / 255

    if eye == "right":
        right_eye_led.color = (r, g, b)
    elif eye == "left":
        left_eye_led.color = (r, g, b)
    else:
        print("Invalid eye selection")



rgb_eyes("right", eye_rgb)

def main():
    command = get_command()

    
    if command["robot"] != "Moby":
        print("Command not for this robot")
        return

    eyes_dict = command["features"]["eyes"]

    eyes_dict = command["features"]["eyes"]

if "set_right_rgb_eye_color" in eyes_dict:
    rgb_eyes("right", eyes_dict["set_right_rgb_eye_color"])

elif "set_left_rgb_eye_color" in eyes_dict:
    rgb_eyes("left", eyes_dict["set_left_rgb_eye_color"])




main()
