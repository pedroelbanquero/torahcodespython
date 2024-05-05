# Torah Codes Python- David Ben Zelateh v1.0.10 Equidistant Letter Sequence Python Library

Torah Codes , An understandable Equidistant Letter Sequence, multilanguaje and multithreading bible codes python library . Study the Torah as never before

Use online on [Online version](https://huggingface.co/spaces/vnosri/Torah_Codes)

![image](https://github.com/pedroelbanquero/torahcodespython/assets/60758685/d37b98c3-87d3-4cd2-b42e-d5d5dbc1309c)


![image](https://user-images.githubusercontent.com/60758685/143378238-d73ee93b-7ba6-4093-83ac-a859fa11461a.png)

![image](https://user-images.githubusercontent.com/60758685/213285427-4561bb21-4635-442b-9b44-affae791c47b.png)


![image](https://user-images.githubusercontent.com/60758685/172951901-fc5d60fe-8bb5-4522-b172-4013d16d279b.png)


## Install (System / Debian-based)

```

sudo apt install python3 python3-pip

pip3 install git+https://github.com/pedroelbanquero/torahcodespython

tbc-cli

```


## Install (Venv / Debian-based)

```

sudo apt install python3 python3-pip python3-venv

python3 -m venv ./venv

./venv/bin/pip install git+https://github.com/pedroelbanquero/torahcodespython

./venv/bin/tbc-cli

```


## Usage

`tbc-cli` on terminal if install on system

Run main program

`use conversions`

Load module

`searchnumber x`

Example 

````

conversions> searchnumber 33

Book: joshua
Yahweh, the God of the Father, the Father of Jesus

Book: jonah
The three-year-old is not the religion of the Reich. 

Book: job
From the time of his death, he was delayed in the procession 

Book: lamentations
In it, there is no doubt that the power of the motherfucker is to increase the number of people who are in need of help. 


Book: judges
They are the first two days in the history of the Lord of Hosts.

In the case of a subdivision, a new law applies to the daughter of the one who is still living in the city, and in the case of the Rishon LeZion, there is a plan for the army


Book: IIkings
In the name of the Lord of the Covenant, the Lord of Hosts, Yes, I will speak to the great thunder of the thunder, and I will hear the voice of the Lord

````

Search ELS at x space distance .

`search words`

Convert words to numbers in gematria, sums and executes ELS function over sumatory distances.

## Modules

- Conversions , search and make conversion
   
   - Multihread ELS search

   - XGBOOST sequences ELS search

   - PROBNET sequences ELS search

   - Words to gematria and viceversa

   - Search over the raw books.

- Big Data , Elasticsearch & Kibana Module

- Baphomet Telegram Bot

![image](https://user-images.githubusercontent.com/60758685/143425642-e4178251-70a3-45c3-b695-6f47cdd3841f.png)

 
## Simple use from your Telegram Chat

- Add @Baphomet_telegram_bot on your telegram

Write

`/start`

you are ready !! 


## Equidistant Letter Sequences (ELS)

<br />Witztum, Rips, and Rosenberg (WRR) define an Equidistant Letter Sequence (ELS) as a sequence of letters in the text whose positions - not counting spaces - form an arithmetic progression. That is to say the letters are found at the positions

n, n + d, n + 2d, ..., n + (k - 1)d

WRR define n as the start, d as the skip between letters in the search-term, and k as the length of the ELS. These three parameters uniquely identify the ELS which is denoted (n, d, k).


![image](https://github.com/pedroelbanquero/torahcodespython/assets/60758685/7bd3466e-247f-410e-b6ee-d4bce1157e10)

## Probability of sequence existence

A way to ensure the faith in the method is directly linked to the probability of generate common sense sentences from the ELS algorithm, is not the same search words of 8 digits than 16 inside the same number of characters (each book)

We need to estimate propertly the probability of ELS generated sequences , is normal appears 100 symbols repetly ? , or long sentence describing modern cities ?, how plausible is something ?

Many uninitiated in kabala might think the results are gimmicks or casual . A math indicators will convince the unitiated .

## Probable encoded sentences

- The sencente have a logical estructure and can be True Or False

- The sentence gematria sumatory value respect to the global number of characters need to be smaller than 10, you can adjust the percentege to ensure the results over the random entropy of the data .

- H(n*book_chars) == H(n*Random)



## Torah encoding analisys

- Language symbols

- Geometry

- Gematria

- Symbol Frequency in Holy writings

- Shannon's Entropy

- Functional encoding patterns

- Information density

- Kabala derivations

- Past, Present and Future

- Similar sentences to other antique books


## TorahBibleCodes python module 

- Import module class
```

from torahbiblecodes.resources.func.torah import *


torah = Torah()


```

- Gematria
```
response_ge = torah.gematrix(listform)

response_ge = torah.gematria(options[0].strip())

```

- Els
```
response_els, tvalue = torah.els(bookNumber, gematriaNumber, tracert='false')

```

- Translate
```
text_translate = torah.func_translate('iw', 'en', response_els)

```

## Authors

Citrix

Hecathomb


## License 

Elohim Open Source

