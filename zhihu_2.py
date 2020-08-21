import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/api/v4/questions/19767285/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=5&platform=desktop&sort_by=default'

headers={
	'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
	'cookie':'_zap=773ed82e-942d-4e0d-b9c3-2f0146dc2e0a; d_c0="AHDbCz7cLhGPTmF6i0FBK7BQklmPjdFeu8E=|1587982519"; _ga=GA1.2.80672341.1587982520; _xsrf=Vw7VAkhOdYnEiYYi1mXlqFxfn1cqHycp; q_c1=3fd4c062fcd141a59d983ac45fbebbb2|1590568262000|1590568262000; capsion_ticket="2|1:0|10:1591008528|14:capsion_ticket|44:ZDUwNDBjNzYwM2FlNDBhMDg1NDFhNzJmZGIyYTQ3NjY=|4af7790552519a168538e6916926bfc3d0f7256a16baa5e92a8a84357549e908"; z_c0="2|1:0|10:1591008735|4:z_c0|92:Mi4xOWRJaUJRQUFBQUFBY05zTFB0d3VFU1lBQUFCZ0FsVk4zeXZDWHdEUjl2YXNFaVlxWm9mWXRXd3hkczNKeE1kQTRB|fba5e99077d29750716214f4d9a6edac5316c813b76b7906740b402c0492a5b7"; tst=f; _gid=GA1.2.1000229683.1591603791; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1591377552,1591377572,1591603790,1591676148; SESSIONID=WfKWHfsakWKEiVmEPTeJFmTM22LCYbjW7BHmGyANPfK; JOID=UlgQAEgGGrShSfuFcQUZrVkbHuNlUXn59gKd8xZuTfriIK7oMfQVbfxK_oZ3Z6T9KQsevPbIaeJl_xa7IGImaJc=; osd=Wl0VCkoOH7GrS_OAdA8bpVweFOFtVHzz9AqY9hxsRf_nKqzgNPEfb_RP-4x1b6H4IwkWufPCa-pg-hy5KGcjYpU=; _gat_gtag_UA_149949619_1=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1591676294; KLBRSID=e42bab774ac0012482937540873c03cf|1591676306|1591676149'
}

requests.get(url,headers=headers)
print(requests.status_code)