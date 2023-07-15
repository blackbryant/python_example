#上下文管理器

#範例一、
f = open("aa.txt","r")
data = f.read()
f.close()

# 用with方法使用，如何實現自動關檔案 
# ans: context

with open("aa.txt") as f:
    data = f.read()


class Myfile:
    def __init__(self,filepath) -> None:
        self.filepath = filepath
    def __enter__(self):
        self.fp = open(self.filepath)
        return self.fp
    def __exit__(self,typ,value,trackback):
        self.fp.close()
#執行步驟: with  statement -> __enter__() -> code -> __exit__   
with Myfile("aa.txt") as fn:
    data = fn.read()

#將S9-1Decorator時間執行計算，利用context來改
#context與Decorate的差異






