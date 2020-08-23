#Ebook de Scrapy

### 1 - Intro Scrapy

Criar um arquivo e faça algo nessa estruta:

 ```py
class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            # response.follow considera o endereço relativo
            yield response.follow(next_page, self.parse 
```
para executar o código

    scrapy runspider my-project.py  

### 2- Iniciar um projeto

    scrapy startproject nome-projeto 

### 3 - Criar um Spider

    scrapy genspider nome-class-spider url-project 

### 4 - Executar o Scrapy modo projeto

    scrapy crawl nome-class-spider 

### 5 - Executar e salvar o arquivo

    scrapy crawl nome-class-spider -o arquivo.formato 

### 6 - Comandos úteis

#### verificar o conteúdo html do elemento seletor
    
    response.get()
    response.extract() 
    response.extract_first()

obs.: Preencher com valor default caso valor não encontrado
    response.get('default')
    response.extract_first('default')
#### Verificar o texto de uma pesquisa xpath

    response.xpath('tag/.text()').extract() ou .extract_first() 

#### Xpath contains

    response.xpath('//tag[contains(@attr, '')]') 
    response.xpath('//tag[contains(text(), 'ipsum')]') 

#### Scrapy shell - aceitar a página em pt-br

```py
from scrapy import Request

req = Request('url', headers={'Accept-Language':'pt-br'})
fetch(req)
# response ativado a partir do fetch
```

#### Scrapy FormResquest
 
```py
from scrapy.http import FormRequest
def start_requests(self):
    url='http://imobiliariabelamorada.com.br/filtro/locacao/\
        apartamentos/pato-branco-pr/?busca=1'
    formdata={
        'cat1': '2.locacao', 
        'cat3': '4.apartamentos', 
        'cidade': '5362.pato-branco-pr', 
        'valor':'', 
        'cod':''
    }
    yield FormRequest(url, callback=self.parse, formdata=formdata, method='POST')
```

#### Alterar o robots.txt na class Spider:
```py
    def start_requests(self):
        
        url = 'https://www.almeidaw.com.br'
        form_data = {
            'cat1': '2.locacao',
        }
        # comando que subscreve ROBOTSTXT_OBEY do settings
        meta = {'dont_obey_robotstxt':'False'}
        yield scrapy.FormRequest(url=url, callback=self.parse, formdata=form_data ,method='POST', meta= meta)

```

#### Start requests completo:
```py

    def start_requests(self):
        
        url = 'https://www.jlo.com/todos/todos/1'

        # headers disponíveis no network
        headers = {
            'Accept': 'text/html,aation/signed-exchange;v=b3;q=9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '77',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '__utmc=226286; __utmz=226LNAD',
            'Host': 'www.jlosso.com.br',
            'Origin': 'https://www.jlosso.com.br',
            'Referer': 'https://www.jlosso.com.br/home',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1'
        }

        # form de request
        form_data = {
            'cat1': '2.locacao',
            'cat3': '4.carros',
            'valormedio': '',
            'codigo': '',
            'cidade': '5166.pato'
        }
        
        # desativa o robots.txt
        meta = {'dont_obey_robotstxt':'False'}

        yield scrapy.FormRequest(
                        url=url,
                        callback=self.parse,
                        formdata=form_data,
                        method='POST',
                        headers= headers,
                        meta= meta
                    )
```

####  FormResquest Shell
exemplo básico de funcionamento:
~~~shell
scrapy shell
~~~

~~~py
url='http://imobiliariabelamorada.com.br/filtro/locacao/ \
    apartamentos/pato-branco-pr/?busca=1'
~~~
 
**Passando form**
~~~py
formdata={
    'cat1': '2.locacao', 
    'cat3': '4.apartamentos', 
    'cidade': '5362.pato-branco-pr', 
    'valor':'', 
    'cod':''
    } 
~~~

~~~py
from scrapy.http import FormRequest
fetch(scrapy.FormRequest(url, formdata=formdata, method='POST'))
~~~

**Passando headers no shell**
~~~shell
scrapy shell -s USER_AGENT='custom user agent' 'http://www.example.com'
~~~
ou dentro do ipython
~~~shell
url = 'http://www.example.com'
request = scrapy.Request(url, headers={'User-Agent': 'Mybot'})
fetch(request)
~~~

**Desativando robots.txt pelo terminal**

Shell
~~~shell
scrapy shell -s ROBOTSTXT_OBEY='False' 'http://www.example.com'
~~~
Crawl
~~~shell
scrapy crawl name-spider -s ROBOTSTXT_OBEY='False'
~~~

#### Avanço de página - next_page
~~~py
        next_page = response.xpath('//a[@data-ix="passar-pagians"]/b/parent::a/following-sibling::a').get()
        if next_page:
            next_url = next_page.xpath('//a/@ref').get()
            # se o href vier com url absoluto usar o scrapy.Request
            yield scrapy.Request(url=next_url, callback=self.parse)
            # se o href vier com url relativa usar o response.follow
            yield response.follow(url=next_url, callback=self.parse)

outra maneira de construir o url absoluto
~~~py   
        from urllib.parse import urljoin
        relative_url = response.xpath('//a[@data-ix="passar-pagians"]/@href').get()
        base_url = 'http://www.imobiliariagralhaazul.com.br'
        absolute_url = urljoin(base_url, next_page)
