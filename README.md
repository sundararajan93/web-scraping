# Web Scraping

Web scraping is a technique to grab the desired contents only from a webpage. I've created three utilities which is helpful to grab all the email ids, all the website urls and images from a webpage

## Prerequisite

For website and email grabbing we don't need a pre-requisite. however for grabbing the images from a site, we require `beautifulsoup` module. we could install the module with below command.

```
pip3 install beautifulsoup4
```

## Usage

### Cloning the repo

```
$ git clone https://github.com/sundararajan93/web-scraping.git
$ cd web-scraping
```

### email grabbing

Email grabbing would grab all the email ids from a webpage. 

![Email Grabbing](https://i.imgur.com/SAiWWMm.png)

### website url grabbing

Website URL grabbing would grab all the URL from a webpage.

![Website Grabbing](https://i.imgur.com/h7drcmR.png)

### Image grabbing

Grabbing images from a webpage is fairly simple utility similar to the email and url grabbing. If we run this app, it would prompt for url. Once you entered the URL of the webpage containing the images, it would grab all the image urls from the webpage and download them inside a folder. The folder would be created using the current timestamp everytime when we run the script

![image grabbing](https://i.imgur.com/0DOmgux.png)
![image grabbing](https://i.imgur.com/SnzdGwa.png)
