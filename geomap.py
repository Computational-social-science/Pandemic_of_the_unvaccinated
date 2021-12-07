import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
from matplotlib.gridspec import GridSpec
shapefile = 'bokeh-app/data/countries_110m/ne_110m_admin_0_countries.shp'

#Read shapefile using Geopandas
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]

#Rename columns.
gdf.columns = ['country', 'country_code', 'geometry']
gdf = gdf.drop(gdf.index[159]) #地图宽度

# #Drop row corresponding to 'Antarctica'
# datafile = 'bokeh-app/data/Countries of the world.csv'
datafile = 'bokeh-app/data/country-plot.csv'
data=pd.read_csv(datafile,usecols=[0,1],names=['country','Volume (Sum)(%)'])#导入数据
# data['Volume (Sum)(%)'] = data['Volume (Sum)(%)']/(73.3024)
print(data['Volume (Sum)(%)'])
#Read data to json.
data = gpd.GeoDataFrame(data)
merged = gdf.merge(data,on = 'country',how='left')
#low -> high
colorslist = ['#E3E3E1','#DFDCC6','#585332']
mycmaps = colors.LinearSegmentedColormap.from_list('mylist',colorslist,N=800)

fig,ax = plt.subplots(figsize = (10,6))

merged.plot(
    column = 'Volume (Sum)(%)',
    scheme = 'userdefined',
    classification_kwds = {'bins':[0,0.000005,0.00001,0.00005,0.0001,0.0005,0.001,0.005,0.01,0.05,0.1,0.2,0.3,0.4]},
    cmap = mycmaps,
    edgecolor = 'black',
    linewidth = 0.1,
    ax = ax,
)

# albers_proj = '+proj=aea +lat_1=25 +lat_2=47 +lon_0=105'
# ax = data.to_crs(albers_proj).plot(ax=ax,
#                                     missing_kwds={
#                                         "color": "lightgrey",
#                                         "edgecolor": "black",
#                                         "hatch": "////"
#                                     },
#                                     legend=True,
#                                     scheme='NaturalBreaks',
#                                     k=5)
plt.xlim(-182,182)
plt.ylim(-58,86)

plt.axis('off')  # 去坐标轴

plt.text(-169,-3.2,'High',family = 'Times New Roman',fontsize = 7)
# plt.text(-169,-30.2,r'$20\%$',family = 'Times New Roman',fontsize = 8)
plt.text(-169,-57.2,'Low',family = 'Times New Roman',fontsize = 7)
plt.text(-174.3,-1.9,r'$-$',family = 'Times New Roman',fontsize = 6,color = 'grey')
# plt.text(-174.3,-29.22,r'$-$',family = 'Times New Roman',fontsize = 6,color = 'grey')
plt.text(-174.3,-56.54,r'$-$',family = 'Times New Roman',fontsize = 6,color = 'grey')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

sm = plt.cm.ScalarMappable(cmap=mycmaps)
position=fig.add_axes([0.131, 0.24, 0.015, 0.2005])#位置[左,下,右,上]
cb=plt.colorbar(sm,cax=position,orientation='vertical',drawedges=False)#方向
cb.outline.set_visible(False)
cb.set_ticks([])  # 去x坐标刻度

plt.savefig('picture/result_mycmaps_dpi=150.jpg', bbox_inches='tight', pad_inches = 0,dpi=150)
plt.savefig('picture/result_mycmaps_dpi=150.png', bbox_inches='tight', pad_inches = 0,dpi=150)
plt.savefig('picture/result_mycmaps_dpi=150.tiff', bbox_inches='tight', pad_inches = 0,dpi=150)

fig,ax = plt.subplots(figsize = (10,6))
merged.plot(
    column = 'Volume (Sum)(%)',
    scheme = 'userdefined',
    classification_kwds =
        # {'bins':[0,0.000005,0.00001,0.00005,0.0001,0.0005,0.001,0.005,0.01,0.05,0.1,0.2,0.3,0.4]},#字典型，传入与分层设色相关的个性化参数
        {'bins':[0,0.005,0.01,0.05,0.1,0.5,1,5,10,50,100,200,300,400]},
    cmap = mycmaps,

    edgecolor = 'black',
    linewidth = 0.1,
    ax = ax,
)
plt.xlim(-182,182)
plt.ylim(-58,86)

plt.axis('off')  # 去坐标轴

plt.text(-169,-3.2,'High',family = 'Times New Roman',fontsize = 7)
# plt.text(-169,-30.2,r'$20\%$',family = 'Times New Roman',fontsize = 8)
plt.text(-169,-57.2,'Low',family = 'Times New Roman',fontsize = 7)
plt.text(-174.3,-1.9,r'$-$',family = 'Times New Roman',fontsize = 6,color = 'grey')
# plt.text(-174.3,-29.22,r'$-$',family = 'Times New Roman',fontsize = 6,color = 'grey')
plt.text(-174.3,-56.54,r'$-$',family = 'Times New Roman',fontsize = 6,color = 'grey')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

sm = plt.cm.ScalarMappable(cmap=mycmaps)
position=fig.add_axes([0.131, 0.24, 0.015, 0.2005])#位置[左,下,右,上]
cb=plt.colorbar(sm,cax=position,orientation='vertical',drawedges=False)#方向
cb.outline.set_visible(False)
cb.set_ticks([])

plt.savefig('picture/result_mycmaps_dpi=300.jpg', bbox_inches='tight',pad_inches = 0,dpi=300)
plt.savefig('picture/result_mycmaps_dpi=300.png', bbox_inches='tight', pad_inches = 0,dpi=300)
plt.savefig('picture/result_mycmaps_dpi=300.tiff', bbox_inches='tight', pad_inches = 0,dpi=300)

fig,ax = plt.subplots(figsize = (10,6))
#
merged.plot(
    column = 'Volume (Sum)(%)',
    scheme = 'userdefined',
    classification_kwds = {'bins':[0,0.000005,0.00001,0.00005,0.0001,0.0005,0.001,0.005,0.01,0.05,0.1,0.2,0.3,0.4]},
    cmap = mycmaps,
    edgecolor = 'black',
    linewidth = 0.1,
    ax = ax,
)
plt.xlim(-182,182)
plt.ylim(-58,86)

plt.axis('off')  # 去坐标轴

plt.text(-169,-3.2,'High',family = 'Times New Roman',fontsize = 7)
# plt.text(-169,-30.2,r'$20\%$',family = 'Times New Roman',fontsize = 8)
plt.text(-169,-57.2,'Low',family = 'Times New Roman',fontsize = 7)
plt.text(-174.3,-1.9,r'$-$',family = 'Times New Roman',fontsize = 6,color = 'grey')
# plt.text(-174.3,-29.22,r'$-$',family = 'Times New Roman',fontsize = 6,color = 'grey')
plt.text(-174.3,-56.54,r'$-$',family = 'Times New Roman',fontsize = 6,color = 'grey')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

sm = plt.cm.ScalarMappable(cmap=mycmaps)
position=fig.add_axes([0.131, 0.24, 0.015, 0.2005])#位置[左,下,右,上]
cb=plt.colorbar(sm,cax=position,orientation='vertical',drawedges=False)#方向
cb.outline.set_visible(False)
cb.set_ticks([])

plt.savefig('picture/result_mycmaps_dpi=150.svg', bbox_inches='tight', pad_inches = 0,dpi=150)
plt.savefig('picture/result_mycmaps_dpi=300.svg', bbox_inches='tight', pad_inches = 0,dpi=300)