~~~



#### Execuntando scrapy em html localhost

**Shell**
~~~shell
    scrapy shell local/name/page
~~~
**Server local**
1. Abra o terminal na pasta onde consta o arquivo .html
    ~~~shell
        python -m http.server <port>
    ~~~
    obs.: A porta default é a 8000, porém, você pode alterar inserindo outro número valor

2. Vá até o local host e clique no arquivo.html

3. Executando scrapy localhost
    ~~~shell
        scrapy shell http://0.0.0.0:8000/arquivo.html
    ~~~
    obs.: No caso de genspider
    ~~~shell
        scrapy genspider name localhost
    ~~~

#### DELAY no dowload das páginas
Configurando o arquivo settings.py
~~~py
    # See also autothrottle settings and docs
    DOWNLOAD_DELAY = 3
~~~
ou passando no sheel
~~~shell
    scrapy crawl name-spider -s DOWNLOAD_DELAY = Valor
~~~
Por padrão, o Scrapy não espera um período fixo de tempo entre solicitações, 
mas usa um intervalo aleatório entre 0,5 * DOWNLOAD_DELAY e 1,5 * DOWNLOAD_DELAY.

#### Passar argumento category

~~~shell
    scrapy crawl projeto -a category=nome_elemento
~~~

#### Ajustar o start_request

    Nesse método é onde faz o callback para o parse, caso seja passado algum argumento,
    é necessário fazer a verificação e/ou alteração do resquet.

#### Scrapy command line - List spiders

    scrapy list

#### Lista de pseudo-classes

**Irmão anterior**
        
    preceding-sibling::tag

**Irmão posterior**
*xpath*

    following-sibling::tag

*css*

    i.ga-bedrooms-02 + span


**Pai**
   
    parent::tag

**Pegar tag filha em css**

    tag.class > child

ou

    tag.class  child

**Pegar último filho em css**

    tag:last-child

**Obter text dentro da tag css**

    response.css('mytag::text') -> Obter texto apenas do nó selecionado.
    response.css('mytag ::text') -> Obter texto do nó selecionado e seus nós filhos.

**Pegar atributo href**

    tag::attr(href)

**Pegar último elemento selecionado [last()]**

    response.xpath('//div[@class="row"]/text() [last()]').get()


#### Scrapy mais Splash

**Instalar e configurar o splash**
[github scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash)


**Instalar**
~~~shell
    pip install scrapy-splash
~~~

**Executar docker**
~~~shell
    docker run -p 8050:8050 scrapinghub/splash
~~~

**colocar em settings do spider**
~~~py
SPLASH_URL = 'http://localhost:8050/'
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
 ~~~

**Exemplo de request com splash**
 ~~~py
from scrapy_splash import SplashRequest

def start_requests(self):
    for url in self.start_urls:
        yield SplashRequest(
            url= url,
            callback= self.parse,
            endpoint='render.html',
            args={'wait': 10}
        )
 ~~~

 #### Scrapy mais Selenium

**Instalar e configurar o splash**
[github scrapy-selenium](https://github.com/clemfromspace/scrapy-selenium)


**Instalar**
~~~shell
    pip install scrapy-selenium
~~~

**colocar em settings do spider**
~~~py
from shutil import which

SELENIUM_DRIVER_NAME = 'firefox'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('geckodriver')
SELENIUM_DRIVER_ARGUMENTS=['-headless']  # '--headless' if using chrome instead of firefox
SELENIUM_BROWSER_EXECUTABLE_PATH = which('firefox')

DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}
 ~~~

**Exemplo de request com splash**
 ~~~py
from scrapy_selenium import SeleniumRequest


    def start_requests(self):
        url = self.start_urls[0]
        yield SeleniumRequest(url=url, callback=self.parse, wait_time= 3)
 ~~~


 #### Interpretando robots.txt
 [Guia robots.txt](https://searchengineland.com/a-deeper-look-at-robotstxt-17573#:~:text=The%20hash%20symbol%20(%23)%20may,lines%20or%20end%20of%20lines.)

 **Básico**
    
    User-agent: * [para todo bot]
    Disallow: / [bloquear o site inteiro]

    User-agent: * [para todo bot]
    Disallow: /dir/ [bloquear diretório específico]

    User-agent: Fetch [para o bot fetch]
    Disallow: /private.html [bloquear página específica]

#### Configurando plugin user-agent random
[scrapy-user-agents](https://pypi.org/project/scrapy-user-agents/)

Primeiro é necessário instalar 
~~~shell
    pip install scrapy-user-agents
~~~

e para configurar basta colocar este comando no arquivo settings.py
~~~py
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}
~~~

#### Configurando plugin proxy random
[scrapy_proxy_pool](https://github.com/hyan15/scrapy-proxy-pool)

Primeiro é necessário instalar 
~~~shell
    pip install scrapy_proxy_pool
~~~

e para configurar basta colocar este comando no arquivo settings.py
~~~py
DOWNLOADER_MIDDLEWARES = {
    'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
}
~~~
obs.: Número dos middlewares devem ser inferiores ao do *RandomUserAgentMiddleware*