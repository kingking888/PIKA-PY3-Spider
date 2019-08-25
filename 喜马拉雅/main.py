from ssfs import main_menu
from html import http_head,music_search,music_gettit,music_albums,music_downlo

http_selt=main_menu()
http_html=music_search(http_selt,http_head)
http_urlt=music_gettit(http_html)
http_urlf=music_albums(http_html)
http_rult=music_downlo(http_urlf,http_urlt)