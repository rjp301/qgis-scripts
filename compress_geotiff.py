import os
layer = iface.activeLayer()

extent = layer.extent()
width,height = layer.width(),layer.height()
renderer = layer.renderer()
provider = layer.dataProvider()

fname = provider.dataSourceUri()
print(fname)
path,name = os.path.split(fname)

name = layer.name()
fname = os.path.join(path,f"{name}_compressed.tif")

pipe = QgsRasterPipe()
pipe.set(provider.clone())
pipe.set(renderer.clone())

opts = ["COMPRESS=JPEG"]

file_writer = QgsRasterFileWriter(fname)
file_writer.setCreateOptions(opts)
file_writer.writeRaster(pipe,width,height,extent,layer.crs())