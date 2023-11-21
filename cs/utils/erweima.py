import qrcode
# 生成二维码
img = qrcode.make(data="http://101.42.17.126:8000/")
# 将二维码保存为图片
with open('test.png', 'wb') as f:
    img.save(f)
