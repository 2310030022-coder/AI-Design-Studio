# 🎨 AI Design Studio — Generative AI Poster and Banner Generator

### AI-Powered Creative Design Application Using Python, OpenAI API and Gradio

**AI Design Studio** is a Generative AI application designed to create customized posters, banners and promotional artwork from natural-language text prompts.

The project integrates OpenAI's image-generation API with a Gradio-based web interface, allowing users to describe their creative ideas, select a visual style and choose an output format.

This application was developed as part of a **Generative AI course-end project** and has been deployed on Render.

## 🌐 Live Website

**[View AI Design Studio](https://ai-design-studio-ns82.onrender.com)**

**Deployment:** Render (Free Tier)

**Current status:** The application interface is deployed and accessible. Live image generation is currently unavailable because the OpenAI API account has no remaining credits.

## 🎯 Project Objective

The objective is to develop an AI-powered creative design platform capable of transforming textual descriptions into visual content using OpenAI's image-generation technology.

The application demonstrates:

- Integration of a Generative AI model through an API.
- Development of an interactive web interface using Gradio.
- Processing of user-provided prompts.
- Selection of artistic styles and image dimensions.
- Handling of API responses and errors.
- Deployment of a Python application using GitHub and Render.

## ✨ Key Features

**1. Text-to-Image Generation**

Users can enter natural-language descriptions for customized posters, banners and promotional artwork.

**2. Multiple Visual Styles**

The application supports five artistic directions:

- Cinematic
- Neon Futuristic
- Minimalist
- Fantasy
- Luxury

**3. Custom Canvas Formats**

Users can select from three output formats:

- Square — Social media posts
- Landscape — Promotional banners
- Portrait — Movie and advertising posters

**4. Interactive Gradio Interface**

A visually styled interface featuring a purple-and-pink theme, text input, style selection, example prompts and an image preview area.

**5. Error Handling**

The application handles missing prompts, missing API keys and API-related failures with error messages.

**6. Cloud Deployment**

The application is connected to GitHub and deployed using Render's free web-service hosting.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main application development |
| OpenAI API | AI image-generation integration |
| Gradio | Interactive web interface |
| Pillow (PIL) | Image processing |
| Google Colab | Development and notebook execution |
| GitHub | Version control and source-code hosting |
| Render | Web application deployment |

## ⚙️ How the Application Works

1. The user enters a description of the desired design.
2. The user chooses an artistic style and canvas format.
3. The application constructs an enhanced image-generation prompt.
4. The Python backend sends the request to OpenAI's API.
5. The API processes the request and returns image data when sufficient credits and access are available.
6. The application processes the returned image using Pillow.
7. Gradio displays the resulting design to the user.

## 💻 Installation and Setup

**Step 1: Clone the repository**

```bash
git clone https://github.com/2310030022-coder/AI-Design-Studio.git
cd AI-Design-Studio
```

**Step 2: Install the dependencies**

```bash
pip install -r requirements.txt
```

**Step 3: Configure the OpenAI API key**

Create an environment variable named `OPENAI_API_KEY` and set its value to your own valid OpenAI API key.

Never publish the API key in source code or commit it to GitHub.

**Step 4: Run the application**

```bash
python app.py
```

**Step 5: Open the Gradio interface**

Open the local URL displayed in the terminal to access the application.

## 🚀 Deployment

The application is deployed on Render and connected to this GitHub repository.

**Live URL:** https://ai-design-studio-ns82.onrender.com

The free instance may enter sleep mode during inactivity, resulting in a slower initial response.

## ⚠️ API Usage and Current Limitations

The application integrates OpenAI's image-generation API.

The original academic problem statement specified `gpt-image-1`. The current implementation uses a replacement model due to changes in model availability.

**Live image generation has not yet been successfully verified**, because the configured OpenAI API account has no remaining credits.

The website, Gradio interface and deployment have been tested successfully. Users wishing to generate images must configure an API key with sufficient credits and appropriate model access.

API usage may incur charges. Public deployments should implement suitable access controls and spending safeguards.

## 📚 Academic Project

**Project Title:** Creating Designs by Leveraging OpenAI and Gradio UI

**Project Category:** Generative Artificial Intelligence

**Application Type:** Text-to-Image Generation

**Course-End Submission:** Jupyter Notebook (`.ipynb`)

**GitHub Repository:** https://github.com/2310030022-coder/AI-Design-Studio

## 🔮 Future Enhancements

Possible future improvements include:

- Integrating additional image-generation providers.
- Adding user authentication.
- Implementing image-generation quotas and rate limiting.
- Supporting additional artistic styles.
- Introducing image editing and regeneration.
- Providing a gallery of generated designs.

## ✅ Conclusion

AI Design Studio demonstrates the integration of Generative AI technology with Python and Gradio to build an interactive creative-design application.

The project covers API integration, prompt processing, user-interface development, image handling, error management and cloud deployment.

The application provides a foundation for developing more advanced AI-powered creative tools.

---

**Project Category:** Generative AI | Python | OpenAI API | Gradio | Cloud Deployment
