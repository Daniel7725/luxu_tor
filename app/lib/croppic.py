import Image

def toSqu(tmp_img):
	tmp_width,tmp_high = tmp_img.size
	print tmp_width,tmp_high
	if tmp_width > tmp_high:
		tmp_size = tmp_high
		a = int((float(tmp_width)/2-float(tmp_size)/2))
		print "a:"+str(a)
		bound = (a,0,a+tmp_size,tmp_size)
		return tmp_img.crop(bound)
	else:
		tmp_size = tmp_width
		a = int((float(tmp_high)/2-float(tmp_size)/2))
		print "a:"+str(a)
		bound = (0,a,tmp_size,a+tmp_size)
		return tmp_img.crop(bound)

def main():
	path = "/Users/Daniel/Pictures/cai.jpg"
	im = Image.open(path)
	cutIm = toSqu(im)
	cutIm.save("/Users/Daniel/Pictures/c.jpg")

if __name__ == '__main__':
	main()
