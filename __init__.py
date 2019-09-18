from pdfy import Pypdfy

pypdfy = Pypdfy()
is_image = pypdfy.are_images(['./Martin_vanden_ing MasterThesis_Final_version(1).pdf'], statistics=True)
print(is_image)