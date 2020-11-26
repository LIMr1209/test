#
# a = '<section style="width: 260px;height: 260px;border-radius: 100%;background-image: url(&quot;https://mmbiz.qpic.cn/mmbiz_jpg/gvZCdf7jzVCNurIFDWmqhcTt3ds0h6S7TDrYDAHQGd3Q7trpXlguetVzLjGRnOvf1YTyVMtL3CbRe1DYniapTwg/640?wx_fmt=jpeg&quot;);background-position: center center;background-size: cover;background-repeat: no-repeat;background-attachment: initial;background-origin: initial;background-clip: initial;"><p class="text-center"><img class="fr-dii fr-draggable" data-type="jpeg" data-width="100%" src="https://p4.taihuoniao.com/topic/201014/5f866660fc5934a64677ff89-hdw.jpg" style="width: 260px; opacity: 0; height: 260px;" title=""></p></section><section style="width: 260px;height: 260px;border-radius: 100%;background-image: url(&quot;https://mmbiz.qpic.cn/mmbiz_jpg/gvZCdf7jzVCNurIFDWmqhcTt3ds0h6S7TDrYDAHQGd3Q7trpXlguetVzLjGRnOvf1YTyVMtL3CbRe1DYniapTwg/640?wx_fmt=jpeg&quot;);background-position: center center;background-size: cover;background-repeat: no-repeat;background-attachment: initial;background-origin: initial;background-clip: initial;"><p class="text-center"><img class="fr-dii fr-draggable" data-type="jpeg" data-width="100%" src="https://p4.taihuoniao.com/topic/201014/5f866660fc5934a64677ff89-hdw.jpg" style="width: 260px; opacity: 0; height: 260px;" title=""></p></section>'
# import re
#
# rex = re.compile('background-image: url\((?P<url>.*?)\)')
#
# def test(matched):
#     b = matched.group("url")
#     b = b.replace('&quot;','')
#     return 'background-image: url(https://p4.taihuoniao.com/topic/201014/5f866660fc5934a64677ff89-hdw.jpg)'
#
# group = rex.sub(test, a)
# print(group)

import re
all_product = Product.objects(channel="yankodesign").all()
for i in all_product:
    date_list = re.findall("/(\d+/\d+/\d+)/", i.url)[0].split("/")
    if int(date_list[0]) <2014:
        i.mark_delete()



