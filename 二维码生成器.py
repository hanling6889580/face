import qrcode  # µ¼ÈëÄ£¿é  
qr = qrcode.QRCode(  
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10,  
    border=4,  
)  
qr.add_data('https://product.suning.com/0000000000/150654447.html')  
qr.make(fit=True)  
  
img = qr.make_image()  
img.save("E:\\tianchi\\advanceduse.png")
