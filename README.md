
# Screen-to-GPT Workflow Installation Guide

Welcome to the **Screen-to-GPT Workflow**! This guide provides comprehensive, step-by-step instructions to install and set up the Screen-to-GPT workflow using Alfred 5. Enhance your productivity with this automated screen-to-text extraction tool integrated with GPT capabilities.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation Steps](#installation-steps)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set Up the Virtual Environment](#2-set-up-the-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Install the Workflow](#4-install-the-workflow)
  - [5. Obtain Environment Keys](#5-obtain-environment-keys)
  - [6. Configure Environment Variables](#6-configure-environment-variables)
  - [7. Customize Prompts](#7-customize-prompts)
- [Testing the Workflow](#testing-the-workflow)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Prerequisites

Before you begin, ensure you have the following:

- **Alfred 5**: Download and install from [Alfred's official website](https://www.alfredapp.com/).
- **Alfred Powerpack**: Purchase and activate the Powerpack from [here](https://www.alfredapp.com/powerpack/).
- **Git**: Ensure Git is installed on your machine. Download it from [git-scm.com](https://git-scm.com/).
- **Python 3**: Verify Python 3 is installed. Download it from [python.org](https://www.python.org/downloads/).

## Installation Steps

Follow these steps to install and set up the Screen-to-GPT workflow:

### 1. Clone the Repository

Open your terminal and clone the `screen-to-gpt` repository from GitHub:

```bash
git clone https://github.com/uwumarogie/screen-to-gpt.git
```

Navigate to the project directory:

```bash
cd screen-to-gpt
```

### 2. Set Up the Virtual Environment

Create and activate a Python virtual environment to manage dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

> **Note**: On Windows, activate the virtual environment using:
>
> ```bash
> .\.venv\Scripts\activate
> ```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Install the Workflow

Install the `screen-to-gpt.alfredworkflow` by double-clicking the file or using the terminal:

```bash
open screen-to-gpt.alfredworkflow
```

> **Note**: Ensure Alfred is running before executing the above command.

### 5. Obtain Environment Keys

You need API keys for the following services:

- **Mathpix**:
  - Sign up at [Mathpix](https://mathpix.com/).
  - Obtain your `MATHPIX_APP_ID` and `MATHPIX_APP_KEY` from your Mathpix dashboard.

- **OpenAI**:
  - Sign up or log in at [OpenAI](https://openai.com/).
  - Navigate to the API section and generate your `OPENAI_API_KEY`.

### 6. Configure Environment Variables

Create a `.env` file in the root of the cloned repository and add your API keys:

```env
MATHPIX_APP_ID=your_mathpix_app_id
MATHPIX_APP_KEY=your_mathpix_app_key
OPENAI_API_KEY=your_openai_api_key
```

Ensure the `.env` file is saved securely and **do not** share it publicly.

### 7. Customize Prompts

Tailor the GPT prompts to fit your workflow needs:

1. Navigate to the `prompts` folder in the repository.
2. Open the desired prompt file (e.g., `default_prompt.txt`) in a text editor.
3. Modify the prompts as needed to suit your requirements.
4. Save the changes.

## Testing the Workflow

After completing the installation and configuration:

1. **Activate Alfred**: Press your Alfred hotkey (default is `⌥ + Space`).
2. **Trigger the Workflow**: Type the workflow keyword (e.g., `s2g`) and execute.
3. **Capture Screen**: Follow the on-screen instructions to capture a portion of your screen.
4. **Review Output**: The extracted text and GPT-processed results will be displayed.

## Troubleshooting

If you encounter issues during installation or usage, consider the following steps:

- **Verify Dependencies**: Ensure all prerequisites are correctly installed.
- **Check API Keys**: Confirm that your API keys in the `.env` file are accurate and active.
- **Permissions**: Ensure `run.sh` has execute permissions:
  
  ```bash
  chmod +x run.sh
  ```
  
- **Review Logs**: Check terminal or Alfred logs for error messages.
- **Consult Documentation**: Refer to the [Alfred Documentation](https://www.alfredapp.com/help/) for workflow-specific issues.

If problems persist, feel free to [open an issue](https://github.com/uwumarogie/screen-to-gpt/issues) on the GitHub repository.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   
   ```bash
   git checkout -b feature/YourFeature
   ```
   
3. Commit your changes:
   
   ```bash
   git commit -m "Add your message"
   ```
   
4. Push to the branch:
   
   ```bash
   git push origin feature/YourFeature
   ```
   
5. Open a pull request detailing your changes.

Please ensure your code follows the project's coding standards and includes appropriate tests.

## License

This project is licensed under the [MIT License](LICENSE).

## Support

For support, please [open an issue](https://github.com/uwumarogie/screen-to-gpt/issues) on the GitHub repository or contact the maintainer at [your-email@example.com](mailto:your-email@example.com).

---

*Enjoy the seamless integration of screen capture and GPT-powered text manipulation!*
