# coding: utf-8

from wechatarticles import ArticlesAPI
from wechatarticles import tools
import time

if __name__ == '__main__':
    # official_cookie = "pgv_pvid=3553036635; pgv_pvi=9932620800; RK=MraMBGF4Ye; ptcz=d4bfa0b1542a3435fafc1766071dbce95c8052a688d47c80be8a0caca4ea7f80; tvfe_boss_uuid=87f4b1b56369d0c2; o_cookie=1507987308; pac_uid=1_1507987308; XWINDEXGREY=0; ied_qq=o1507987308; ua_id=QHfDIPUaqj3N9Dv3AAAAAPJq_uXNt_ZCW6soPZcdSXk=; mm_lang=zh_CN; iip=0; ts_uid=8725172784; openid2ticket_o-OXh0jjs0m7ixfuItLsNeH48oPo=; pt_sms_phone=186******87; ptui_loginuin=maohuibo@qq.com; rewardsn=; wxtokenkey=777; pgv_si=s3150940160; uuid=1958f60e31e1b62ddc962f1ba9760fb7; rand_info=CAESIFIxp/PZXT3aUZDS+vo1CkeNIMRl5ycsOhl1eGb7ccMT; slave_bizuin=3538019832; data_bizuin=3538019832; bizuin=3538019832; data_ticket=i0CFI+5bk5amig0HJyMsha4gQP27CqzdzsiDCLs3sMErRKZAbtkhc4mouQn2LnJr; slave_sid=ZEcxenNNYjZ4eURib3dqSW5lMFZEU214YjlvcWx1WU9ZYTZZQVJibmM3aXh4SkFuaWd4T0hQc0VFbXFZSUtUeHdwbjgxOWNyeDZ3d3NvUm9SaDhpNVRJR3JZakxiemxBVE9vUG5mMmhPMWY0WklubnNkb0N6WFRETUlyM3JGZGdaMVpZcVBHajZkRFdvdnEz; slave_user=gh_7bffc795a685; xid=5013b8d5a32663ed86ec69546ce06150"
    official_cookie = "appmsglist_action_3538019832=card; bid=9b6319f9-4f3d-4f3e-946f-eee29fc56f0d; ua_id=QHfDIPUaqj3N9Dv3AAAAAPJq_uXNt_ZCW6soPZcdSXk=; mm_lang=zh_CN; ts_uid=7200495880; com_tenpay_nacl_plugin=exist; ts_uid=8725172784; openid2ticket_o-OXh0jjs0m7ixfuItLsNeH48oPo=; bidjs=17ecd30a-6153-464c-8ee6-62ebdc8cb86f; wxuin=00419402942469; wwrtx.i18n_lan=zh; wwrtx.c_gdpr=0; rewardsn=; wxtokenkey=777; cert=OKivvNYjqcXqYaA_ph7ZTlXJxfMipiSo; sig=h01add9c554fbaecb9450043b0af6e8322a60a78f7817005a796fd740632425372f0b79dfab1e9a4987; master_key=4ikDyD7kVjg+OhRSEnrahG7INlDLqAfP9Z6S8tKt/Dg=; uuid=c58ddb1de8e2ed122dc378fcfd774bf6; rand_info=CAESIDUWHoqnb5QG/tk5TePFhLDWDknqGzsuMWFPKvG0enD0; slave_bizuin=3538019832; data_bizuin=3538019832; bizuin=3538019832; data_ticket=kZIb+4+YuSO2ZejBepNpj3cuZvXA6TuqnBx2TSu3NAxqflO59BMgq9vPdLqq1tvr; slave_sid=ejNGQmU3Smt1dEFEaGNFU1czWjZPMnhRQkFDWkVCTEtHRmFaMFJLQ29lOXlPdnFPT2daMTZIMHMyNlg3STd6eTN6STRUc2RWWUNqaUJheXBpT0ZZeG5IS2RYS2k5QXlCN2dNaXV0YkcyWDdwNUJ5eXEyVHNnMlBXcnZBZU1OZkNOblBhRXhBYThqdk9JUnp6; slave_user=gh_7bffc795a685; xid=5d560c5895b865420f8ee03a7345bbcc;";
    token = "1701470307"
    appmsg_token = "1092_uJv9cEZRh2VvBdDHpJZcKfzXgHSe_ak8kzcGnNAUlYoof4lWRyA0Jhq6J5-h0KVunmO1bLz7hF4USpOj"
    wechat_cookie = "rewardsn=; wxtokenkey=777; wxuin=325115960; devicetype=Windows10x64; version=63010097; lang=zh_CN; pass_ticket=KKn8KrnyJhe2/JcU4m3nMH9FjilRQEZ6Gi1ADMhYeirGes036/2EHSnXOYSunAgW; wap_sid2=CLjAg5sBEooBeV9IRERfaFRreUpXTmx1TEs4YzU1aElBRTY5NjZydHJpLXpZaUFfdkpYSVdoUWRfcU55em1JcF9ocjl0QWcycHRDRU1Feko5Nlk2dm9TUUktbDRzZS12VzdEdF9RSDB1RGdLZlV0d3JTbE9pb2VuVUxMYWFMNXhQZXVScllYZmdHQ1dpRVNBQUF+MJnK8f4FOA1AAQ=="

    # 手动输入所有参数
    test = ArticlesAPI(official_cookie=official_cookie,
                       token=token,
                       appmsg_token=appmsg_token,
                       wechat_cookie=wechat_cookie)

    # 自定义爬取，每次爬取5篇以上
    nicknames = ["xiaojunzixun", "gh_3ee21838dcfc", "jdb988", "jfp-jd", "jiancoolman", "gh_b80c83677237"]
    for nn in nicknames:
        time.sleep(2)
        data = test.complete_info(nickname=nn, begin=0, count=5)
        print(len(data))
        # pprint(data)
        for d in data:
            print(d['title'])
            print(d['link'])


    # 自定义从某部分开始爬取，持续爬取，直至爬取失败为止，一次性最多爬取40篇（功能未测试，欢迎尝试）
    # datas = test.continue_info(nickname=nickname, begin=0)

    tools.save_json("test.json", data)
