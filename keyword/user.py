import re
from bs4 import BeautifulSoup


def function():
    html = '<div id="botstuff"><div data-ved="2ahUKEwj0rOaKhPPsAhWWu54KHeQsBIE4HhAIegQIBBAv"><div id="bres"></div><div class="med"><h2 class="Uo8X3b">关于过滤结果的声明</h2><div class="card-section"><p id="ofr"><i> 为了向您显示相关程度最高的结果，我们省略了一些与已显示的 33 条结果极为相似的条目。<br>如有需要，您可以<a href="/search?q=site:onion.city&amp;newwindow=1&amp;client=firefox-b-d&amp;sxsrf=ALeKk03R2BAZI3vL0WzbHTy8IkXCXHXUxQ:1604841396353&amp;filter=0">重新搜索以显示省略的结果</a>。 </i></p></div><div class="card-section"><div class="a1DBFd"><i data-hveid="CAQQMA"> 依照其他人根据美国的《数字千年版权法案》(DMCA) 向我们提交的投诉，我们从该页面中移除了 1 条搜索结果。如有需要，您可以前往 <span>LumenDatabase.org</span>，查看导致搜索结果遭到移除的 <a href="http://www.chillingeffects.org/notice.cgi?sID=11130466" onmousedown="return rwt(this,'','','','',"AOvVaw279Q4kRuTgxuvI8kNyrxVC",'',"ahUKEwj0rOaKhPPsAhWWu54KHeQsBIE4HhC_FXoECAQQMQ",'','',event)">DMCA 投诉</a>。  </i></div></div></div></div></div>'
    htmlo = '<div id="botstuff"><div data-ved="2ahUKEwj0rOaKhPPsAhWWu54KHeQsBIE4HhAIegQIBBAv"></div>'

    list = BeautifulSoup(html, 'html.parser').find(id='botstuff').find_all(class_='card-section')
    listo = BeautifulSoup(htmlo, 'html.parser').find(id='botstuff').find_all(class_='card-section')

    print(len(list) == 0)
    print(len(listo) == 0)


if __name__ == '__main__':
    function()
