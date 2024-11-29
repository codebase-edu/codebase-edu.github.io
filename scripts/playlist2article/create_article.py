from datetime import datetime
from unidecode import unidecode


import re

    # print(f"Title: {video['title']}")
    # print(f"Permalink: {video['permalink']}")
    # # print(f"Categories: {video['categories']}")
    # # print(f"Summary: {video['summary']}")
    # print(f"Iframe URL: {video['iframe_url']}")
    # print(f"Link: {video['url']}\n")
class Article:
    def __init__(self, data_json):
        self.title_vi = data_json['title']

        self.title = self.title_vi
        self.title = self.title.replace(':', '-') # Markdown does not allow ':' in title

        self.date = '2024-11-05 23:09:00'
        self.permalink = ''
        self.summary = data_json['summary']
        self.iframe_url = data_json['iframe_url']
        self.video_url = data_json['url']

    def create_article(self):
        """
        Generates a Markdown blog post using the provided data_json.
        Args:
            data_json (dict): Contains keys like title, title2, date, permalink, sidebar, mathjax, tags, categories, img, summary, iframe_url.
        Returns:
            str: The generated article as a string.
        """
        # Convert date to the desired format
        
        # Template for the article
        article_template = f"""---
layout: post
comments: true
title:  {self.title}
title2:  {self.title}
date:   {self.date}
permalink: {self.permalink}
sidebar: c_basic_sidebar
mathjax: true
tags: C++ C++-cơ-bản
categories: C++-Basic
# sc_project: 11213301
# sc_security: 8d50f6a5
img: /assets/cpp/cpp-programming-400x250.png
summary: {self.title} - Các bạn nhớ đăng kí kênh để nhận nhiều video hữu ích nhé. http://bit.ly/kenhDTLT. Fan page chính thức và duy nhất của kênh https://www.facebook.com/kenhDTLT
---

<iframe width="560" height="315" src="{self.iframe_url}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
"""
        return article_template


    def no_accent_vietnamese(s):
        s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
        s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
        s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
        s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
        s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
        s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
        s = re.sub(r'[ìíịỉĩ]', 'i', s)
        s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
        s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
        s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
        s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
        s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
        s = re.sub(r'[Đ]', 'D', s)
        s = re.sub(r'[đ]', 'd', s)
        print('no_accent_vietnamese result: ' + s)
        return s

    def make_article_permanent_link_from_video_title(video_title):
        # c-basic-19-vong-lap-for
        article_title_unidecode = Article.no_accent_vietnamese(video_title)
        article_number = Article.extract_numbers(article_title_unidecode)

        if " - " in article_title_unidecode:
            article_parts = article_title_unidecode.split(" - ")
            article_2nd_part = article_parts[1]
        elif ": " in article_title_unidecode:
            article_parts = article_title_unidecode.split(": ")
            article_2nd_part = article_parts[1]
        else:
            article_2nd_part = article_title_unidecode

        article_title = f'c-basic-{article_number}-{article_2nd_part}'
        article_title = article_title.replace(' ', '-')
        print('make_article_permanent_link_from_video_title: ' + article_title)
        return article_title

    def extract_numbers(text):
        # Use regex to find all numbers in the text
        numbers = re.findall(r'\d+', text)
        # Convert the numbers to integers (optional)
        return numbers[0]


    # # Example data to generate the article
    # article_data = {
    #     "title": "Lập trình C Cơ bản 01 - Lý do nên học và ứng dụng của ngôn ngữ C/C++ trong thực tế",
    #     "title2": "Lập trình C Cơ bản 01 - Lý do nên học và ứng dụng của ngôn ngữ C/C++ trong thực tế",
    #     "date": "2024-11-05 23:09:00",
    #     "permalink": "/cpp-basic-20-.html",
    #     "sidebar": "c_basic_sidebar",
    #     "mathjax": "true",
    #     "tags": "C++ C++-cơ-bản",
    #     "categories": "C++-Basic",
    #     "img": "/assets/cpp/cpp-programming-400x250.png",
    #     "summary": "Hướng dẫn cài đặt bộ công cụ để học lập trình C++",
    #     "iframe_url": "https://www.youtube.com/embed/bQV5l1RLc7U?si=iaSfOorQIG9QrE6i",
    # }

    # Generate the article

    # article = create_article(article_data)

    def save_article_to_file(file_name, article):
        print(f'save_article_to_file name: {file_name}, data: {article}')
        # article_file_name = Article.no_accent_vietnamese(article.title)
        
        print('Save the article to a file')
        try:
            with open(f"{file_name}.md", "w+", encoding="utf-8") as file:
                file.write(article)
        except FileNotFoundError:
            print("The specified file was not found.")
        except IOError:
            print("An I/O error occurred while handling the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Article generated successfully!")

    def add_to_side_bar(self):
        _side_bar_title = self.title_vi
        title_num = Article.extract_numbers(self.title_vi)

        if " - " in _side_bar_title:
            article_parts = _side_bar_title.split(" - ")
            article_2nd_part = article_parts[1]
        elif ": " in _side_bar_title:
            article_parts = _side_bar_title.split(": ")
            article_2nd_part = article_parts[1]
        else:
            article_2nd_part = _side_bar_title

        sidebar_template = f"""
    - title: {title_num}.{article_2nd_part}
      url: /{self.permalink}
      output: web, pdf
"""
        print('Append the hyperlink to a sidebar')
        try:
            with open(f"c_basic_sibar.md", "a+", encoding="utf-8") as file:
                file.write(sidebar_template)
        except FileNotFoundError:
            print("The specified file was not found.")
        except IOError:
            print("An I/O error occurred while handling the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Article generated successfully!")


    def add_to_introduction_page(self):
        course_num = Article.extract_numbers(self.title_vi)

        if " - " in self.title_vi:
            article_parts = self.title_vi.split(" - ")
            course_vietnamese_title = article_parts[1]
        elif ": " in self.title_vi:
            article_parts = self.title_vi.split(": ")
            course_vietnamese_title = article_parts[1]
        else:
            course_vietnamese_title = self.title_vi
        # Lập trình C bài 08. Hiểu rõ về mảng | [Hiểu rõ về mảng?](/cpp-basic-08-hieu-ro-ve-mang.html){:target="_blank"} | [Youtube](https://www.youtube.com/watch?v=bQV5l1RLc7U){:target="_blank"}|
        course_table_list_template = f"""
Lập trình C bài {course_num}. {course_vietnamese_title} | [{course_vietnamese_title}]({self.permalink}){{target="_blank"}} | [Youtube]({self.video_url}){{target="_blank"}} |
"""


        print('Append the course to introduction page')
        try:
            with open(f"c_introduction_page.md", "a+", encoding="utf-8") as file:
                file.write(course_table_list_template)
        except FileNotFoundError:
            print("The specified file was not found.")
        except IOError:
            print("An I/O error occurred while handling the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Article generated successfully!")
