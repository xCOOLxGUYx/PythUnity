from PythUnity.Classes import Object
from PythUnity.Classes import String
from PythUnity.Classes import Rect
from PythUnity.Classes import Button
from PythUnity.Classes import RenderOptions
from PythUnity.Functions import AddPrefab
from PythUnity.Functions import GetPrefab
from PythUnity.Functions import GetFonts
from PythUnity.main import init
from PythUnity.help import help
import PythUnity.Variables
from pygame import image
from pygame import Surface
from pygame import font
v = Variables.var

del Variables
__load = image.load
def __im(fileDest, colorKey=(255, 0, 255)): 
  errMessage = "in PythUnity.image.load(\"Image.png\", colorKey) "
  if(type(colorKey) is not tuple):
    PythUnity.Functions.Err(errMessage + "colorKey must be a tuple")
  elif(len(colorKey) != 3):
    PythUnity.Functions.Err(errMessage + "colorKey must have a length of 3 in RGB format")
  image = __load(fileDest)
  image.set_colorkey(colorKey)
  return image
image.load = __im
