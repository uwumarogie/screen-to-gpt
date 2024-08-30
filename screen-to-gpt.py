import base64
import json
import os
import sys

import pyperclip
import requests
from dotenv import load_dotenv
from mss import mss
from openai import OpenAI
from PIL import Image

load_dotenv()
MATHPIX_APP_ID = os.environ["MATHPIX_APP_ID"]
MATHPIX_APP_KEY = os.environ["MATHPIX_APP_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
PATH_TO_THIS_REPOSITORY = os.environ["PATH_TO_THIS_REPOSITORY"]

class TextExtractor:
    def __init__(self, app_id: str, app_key: str):
        self.app_id = app_id
        self.app_key = app_key
        self.screenshot_path = ""

    def save_screenshot(self) -> str:
        with mss() as sct:
            monitor = sct.monitors[0]
            sct_img = sct.grab(monitor)

            image = Image.frombytes("RGB", sct_img.size, sct_img.rgb)
            screenshot_path = PATH_TO_THIS_REPOSITORY + "/screenshot.png"
            image.save(screenshot_path)
            return screenshot_path

    def image_to_base64(self, image_path: str) -> str:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()

    def get_text(self) -> str:
        self.screenshot_path = self.save_screenshot()
        image_base64 = self.image_to_base64(self.screenshot_path)

        headers = {
            "app_id": self.app_id,
            "app_key": self.app_key,
            "Content-type": "application/json",
        }

        data = json.dumps(
            {"src": "data:image/png;base64," + image_base64, "formats": ["text"]}
        )

        response = requests.post(
            "https://api.mathpix.com/v3/text", headers=headers, data=data
        )
        result = response.json()
        return result.get("text", "")

    def reset(self):
        self.screenshot_path = ""


class OpenAiService:

    def main(self, prompt, text: str):
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": text},
            ],
        )
        return response.choices[0].message.content

    def format_response(self, response: str):
        result = []
        if "-!-" in response:
            keep = False
            for line in response.split("\n"):
                if line.startswith("-!-"):
                    keep = True
                elif keep:
                    result.append(line)
        else:
            for line in response.split("\n"):
                if line.startswith("```"):
                    continue
                else:
                    result.append(line)
        return "\n".join(result)


if __name__ == "__main__":
    prompt_name = sys.stdin.readline()
    prompt_name = prompt_name.replace("\n", "").replace(" ", "")
    with open(f"{PATH_TO_THIS_REPOSITORY}/prompts/{prompt_name}") as prompt_file:
        prompt = prompt_file.read()
        text_extractor = TextExtractor(
            app_id=MATHPIX_APP_ID,
            app_key=MATHPIX_APP_KEY,
        )
        text = text_extractor.get_text()

        openai_service = OpenAiService()
        response = openai_service.main(prompt, text)
        pyperclip.copy(response)
        text_extractor.reset()
        print(response)
