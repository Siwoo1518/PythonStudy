import qrcode

qr_date = 'http://WWW.naver.com'
qr_img = qrcode.make(qr_date)

save_path = 'myqr.png'
qr_img.save(save_path)