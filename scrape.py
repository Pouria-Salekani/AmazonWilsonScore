from requests_html import HTMLSession

def getRate(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)


    #This is our simple scraper, just copy xPath from inspect then paste it and follow this format
    data = {
        'total-ratings' : r.html.xpath('//*[@id="cm_cr-product_info"]/div/div[1]/div[3]/span', first=True).text,
        'outof5' : r.html.xpath('//*[@id="cm_cr-product_info"]/div/div[1]/div[2]/div/div/div[2]/div/span', first=True).text
    }

    print(data)

#getRate('https://www.amazon.com/Daisy-Jones-Taylor-Jenkins-Reid/product-reviews/1524798649/?_encoding=UTF8&pd_rd_w=NCCGT&content-id=amzn1.sym.64be5821-f651-4b0b-8dd3-4f9b884f10e5&pf_rd_p=64be5821-f651-4b0b-8dd3-4f9b884f10e5&pf_rd_r=P0CSWMGQD4WBNFV20N16&pd_rd_wg=gfa1J&pd_rd_r=db04e1dc-4f1e-485a-9c91-cd7d3090de03&ref_=pd_gw_crs_zg_bs_283155')