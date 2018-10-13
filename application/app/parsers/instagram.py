import requests
import re


class InstagramParser:

    def get_images_by_keyword(self, keyword: str, max_images: int=20) -> list:
        """
        Get image list by word
        :param keyword:
        :param max_images:

        :return:
        """
        response = requests.get(
            'https://www.instagram.com/explore/tags/%s/' % keyword)
        results = re.findall('"([^"]*cdninstagram[^"]*s480x480[^"]*)', response.text)
        if not results or len(results) < 2:
            return []
        return results[1:max_images + 1]


if __name__ == "__main__":
    parser = InstagramParser()
    for img in parser.get_images_by_keyword("dog"):
        print(img)
