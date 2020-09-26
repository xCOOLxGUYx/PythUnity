Mouse position does not update when dragging so scrolling with dragging isnt possible :(

#Documentation#
Classes.Object types instantiate with
(rect, image, onClick = None, onDrag = None, onClickOff = None, enableDragOff = False)
the image parameter can be a "pygame.image, color i.e (255, 0, 255), and a Classes.String"

Classes.String types instatiate with (text, fontSize, font, fontColor, backgroundColor)
an example for font would be "freesansbold"

#EXAMPLES############
#Add color rectangle#
Important.Functions.AddObject(Important.Classes.Object(pygame.Rect(100, 200, 100, 200), (255, 0, 0)))

#Add Text#
text = Important.Classes.String("TEST TEXT", 36, "freesansbold", (0, 255, 0), (0, 0, 255))
  Important.Functions.AddObject(Important.Classes.Object(pygame.Rect(0, 0, 100, 200), text))#Prints text

#Add Image#
dvdLogo = pygame.image.load("IMAGE FILEPATH")
Important.Functions.AddObject(Classes.Object(pygame.Rect(0, 0, 500, 500), dvdLogo))

#Prints all fonts#
Important.Functions.PrintFonts()

#Change Order in Layer#
Variables.parts[0].Move(5)

#Change Parent#
Variables.parts[1].SetParent(Variables.parts[0])

#Copy#
newCopy = Variables.parts[0].Copy()

#Set And Get Prefab#
Functions.AddPrefab("TestPrefab", Variables.parts[0])
newObject = Functions.GetPrefab("TestPrefab")
newObject.rect.top = 200

#Get Children Of Parent#
children = Variables.parts[0].GetParentChildren()

#Destroy Object#
Variables.parts[0].Destroy()

#Add Component#
Variables.parts[0].AddComp((StartFunc, UpdateFunc))

#Get All Decendants#
Variables.parts[0].Decendants()
