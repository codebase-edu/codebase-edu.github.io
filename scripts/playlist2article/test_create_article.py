from create_article import Article

video_title = 'Lập trình C Cơ bản 01 - Lý do nên học ngôn ngữ C/C++ và ứng dụng của C/C++ trong thực tế'


article_title_unidecode = Article.no_accent_vietnamese(video_title)
article_number = Article.extract_numbers(article_title_unidecode)

article_parts = article_title_unidecode.split(" - ")
article_2nd_part = article_parts[1]

article_title = f'c-basic-{article_number}-{article_2nd_part}'


article_title = article_title.replace(' ', '-')
print(article_title)
