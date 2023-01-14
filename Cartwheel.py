#%%
from fileinput import filename
import numpy as np
import matplotlib.pyplot as plt

from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits
from astropy.visualization import make_lupton_rgb


# img1 = get_pkg_data_filename('MF770W\jw02727-o007_t062_miri_f770w_i2d.fits')

# fits.info(img1)
m770 = fits.open('MF770W\jw02727-o007_t062_miri_f770w_i2d.fits')
m1000 = fits.open('MF1000W\jw02727-o007_t062_miri_f1000w_i2d.fits')
m1280 = fits.open('MF1280W\jw02727-o007_t062_miri_f1280w_i2d.fits')
m1800 = fits.open('MF1800W\jw02727-o007_t062_miri_f1800w_i2d.fits')
n90 = fits.open('NF090W\jw02727-o002_t062_nircam_clear-f090w_i2d.fits')
n150 = fits.open('NF150W\jw02727-o002_t062_nircam_clear-f150w_i2d.fits')
n200 = fits.open('NF200W\jw02727-o002_t062_nircam_clear-f200w_i2d.fits')
n277 = fits.open('NF277W\jw02727-o002_t062_nircam_clear-f277w_i2d.fits')
n356 = fits.open('NF356W\jw02727-o002_t062_nircam_clear-f356w_i2d.fits')
n444 = fits.open('NF444W\jw02727-o002_t062_nircam_clear-f444w_i2d.fits')

# Put all raw images in a list for ease of access - Also ordered by wavelength
all_raw = [n90,n150,n200,n277,n356,n444,m770,m1000,m1280,m1800]


# %%
all_data = []
len(all_raw)
for x in range(10):
    all_data.append(all_raw[x][1].data)

print(all_data)
# %%
# order of all minimums and maximums by image list order
# All are set to 0 here, and applied in each relevant cell below
mins = [0,0,0,0,0,0,0,0,0,0]
maxs = [0,0,0,0,0,0,0,0,0,0]

# %%
all_data[0].shape
mins[0] = 0.15
maxs[0] = 1.2

range_val = []
for x in range(90,200):
    range_val.append(x/100)
# plt.hist(all_data[0].flatten(),bins=range_val)
plt.imshow(all_data[0],cmap='gray',vmin=mins[0],vmax=maxs[0])


# %%
all_data[1].shape
mins[1]=0.15
maxs[1]=3

# range_val = []
# for x in range(150,750):
#     range_val.append(x/500)
# plt.hist(all_data[1].flatten(),bins=range_val)
plt.imshow(all_data[1],cmap='gray',vmin=mins[1],vmax=maxs[1])

# %%
all_data[2].shape
mins[2]=0.15 # may be closer to 0.175
maxs[2]=1.65

range_val = []
for x in range(150,200):
    range_val.append(x/100)
# plt.hist(all_data[2].flatten(),bins=range_val)
# plt.axes('off')
plt.imshow(all_data[2],cmap='gray',vmin=mins[2],vmax=maxs[2],aspect='equal')

# %%
all_data[3].shape
mins[3]=0.17
maxs[3]=1.5

range_val = []
for x in range(5,20):
    range_val.append(x/100)
# plt.hist(all_data[3].flatten(),bins=range_val)
plt.imshow(all_data[3],cmap='gray',vmin=mins[3],vmax=maxs[3],aspect='equal')
all_data[3].shape
# %%
all_data[4].shape
mins[4]=0.15
maxs[4]=0.9

range_val = []
for x in range(100,125):
    range_val.append(x/1000)
# plt.hist(all_data[4].flatten(),bins=range_val)
plt.imshow(all_data[4],cmap='gray',vmin=mins[4],vmax=maxs[4],aspect='equal')
all_data[4].shape

# %%
all_data[5].shape
mins[5]=0.32
maxs[5]=0.9

range_val = []
for x in range(300,350):
    range_val.append(x/1000)
# plt.hist(all_data[5].flatten(),bins=range_val)
plt.imshow(all_data[5],cmap='gray',vmin=mins[5],vmax=maxs[5],aspect='equal')
all_data[5].shape

# %%
# 
all_data[6].shape
mins[6]=7.25
maxs[6]=10

# range_val = []
# for x in range(1,1000):
#     range_val.append(x/100)
# plt.hist(all_data[6].flatten(),bins=range_val)
plt.imshow(all_data[6],cmap='gray',vmin=mins[6],vmax=maxs[6],aspect='equal')
all_data[6].shape

# %%
# 
all_data[7].shape
mins[7]=18.5
maxs[7]=21.5

# range_val = []
# for x in range(184,200):
#     range_val.append(x/10)
# plt.hist(all_data[7].flatten(),bins=range_val)
plt.imshow(all_data[7],cmap='gray',vmin=mins[7],vmax=maxs[7],aspect='equal')
all_data[7].shape

# %%
# 
all_data[8].shape
mins[8]=31.6
maxs[8]=36

# range_val = []
# for x in range(315,340):
#     range_val.append(x/10)
# plt.hist(all_data[8].flatten(),bins=range_val)
plt.imshow(all_data[8],cmap='gray',vmin=mins[8],vmax=maxs[8],aspect='equal')
all_data[8].shape
# %%
# 
all_data[9].shape
mins[9]=102.09
maxs[9]=109

# range_val = []
# for x in range(1010,1060):
#     range_val.append(x/10)
# plt.hist(all_data[9].flatten(),bins=range_val)
plt.imshow(all_data[9],cmap='gray',vmin=mins[9],vmax=maxs[9],aspect='equal')
all_data[9].shape
# %%
i = 1
for x in all_data:
    print(i,' ,', x.shape)
    i = i+1

# %%
# print(all_data[1].shape,all_data[2].shape)
qrgb = 3
srgb = 1
img1 = make_lupton_rgb(all_data[5],all_data[4],all_data[3],minimum=[mins[5],mins[4],mins[3]],stretch=srgb,Q=qrgb,filename='Cartwheel_test.jpg')
plt.axis('off')
plt.imshow(img1)

# %%

# print(all_data[1].shape,all_data[2].shape)
qrgb = 1
srgb = 3.5
img2 = make_lupton_rgb(all_data[6],all_data[7],all_data[9],minimum=[mins[6],mins[7],mins[9]],stretch=srgb,Q=qrgb,filename='Cartwheel_test.jpg')
plt.axis('off')
plt.imshow(img2)
# %%
