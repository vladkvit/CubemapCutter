from PIL import Image #Actually Pillow.
import sys

inp_str = 'CubemapCross'
inp_ext = 'png'

im = Image.open( inp_str + '.' + inp_ext )

in_sz = im.size #width, height

#initializing indeces
ind_large = 0
ind_small = 0
if( in_sz[0] > in_sz[1] ):
	ind_large = 0
	ind_small = 1
else:
	ind_large = 1
	ind_small = 0

assert( in_sz[ind_large] / 4 == in_sz[ind_small] / 3 )

cube_len = in_sz[ind_large] / 4

#slice up the image. First index is X, second index is Y
slices = [[ [Image.new( 'RGB', (cube_len, cube_len)), 0] \
					for x in xrange(in_sz[1] / cube_len)] \
					for x in xrange(in_sz[0] / cube_len)] 
slices_data = [[ 0 for x in xrange(in_sz[1] / cube_len)] for x in xrange(in_sz[0] / cube_len)] 

for i in range(len( slices )):
	for j in range( len(slices[i])):
		slices[i][j][0] = im.crop( (i*cube_len, j*cube_len, (i+1)*cube_len, (j+1)*cube_len ))

for i in range(len( slices )):
	for j in range( len(slices[i])):
		tmp_color = slices[i][j][0].getpixel( (0, 0) )
		for pixel in slices[i][j][0].getdata():
			if( pixel != tmp_color ):
				slices[i][j][1] = 1
				break

for i in range(len( slices )):
	for j in range( len(slices[i])):
		if( slices[i][j][1] != 0 ):
			slices[i][j][0].save( (str(i) + str(j) + '.png'), 'PNG' )


print( 'Done' )