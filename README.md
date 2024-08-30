# Screen-to-GPT Workflow Installation

This guide provides step-by-step instructions to install and set up the Screen-to-GPT workflow using Alfred 5. Follow these steps to enhance your productivity with an automated screen-to-text extraction tool that integrates GPT capabilities.

## Prerequisites

Before you begin, make sure you have the following:
- Alfred 5 installed on your machine. You can download it [here](https://www.alfredapp.com/).
- Purchase the premium Powerpack for Alfred 5, available [here](https://www.alfredapp.com/powerpack/).

## Installation Steps

1. **Clone the Repository**  
   Clone the `screen-to-gpt` repository from GitHub using the following command:
   ```bash
   git clone https://github.com/uwumarogie/screen-to-gpt.git

2. **Install the virtual enviroment and dependencies**
   ```python
   python3 -m venv .venv
   ```
   ```bash
   source .venv/bin/activate
   ```
   ```python
   pip3 install -r requirements.txt
   ```
3. **Install the Workflow**  
   Install the `screen-to-gpt.alfredworkflow` by double-clicking on the file.

4. **Configure the Workflow**  
   - Update the path to the repository in the external script tag within the workflow.
   - Modify `run.sh` to reflect your local path and then make the script executable:
     ```bash
     chmod +x run.sh
     ```

5. **Environment Keys**  
   Obtain the necessary environment keys:
   - **Mathpix**: Get the `MATHPIX_APP_ID` and `MATHPIX_APP_KEY` from [Mathpix](https://mathpix.com/).
   - **OpenAI**: Get the `OPENAI_API_KEY` from [OpenAI](https://openai.com/). 

6. **Environment Configuration**  
   Insert the obtained environment keys into the `.env` file located in the root of the cloned repository.

7. **Customize Prompts**  
   Add or modify the prompts in the `prompts` folder as per your requirements.

## Testing

- **Try It Out**: Launch the workflow to see it in action and refine configurations as needed.

## Have Fun!

Explore the capabilities of your new setup and enjoy the seamless integration of screen capture and GPT-powered text manipulation.
