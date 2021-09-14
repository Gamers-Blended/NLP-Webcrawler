<h1 align='center'>WEB CRAWLER FOR FORBES BUSINESS NEWS</h1>

<p align="center">
A spider that crawls Forbes business news articles
</p>

## Table of Contents
<details open>
<summary>Show/Hide</summary>
<br>

1. [ File Descriptions ](#File_Description)
2. [ Technologies Used ](#Technologies_Used)    
3. [ Overview ](#Overview)
   * [ 1. Webscraping ](#Webscraping)
   * [ 2. Preprocessing ](#Preprocessing) 
4. [ Instructions ](#Instructions)
5. [ Issues ](#Issues)
</details>

## File Descriptions
<details>
<a name="File_Description"></a>
<summary>Show/Hide</summary>
<br>
  
* [`news/spiders`](https://github.com/Gamers-Blended/NLP-Webcrawler/tree/main/news/spiders):
    * `settings.py`: settings for web crawler
    * `utils.py`: list of user agents
    * [`news/spiders`](https://github.com/Gamers-Blended/NLP-Webcrawler/tree/main/news/spiders):
      * `newss.py`: scoure code for web crawler
* [`output`](https://github.com/Gamers-Blended/NLP-Webcrawler/tree/main/output):
    * output txt files go here
* `convert.py`: takes CSV file of scrapped data, remove special characters and generate txt files into `output` folder
* [`Notebook_for_Task_2.ipynb`](https://github.com/Gamers-Blended/NLP-Webcrawler/blob/main/Notebook_for_Task_2.ipynb): notebook that preprocesses a txt file for topic modelling
</details>

## Tecnologies Used:
<details>
<a name="Technologies_Used"></a>
<summary>Show/Hide</summary>
<br>
    
* <strong>Python</strong>
* <strong>NLTK</strong>
* <strong>Scrapy</strong>
</details>
  
<a name="Overview"></a>
## Overview

<a name="Webscraping"></a>
### Part 1: Web crawler crawls all news from www.forbes.com/business
Spider is to scrap all articles till button "More Articles" disappears.
<br>
Save each piece of scrapped article as one `txt` document.

<a name="Preprocessing"></a>
### Part 2: Choose 1 scrapped article which talks about any companies and preprocess it
Do the following pre-processing steps:
- Remove all company names showed in the article
- Regular Expression/Normalization — lowercase the words, remove punctuation and remove numbers
- Tokenization
- Remove stop words 
- Stemming and lemmatization
- Any other pre-processing steps necessary to prepare this input for topic modelling

<a name="Instructions"></a>
## Instructions on Using Web Crawler
1. Open `news/spiders/newss`
2. Modify line 15 for the correct browser and path to `chromedriver.exe`
3. Save the file
4. Open command prompt
5. Change directory to this folder
6. Run `scrapy crawl newss -o "news.csv"`
7. Run `python convert.py` to generate txt files for every srcapped article
8. Requested `txt` files are stored under the `output` folder

<a name="Issues"></a>
## Issues with Web Crawler
- Although the program is able to click through all the "More Articles" buttons,  the crawler is unable to scrap the "un-hidden" article URLs.

- Some articles cannot be converted into txt due to the "?" character its header.
Although `df['header'] = df['header'].replace('?', '', regex=False)` is used in "convert.py"
to remove it, the "?" character could not be removed.  
EG: "Remote-Controlled Labs? Strateos Raises $56 Million To Build Out Its Vision Of Scientific Automation"

- Some articles could not be scraped (error 403) despite using a random USER_AGENT (defined in "utils.py" and "settings.py").  
EG: The World’s Richest Sports Team Owners 2021

- The 'header' txt file is not an article.
