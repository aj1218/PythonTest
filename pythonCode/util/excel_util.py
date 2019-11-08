#coding=utf-8
#操作excel的文件
import xlrd
from xlutils.copy import copy  #讲excel里面的数据复制一份  然后在实际结果里面写一下   对整个结果进行保留
class ExcelUtil:
    def __init__(self,excel_path=None,index=None):
        if excel_path==None:
            self.excel_path=r"D:\pythonCode\congif\codedata.xls"
        else:
            self.excel_path=excel_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]
        # #行数
        # self.rows=self.table.nrows

        #获取excel数据 按照每一行的一个list 添加到一个大的list里面
    def get_data(self):
        result=[]
        row=self.get_lines()
        if row!=None:
            for i in range(self.get_lines()):
                col = self.table.row_values(i)
                # print(col)
                result.append(col)
            return result
        return None


      #获取excel行数
    def get_lines(self):
         # 行数
         rows = self.table.nrows
         if rows>=1:
             return rows
         return None


    #获取单元格数据
    def get_col_value(self,row,col):
       # print()
        if self.get_lines()>row:
            data=self.table.cell(row,col).value
            return data
        return None

    #判断行数
    def has_next(self):   #行数大于0的时候才返回  如果不大于  就不返回
        pass
    #写入数据
    def write_value(self,row,value):
        read_value=xlrd.open_workbook(self.excel_path)  #整个excel得数据  要拿到数据
        write_data=copy(read_value)#将整个excel的数据复制
        write_data.get_sheet(0).write(row,9,value) #写入的数据行数
        write_data.save(self.excel_path)#在运行的时候不能打开excel   不然就会报错   保存



if __name__ =='__main__':
    ex=ExcelUtil("D:\pythonCode\congif\keyword.xls")
    print(ex.write_value(7,'test'))
