from image_generator import generate_image


prompt = input("Enter image prompt: ")

image_bytes = generate_image(prompt)

with open(
        "generated_images/output.png",
        "wb"
) as file:

    file.write(image_bytes)

print("Image saved successfully.")