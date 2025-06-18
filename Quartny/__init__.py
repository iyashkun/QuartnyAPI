import re
import os
import json
import base64
import string
import random
import urllib
import requests
from bs4 import BeautifulSoup
from base64 import b64decode as m
from base64 import b64encode as n
from requests_html import HTMLSession
from PIL import Image, ImageDraw, ImageFont
from Quartny.Funcs import payloads_response, advance_GPT_Mode, payload_8

__version__ = "0.1.0"
__all__ = ["Ai"]

class Quartny:
    def __init__(self)->None:
        """
        API Uses For Verious Prepose
        Support : https://telegram.me/InfinityHorizen
        Owner : @Quartny
        """
        pass
    
    @staticmethod
    def datagpt(args:str):
        """
        Example Usage:
        >>> from Quartny import Ai
        >>> response = Ai.datagpt("What are the latest trends in AI?")
        >>> print(response)
        """
        url = m("aHR0cHM6Ly9hcHAuY3JlYXRvci5pby9hcGkvY2hhdA==").decode("utf-8")
        payload = {
            "question": args,
            "chatbotId": "712544d1-0c95-459e-ba22-45bae8905bed",
            "session_id": "8a790e7f-ec7a-4834-be4a-40a78dfb525f",
            "site": "datacareerjumpstart.mykajabi.com"
        }
        try:
            response = requests.post(url, json=payload)
            extracted_text = re.findall(r"\{(.*?)\}", response.text, re.DOTALL)
            extracted_json = "{" + extracted_text[0] + "}]}"
            json_text = extracted_json.replace('\n', ' ')
            data = json.loads(json_text)
            return {"results":data["text"], "owner": "@Quartny", "success": True
                    }
        except Exception as eo:
            return eo
    
    @staticmethod
    def blackpink(args):
        text = args
        font_path = os.path.dirname(__file__)+"blackpink.otf"
        font_size = 230
        font = ImageFont.truetype(font_path, font_size)
        fontsize = int(font.getlength(text))
        img = Image.new("RGB", (fontsize + 100, font_size + 100), color=(0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.text(
            ((img.width - fontsize) / 2, 0),
            text,
            fill=(255, 148, 224),
            font=font,
            align="center",
        )
        draw.rectangle([0, 0, img.width, img.height], outline="#ff94e0", width=20)
        img2 = Image.new("RGB", (fontsize + 800, font_size + 300), color=(0, 0, 0))
        img2.paste(img, (350, 100))

        buffered = io.BytesIO()
        img2.save(buffered, format="JPEG")
        img_str = n(buffered.getvalue()).decode("utf-8")
        return img_str
    
    @staticmethod
    def blackbox(args: str) -> requests.Response:
        """
        Example Usage:
        >>> from Quartny import Ai
        >>> response = Ai.blackbox("Hello, how are you?")
        >>> print(response.text)
        {
            "response": "Generated content response",
            "status": 200
        }
        """
        url = m('aHR0cHM6Ly93d3cuYmxhY2tib3guYWkvYXBpL2NoYXQ=').decode("utf-8")
        payload = {
            "agentMode": {},
            "codeModelMode": True,
            "id": "XM7KpOE",
            "isMicMode": False,
            "maxTokens": None,
            "messages": [
                {
                    "id": "XM7KpOE",
                    "content": urllib.parse.unquote(args),
                    "role": "user"
                }
            ],
            "previewToken": None,
            "trendingAgentMode": {},
            "userId": "87cdaa48-cdad-4dda-bef5-6087d6fc72f6",
            "userSystemPrompt": None
        }
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'sessionId=f77a91e1-cbe1-47d0-b138-c2e23eeb5dcf; intercom-id-jlmqxicb=4cf07dd8-742e-4e3f-81de-38669816d300; intercom-device-id-jlmqxicb=1eafaacb-f18d-402a-8255-b763cf390df6; intercom-session-jlmqxicb=',
            'Origin': m('aHR0cHM6Ly93d3cuYmxhY2tib3guYWk=').decode("utf-8"),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                return {"results": response.text, "owner": "@Quartny", "success": True}
        except Exception as eo:
            return eo
    
    @staticmethod
    def chatgpt(args:str,mode:str=False):
        """
        Example Usage:
        >>> from Quartny import Ai
        >>> response = Ai.chatgpt("hi babe?", mode="girlfriend")
        >>> print(response)
        """
        if not mode:
            session = requests.Session()
            response_data=payloads_response(payloads=payload_8, args=args)
            url = m("aHR0cHM6Ly9hcGkuZXhoLmFpL2NoYXRib3QvdjEvZ2V0X3Jlc3BvbnNl").decode("utf-8")
            headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6ImJvdGlmeS13ZWItdjMifQ.O-w89I5aX2OE_i4k6jdHZJEDWECSUfOb1lr9UdVH4oTPMkFGUNm9BNzoQjcXOu8NEiIXq64-481hnenHdUrXfg",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
            response = session.post(url, headers=headers, data=json.dumps(response_data))
            return {"results":response.json()["response"], "join": "@Mr_Sukkun", "success": True}
        else:
            try:
                result = advance_GPT_Mode(args, mode)
                return {"results":result, "owner": "@Quartny", "success": True}
            except Exception as eo:
                return eo
    
    @staticmethod
    def gemini(args: str) -> dict:
        """
        Example Usage:
        >>> from Quartny import Ai
        >>> generated_content = Ai.gemini("Hello, how are you?")
        >>> print(generated_content)
        """
        url = m('aHR0cHM6Ly9nZW5lcmF0aXZlbGFuZ3VhZ2UuZ29vZ2xlYXBpcy5jb20vdjFiZXRhL21vZGVscy9nZW1pbmktcHJvOmdlbmVyYXRlQ29udGVudD9rZXk9QUl6YVN5QlFhb1VGLUtXalBWXzRBQnRTTjBEUTBSUGtOZUNoNHRN').decode("utf-8")
        headers = {'Content-Type': 'application/json'}
        payload = {
            'contents': [
                {'parts': [{'text': args}]}
            ]
        }
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            if response.status_code == 200:
                generated_text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
                return {"results":generated_text, "owner": "@Quartny", "success": True}
        except Exception as eo:
            return eo
    
    @staticmethod
    def hashtag(arg: str)-> list:
        """
        Example Usage:
        >>> from Quartny import Ai
        >>> keyword = "python"
        >>> hashtag = Ai.hashtag(keyword)
        >>> print(hashtag)
        """
        url = m("aHR0cHM6Ly9hbGwtaGFzaHRhZy5jb20vbGlicmFyeS9jb250ZW50cy9hamF4X2dlbmVyYXRvci5waHA=").decode("utf-8")
        data = {"keyword": arg, "filter": "top"}
        response = requests.post(url, data=data).text
        content = BeautifulSoup(response, "html.parser").find("div", {"class": "copy-hashtags"}).string
        output=content.split()
        return output
    
    @staticmethod
    def chatbot(args:str)->str:
        """
        Example Usage:
        >>> from Quartny import Ai
        >>> input = "Hello, how are you?"
        >>> response = Ai.chatbot(input)
        >>> print(response)
        """
        x = base64.b64decode("aHR0cHM6Ly9mYWxsZW54Ym90LnZlcmNlbC5hcHAvYXBpL2FwaWtleT01OTM1NjA4Mjk3LWZhbGxlbi11c2JrMzNrYnN1L2dyb3VwLWNvbnRyb2xsZXIvbXVrZXNoL21lc3NhZ2U9").decode("utf-8")
        full_url = f"{x}{args}"
        response = requests.get(full_url).json()["reply"]
        return response
    
    
    @staticmethod
    def bhagwatgita(chapter: int, shalok: int = 1) -> requests.Response:
        """
        Example Usage:
        >>> from Quartny import Ai
        >>> verse_data = Ai.bhagwatgita(1, 5)
        >>> print(verse_data)
        """
        xc=base64.b64decode("aHR0cHM6Ly93d3cuaG9seS1iaGFnYXZhZC1naXRhLm9yZy9jaGFwdGVyLw==").decode(encoding="utf-8")
        url = f"{xc}{chapter}/hi"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraph = soup.find("p")
        chapter_intro = soup.find("div", class_="chapterIntro")
        co = soup.find_all("section", class_="listItem")
        output = [i.text.strip().replace("View commentary »", "").replace("Bhagavad Gita ", "").strip()  for i in co]
        data = {
            "chapter_number": chapter,
            "verse": paragraph.text,
            "chapter_intro": chapter_intro.text,
            "shalok": output[shalok],
        }
        return data

    
    @staticmethod
    def imdb(args: str) -> dict:
        """
        Example Usage:
        >>> from Quartny import Ai
        >>> movie_data = Ai.imdb("1920")
        >>> print(movie_data)
        """
        session = HTMLSession()

        url = f"https://www.imdb.com/find?q={args}"
        response = session.get(url)
        results = response.html.xpath("//section[@data-testid='find-results-section-title']/div/ul/li")
        urls = [result.find("a")[0].attrs["href"] for result in results][0]
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(f"https://www.imdb.com/{urls}", headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        movie_name = soup.title.text.strip()
        meta_tags = soup.find_all("meta")
        description = ""
        keywords = ""
        for tag in meta_tags:
            if tag.get("name", "") == "description":
                description = tag.get("content", "")
            elif tag.get("name", "") == "keywords":
                keywords = tag.get("content", "")

        json_data = soup.find("script", type="application/ld+json").string
        parsed_json = json.loads(json_data)
        
        movie_url = parsed_json["url"]
        movie_image = parsed_json["image"]
        movie_description = parsed_json["description"]
        movie_review_body = parsed_json["review"]["reviewBody"]
        movie_review_rating = parsed_json["review"]["reviewRating"]["ratingValue"]
        movie_genre = parsed_json["genre"]
        movie_actors = [actor["name"] for actor in parsed_json["actor"]]
        movie_trailer = parsed_json["trailer"]
        
        output = []
        for result in results:
            name = result.text.replace("\n", " ")
            url = result.find("a")[0].attrs["href"]
            if ("Podcast" not in name) and ("Music Video" not in name):
                try:
                    image = result.xpath("//img")[0].attrs["src"]
                    file_id = url.split("/")[2]
                    output.append({
                        "movie_name": movie_name,
                        "id": file_id,
                        "poster": image,
                        "description": description,
                        "keywords": keywords,
                        "movie_url": movie_url,
                        "movie_image": movie_image,
                        "movie_description": movie_description,
                        "movie_review_body": movie_review_body,
                        "movie_review_rating": movie_review_rating,
                        "movie_genre": movie_genre,
                        "movie_actors": movie_actors,
                        "movie_trailer": movie_trailer,
                        "owner": "@Quartny",
                        "success": True,
                    })
                    return {"results": output}
                except:
                    return {"Success": False}
    
    @staticmethod
    def unsplash(args)->requests.Response:
        """
        Example Usage:
        >>> from Quartny import Ai
        >>> response = Ai.unsplash("boy image")
        >>> print(response)
        """
        url = f'https://www.istockphoto.com/search/2/image?alloweduse=availableforalluses&phrase={args}&sort=best'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://unsplash.com/'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            image_tags = soup.find_all('img')
            image_urls = [img['src'] for img in image_tags if img['src'].startswith('https://media.istockphoto.com')]
            return {"results": image_urls, "owner": "@Quartny", "success": True}
        else:
            return {f"status code: {response.status_code}"}       
    
    @staticmethod
    def pypi(args):
        """
        Example Usage:
        >>> from Quartny import Ai
        >>> package_info = Ai.pypi("requests")
        >>> print(package_info)
        """
        n = base64.b64decode("aHR0cHM6Ly9weXBpLm9yZy9weXBpLw==").decode("utf-8")
        result = requests.get(f"{n}{args}/json").json()["info"]
        return result
    
    
    @staticmethod
    def repo(args):
        """
        Example usage:
        >>> from MukeshAPI import api
        >>> search_results = api.repo("MukeshRobot")
        >>> print(search_results)
        """
        n = base64.b64decode("aHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9zZWFyY2gvcmVwb3NpdG9yaWVzP3E9"
            ).decode("utf-8")
        search_results = requests.get(f"{n}{args}").json()
        items = search_results.get("items", [])
        result = []
        for index, item in enumerate(items, 1):
            result.append((index, item))
        return {"results": result, "owner": "@Quartny", "sucess": True}
    
    @staticmethod
    def github(args):
        """
        Example Usage:
        >>> from Quartny import Ai
        >>> search_results = Ai.github("noob-mukesh")
        >>> print(search_results)
        """
        n = base64.b64decode("aHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy8=").decode("utf-8")
        result = requests.get(f"{n}{args}").json()
        url = result["html_url"]
        name = result["name"]
        id = result["id"]
        company = result["company"]
        bio = result["bio"]
        pattern = "[a-zA-Z]+"
        created_at = result["created_at"]
        created = re.sub(pattern, " ", created_at)
        updated_at = result["updated_at"]
        updated = re.sub(pattern, " ", updated_at)
        avatar_url = f"https://avatars.githubusercontent.com/u/{id}"
        blog = result["blog"]
        location = result["location"]
        repositories = result["public_repos"]
        followers = result["followers"]
        following = result["following"]
        results = {
            "url": url,
            "name": name,
            "id": id,
            "company": company,
            "bio": bio,
            "created at": created,
            "updated at": updated,
            "Profile image": avatar_url,
            "blog": blog,
            "location": location,
            "repos": repositories,
            "followers": followers,
            "following": following,
        }
        return results
    
    @staticmethod
    def meme():
        """
        Example Usage:
        >>> from Quartny import Ai
        >>> search_results = Ai.meme()
        >>> print(search_results)
        """
        n = base64.b64decode("aHR0cHM6Ly9tZW1lLWFwaS5jb20vZ2ltbWU=").decode("utf-8")
        res = requests.get(f"{n}").json()
        title = res["title"]
        url = res["url"]
        results = {"title": title, "url": url}
        return results
    
    @staticmethod
    def weather(city: str):
        """
        Example Usage:
        >>> from Quartny import Ai
        >>> weather_data = Ai.weather("Bihar")
        >>> print(weather_data)
        """
        url=m("aHR0cHM6Ly93ZWF0aGVyeGFwaS5kZW5vLmRldi93ZWF0aGVyP2NpdHk9").decode("utf-8")
        results=requests.get(f"{url}{city}")
        return results.json() 
    
Ai: Quartny = Quartny()
