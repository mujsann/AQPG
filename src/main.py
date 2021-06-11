from src.segmentation import Segmentation
from src.extraction import Extraction
from src.data.entities import Story, Entities

# Calls the segmentation class and passes the story and entities to it
a = Segmentation(Story, Entities).create()
print("\n \n \n Extraction...")
Extraction(a).create()


