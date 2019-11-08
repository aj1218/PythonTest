#coding=utf-8
#运行所有case   命名的时候不能运用Python里面的关键字 不然就会报错
from util.excel_util import ExcelUtil
from keywordSelenium.actionMethod import ActionMethod
class KeywordCase:
    def run_main(self): #运行的主入口
        self.action_method=ActionMethod()#实例化
        handle_excel=ExcelUtil(r"D:\pythonCode\congif\keyword.xls")
        case_lines=handle_excel.get_lines()#所有行数
        if case_lines:
            for i in range(1,case_lines):#不能从零开始   因为那一行没有数据 就是很简答的列名
                # handle_excel.write_value(i,'test')
                # continue
                is_run=handle_excel.get_col_value(i,3)#获取数据  单元格的数据 传行号和列号
                if  is_run == "yes": #如果是yes就执行   拿下面的数据
                    method=handle_excel.get_col_value(i,4) #拿到这一行的数据  执行方法
                    print(method)
                    send_value=handle_excel.get_col_value(i,5) #拿到输入数据
                    print(send_value)
                    handle_value=handle_excel.get_col_value(i,6) #拿到操作数据
                    except_rusult_method=handle_excel.get_col_value(i,7)
                    except_rusult=handle_excel.get_col_value(i,8)#可能这个数据是空的   要经过''判断而不是None判断

                    print(handle_value)
                    #if send_value:
                    self.run_method(method,send_value,handle_value) #思路 low代码
                    if except_rusult != '': #不等于空的时候先获取他的值
                        except_value=self.get_except_result_value(except_rusult)
                        if except_value[0] == 'text':
                            print('12345678'+except_rusult_method)
                            print("<------>",except_rusult_method)
                            result=self.run_method(except_rusult_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_rusult_method,except_value[1])
                            if result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        else:
                            print("没有else")
                    else:
                        print("预期结果为空")


                        # getattr(action_method,method) #拿到方法和对象  但是没有执行



#获取预期结果值
    def get_except_result_value(self,data):
        return  data.split('=') #按照等号分割

    def run_method(self,method,send_value = '',handle_value = ''): #传一个输入的 操作的数据
        print(send_value,"=======",handle_value)
        method_value=getattr(self.action_method,method) #拿到方法和对象  但是没有执行 不是一个具体的函数 是一个对象
        if send_value == '' and handle_value!= '':    #判断 send_method是否为空
            result =method_value(handle_value)#传进去就可以执行
        elif send_value=='' and handle_value == '':
            result =method_value() #执行操作元素
        elif send_value != ''and handle_value =='':
            result =method_value(send_value)
        else:
            result =method_value(send_value,handle_value)
        return result
if __name__ == '__main__':
    key=KeywordCase()
    key.run_main()

