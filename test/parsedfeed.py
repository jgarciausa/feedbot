import feedparser
from feedparser import FeedParserDict

PARSED_FEED_304: FeedParserDict = FeedParserDict()
PARSED_FEED_304['status'] = 304
PARSED_FEED_304['feed'] = {}
PARSED_FEED_304['entries'] = []
PARSED_FEED_304['debug_message'] = ('The feed has not changed since you last checked, so the server sent no '
                                    'data.  This is a feature, not a bug!')

NYT_VALID_RESPONSE_LAST_MODIFIED = 'Tue, 04 Sep 2018 15:23:01 GMT'
NYT_VALID_RESPONSE_ETAG = '"3d7dac85e1976845ada272a608c88458"'
NYT_RESPONSE_HEADER = {'X-GUploader-UploadID': 'AEnB2UpXtvDrrB6uCmzYY_bKw3BVnRvpdMI4DvFGpnHNmPO8tatucj-u-yuIzUkb3rrlx0CQIqap1ldm-X1jr5kwnPcBiak8xQ', 'Expires': 'Tue, 04 Sep 2018 15:27:51 GMT', 'Cache-Control': 'private, max-age=0', 'Last-Modified': NYT_VALID_RESPONSE_LAST_MODIFIED, 'ETag': NYT_VALID_RESPONSE_ETAG, 'x-amz-meta-x-nyt-agent': 'feedgen::generate_single_section', 'Content-Type': 'application/xml; charset=utf-8', 'x-goog-hash': 'crc32c=Hnnjag==', 'x-goog-storage-class': 'MULTI_REGIONAL', 'Accept-Ranges': 'bytes', 'Access-Control-Allow-Origin': '*', 'Access-Control-Expose-Headers': 'Content-Type', 'Server': 'UploadServer', 'Alt-Svc': 'quic=":443"; ma=2592000; v="44,43,39,35"', 'Via': '1.1 varnish', 'x-nyt-gcs-bucket': 'co-prd', 'Content-Length': '39821', 'Date': 'Tue, 04 Sep 2018 15:27:51 GMT', 'Age': '0', 'Connection': 'close', 'X-Served-By': 'cache-iad2134-IAD, cache-jfk8126-JFK', 'X-Cache': 'MISS, MISS', 'X-Cache-Hits': '0, 0', 'X-Timer': 'S1536074871.290754,VS0,VE33', 'Vary': 'Accept-Encoding'}

