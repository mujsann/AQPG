from src.segmentation import Segmentation
from src.extraction import Extraction
from src.data.entities import Story, Entities

a = Segmentation(Story, Entities).create()
print("\n \n \n Extraction...")
Extraction(a).create()


