# Usage: python3 -I tools/photos.py titles.txt photos.json
# titles.txt: one English Wikipedia article title per line. Writes {title: {img, page, artist, license, licenseUrl, wiki}}
# for each article whose lead image is freely licensed on Wikimedia Commons. Batches 40 titles per request and backs off on 429s.

import json, sys, urllib.request, urllib.parse, re, html, time
UA={"User-Agent":"holiday-planner/1.0 (personal holiday page)"}
def get(url, params):
    for i in range(5):
        try:
            u=url+"?"+urllib.parse.urlencode(params)
            return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))
        except urllib.error.HTTPError as e:
            if e.code==429: time.sleep(10*(i+1)); continue
            raise
titles=[l.strip() for l in open(sys.argv[1]) if l.strip()]
back={}; allpages=[]
for n in range(0,len(titles),40):
    r=get("https://en.wikipedia.org/w/api.php",{"action":"query","titles":"|".join(titles[n:n+40]),"prop":"pageimages|info","piprop":"name","inprop":"url","redirects":1,"format":"json"})
    q=r["query"]
    for k in ("normalized","redirects"):
        for x in q.get(k,[]): back[x["to"]]=back.get(x["from"],x["from"])
    allpages+=list(q["pages"].values()); time.sleep(2)
pages={}
for pg in allpages:
    orig=back.get(pg["title"],pg["title"])
    if "pageimage" in pg: pages[orig]=(pg["pageimage"],pg["fullurl"])
files=["File:"+v[0] for v in pages.values()]
time.sleep(2)
cn={}; cpages=[]
for n in range(0,len(files),40):
    c=get("https://commons.wikimedia.org/w/api.php",{"action":"query","titles":"|".join(files[n:n+40]),"prop":"imageinfo","iiprop":"url|extmetadata","iiurlwidth":800,"format":"json"})
    cq=c["query"]; cn.update({x["to"]:x["from"] for x in cq.get("normalized",[])}); cpages+=list(cq["pages"].values()); time.sleep(2)
info={}
strip=lambda s: re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>","",s or ""))).strip()
for cp in cpages:
    if "imageinfo" not in cp: continue
    ii=cp["imageinfo"][0]; m=ii.get("extmetadata",{})
    info[cp["title"]]={"img":ii["thumburl"],"page":ii["descriptionurl"],"artist":strip(m.get("Artist",{}).get("value")) or "Unknown","license":strip(m.get("LicenseShortName",{}).get("value")),"licenseUrl":m.get("LicenseUrl",{}).get("value","")}
out={}
for t in titles:
    if t not in pages: print(t,"-> none",file=sys.stderr); continue
    f="File:"+pages[t][0]; f=f.replace("_"," ")
    i=info.get(f) or info.get(cn.get(f,f))
    if not i: print(t,"-> not commons",file=sys.stderr); continue
    i=dict(i, wiki=pages[t][1]); out[t]=i
    print(t,"->",i["license"],"|",i["artist"][:40],file=sys.stderr)
json.dump(out,open(sys.argv[2],"w"),indent=1)