PARSED_FEED_NYT_200 = feedparser.parse("""<?xml version="1.0"?>
<rss xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:media="http://search.yahoo.com/mrss/" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:nyt="http://www.nytimes.com/namespaces/rss/2.0" version="2.0">
  <channel>
    <title>NYT &gt; New York</title>
    <link>https://www.nytimes.com/section/nyregion?partner=rss&amp;emc=rss</link>
    <atom:link rel="self" type="application/rss+xml" href="http://www.nytimes.com/services/xml/rss/nyt/NYRegion.xml"/>
    <description/>
    <language>en-us</language>
    <copyright>Copyright 2018  The New York Times Company</copyright>
    <lastBuildDate>Tue, 04 Sep 2018 14:55:20 GMT </lastBuildDate>
    <image>
      <title>NYT &gt; New York</title>
      <url>https://static01.nyt.com/images/misc/NYT_logo_rss_250x40.png</url>
      <link>https://www.nytimes.com/section/nyregion?partner=rss&amp;emc=rss</link>
    </image>
    <item>
      <title>Mueller&#x2019;s Office Will Grill Him About Roger Stone. He Will Respond With Comedy.</title>
      <link>https://www.nytimes.com/2018/09/04/nyregion/mueller-investigation-randy-credico-roger-stone.html?partner=rss&amp;emc=rss</link>
      <guid isPermaLink="true">https://www.nytimes.com/2018/09/04/nyregion/mueller-investigation-randy-credico-roger-stone.html</guid>
      <atom:link href="https://www.nytimes.com/2018/09/04/nyregion/mueller-investigation-randy-credico-roger-stone.html?partner=rss&amp;emc=rss" rel="standout"/>
      <media:content url="https://static01.nyt.com/images/2018/08/30/nyregion/00randy01/00randy01-moth.jpg" medium="image" height="151" width="151"/>
      <media:description>Randy Credico, the comedian, left, is set to testify Sept. 7 before a grand jury convened by the special counsel, Robert S. Mueller III. He and his lawyer, Martin Stolar, left the Federal Building in Manhattan last week after being interviewed about his testimony.</media:description>
      <media:credit>Jefferson Siegel</media:credit>
      <description>Randy Credico, a comedian and Mr. Stone&#x2019;s sometime sidekick, is poised to appear before the Mueller grand jury. &#x201C;You got to give that grand jury some comic relief,&#x201D; he says.</description>
      <dc:creator>DANNY HAKIM</dc:creator>
      <pubDate>Tue, 04 Sep 2018 09:00:10 GMT</pubDate>
      <category domain="http://www.nytimes.com/namespaces/keywords/des">Politics and Government</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/des">United States Politics and Government</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/mdes">Comedy and Humor</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/mdes">Jury System</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/mdes">Classified Information and State Secrets</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/mdes">Impersonators and Impressionists (Entertainment)</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/mdes">Telemarketing</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/mdes">Marijuana</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/nyt_org_all">WikiLeaks</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Assange, Julian P</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Credico, Randolph A (1954- )</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Stone, Roger J Jr</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Trump, Donald J</category>
    </item>
    <item>
      <title>Chirlane McCray Endorses Zephyr Teachout in N.Y. Attorney General Race</title>
      <link>https://www.nytimes.com/2018/09/04/nyregion/chirlane-mccray-zephyr-teachout-endorsement.html?partner=rss&amp;emc=rss</link>
      <guid isPermaLink="true">https://www.nytimes.com/2018/09/04/nyregion/chirlane-mccray-zephyr-teachout-endorsement.html</guid>
      <atom:link href="https://www.nytimes.com/2018/09/04/nyregion/chirlane-mccray-zephyr-teachout-endorsement.html?partner=rss&amp;emc=rss" rel="standout"/>
      <media:content url="https://static01.nyt.com/images/2018/09/05/nyregion/05chirlane1/05chirlane1-moth.jpg" medium="image" height="151" width="151"/>
      <media:description>Zephyr Teachout, who is running for state attorney general, has acknowledged that her campaign has ridden a significant wave of support in the past few weeks.</media:description>
      <media:credit>Sara Naomi Lewkowicz for The New York Times</media:credit>
      <description>For Ms. McCray, the wife of Mayor Bill de Blasio, this is her first solo endorsement; the mayor has not endorsed any candidates in statewide races.</description>
      <dc:creator>VIVIAN WANG</dc:creator>
      <pubDate>Tue, 04 Sep 2018 11:27:37 GMT</pubDate>
      <category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Teachout, Zephyr</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">McCray, Chirlane</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">de Blasio, Bill</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">James, Letitia</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/des">Endorsements</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/mdes">Elections, Attorneys General</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/mdes">Race and Ethnicity</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/des">Primaries and Caucuses</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/nyt_org_all">Democratic Party</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">New York State</category>
    </item>
    <item>
      <title>New Yorker Festival Pulls Steve Bannon as Headliner Following High-Profile Dropouts</title>
      <link>https://www.nytimes.com/2018/09/03/arts/bannon-new-yorker-festival-remnick.html?partner=rss&amp;emc=rss</link>
      <guid isPermaLink="true">https://www.nytimes.com/2018/09/03/arts/bannon-new-yorker-festival-remnick.html</guid>
      <atom:link href="https://www.nytimes.com/2018/09/03/arts/bannon-new-yorker-festival-remnick.html?partner=rss&amp;emc=rss" rel="standout"/>
      <media:content url="https://static01.nyt.com/images/2018/09/04/us/04newyorker-print/04newyorker-bannoncanceled-moth.jpg" medium="image" height="151" width="151"/>
      <media:description>Steve Bannon was dropped as a headliner at The New Yorker Festival on Monday evening.</media:description>
      <media:credit>Martin Divisek/EPA, via Shutterstock</media:credit>
      <description>John Mulaney, Jim Carrey and Patton Oswalt were among celebrities who said they would not appear at the festival next month if Stephen K. Bannon remained its headliner.</description>
      <dc:creator>SOPAN DEB and JEREMY W. PETERS</dc:creator>
      <pubDate>Tue, 04 Sep 2018 01:57:13 GMT</pubDate>
      <category domain="http://www.nytimes.com/namespaces/keywords/des">New Yorker Festival</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/nyt_org_all">New Yorker</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Bannon, Stephen K</category>
      <category domain="http://www.nytimes.com/namespaces/keywords/nyt_per">Remnick, David</category>
    </item>
    <item>
      <title>Metropolitan Diary: &#x2018;Almost Magnetically, My Hand Was Drawn Into His&#x2019;</title>
      <link>https://www.nytimes.com/2018/09/03/nyregion/metropolitan-diary.html?partner=rss&amp;emc=rss</link>
      <guid isPermaLink="true">https://www.nytimes.com/2018/09/03/nyregion/metropolitan-diary.html</guid>
      <atom:link rel="standout" href="https://www.nytimes.com/2018/09/03/nyregion/metropolitan-diary.html?partner=rss&amp;emc=rss"/>
      <media:content url="https://static01.nyt.com/images/2018/09/03/nyregion/03diary-parking/03diary-parking-moth.jpg" medium="image" height="151" width="151"/>
      <media:description/>
      <media:credit/>
      <description>Parking tension on West 130th Street, really long nails on the subway and more reader tales from this week&#x2019;s Metropolitan Diary.</description>
      <dc:creator>THE NEW YORK TIMES</dc:creator>
      <pubDate>Tue, 04 Sep 2018 02:22:47 GMT</pubDate>
      <category domain="http://www.nytimes.com/namespaces/keywords/nyt_geo">New York City</category>
    </item>
  </channel>
</rss>""", response_headers=NYT_RESPONSE_HEADER)
PARSED_FEED_NYT_200['status'] = 200
