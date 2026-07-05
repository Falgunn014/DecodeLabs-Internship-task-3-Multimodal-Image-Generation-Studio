Multimodal Image Generation Studio

This project was developed as part of the DecodeLabs Generative AI Internship (Week 3).

The objective of this project is to generate images from natural language prompts using an AI image generation model. The application accepts a text prompt from the user and saves the generated image automatically.

Project Features

- Text-to-image generation
- Saves generated images automatically
- Simple command-line interface
- Organized project structure
- API-based image generation

Technologies Used

- Python 3.12
- Requests
- Hugging Face Inference API

Project Structure

```
Task 3 - Multimodal Image Generation Studio

app.py
image_generator.py
config.py
requirements.txt
README.md

generated_images/
```

Installation

```bash
pip install -r requirements.txt
```

Configuration

Add your API token inside `config.py`.

Run

```bash
python app.py
```

Example

```
Enter image prompt:

Generate a realistic apple image
```

The generated image is saved inside the `generated_images` folder.

Learning Outcomes

This project helped me understand text-to-image generation, API communication, image handling, and project organization.

Author

Falgun Nagpure

DecodeLabs Generative AI Internship – Week 3
