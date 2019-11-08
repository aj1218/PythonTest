# #coding=utf-8
# from PIL import Image
# from util.ShowapiRequest import ShowapiRequest
# import time
# class GetCode:
#     def __init__(self,driver):
#         self.driver=driver  #进行赋值
#     # 获取图片
#     def get_code_image(self,file_name):
#         self.driver.save_screenshot(file_name)  # 保存整个网页的图片
#         code_element = self.driver.find_element_by_id("getcode_num")  # 得到图片的id获取
#         left = code_element.location['x']  # 得到左边的那个点  通过.loaction
#         top = code_element.location['y']  # 获取右边的这个点
#         rigth = code_element.size['width'] + left  # 计算宽度 通过.size
#         height = code_element.size['height'] + top  # 计算长度
#         im = Image.open(file_name)
#         img = im.crop((left, top, rigth, height))
#         img.save(file_name)
#         time.sleep(5)
#
#     # 解析图片获取验证码
#     def code_online(self,file_name):
#         self.get_code_image(file_name)#调用的目的就是为了存储这个图片
#         r = ShowapiRequest("http://route.showapi.com/184-1", "100565", "ae6dbef63c1d4b82bafd28425ce6a215")
#         r.addFilePara("image", file_name)
#         r.addBodyPara("typeId", "35")
#         r.addBodyPara("convert_to_jpg", "0")
#         res = r.post()
#         # print(res.text)
#         test = res.json()["showapi_res_body"]['Result']
#         time.sleep(5)
#         return test
#
