# Alexander Piotrowski
# Dr. Marshall CBIS 4210
# 8/30/2024
def turn_on_lights():
    print("Lights are ON. The business is open.")


def turn_off_lights():
    print("Lights are OFF. The business is closed.")


def main():
    business_open = True  # Assume the business starts as open

    if business_open:
        turn_on_lights()
    else:
        turn_off_lights()

    # Simulate closing the business
    business_open = False

    if business_open:
        turn_on_lights()
    else:
        turn_off_lights()

if __name__ == "__main__":
    main()
