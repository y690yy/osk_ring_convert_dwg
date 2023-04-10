# -*- coding: utf-8 -*-

import os
import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc


def getRhinoFile(_dir):
    pathList = []
    for root, dirs, files in os.walk(_dir, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            path = str(path)
            if path.endswith(".3dm"):
                pathList.append(path)
    return pathList
    

def export_dwg(_dir):
    
    rs.UnselectAllObjects()
    
    
    ### Get Info of currentfile    
    fileName = Rhino.RhinoDoc.ActiveDoc.Name
    
    ### SelectObject
    rs.Command("_-SelLayer Make2d::*")
    
    ### Export DWG
    value0 = "{}_OSK_ring".format(fileName)
    f = "{}\\{}.dwg".format(_dir, value0)
    f = '"' + f + '"'
    
    rs.Command("_-Export {} _Scheme=\"2007 Polylines\" _Enter _Enter".format(f))
    
    rs.UnselectAllObjects()

def open_close(files, result_path):
    for f in files:
        f = '"' + f + '"'
        rs.Command('_-Open {}'.format(f))
        #rs.Command("_-purge _Enter")
        
        rs.UnselectAllObjects()
        
        export_dwg(result_path)
        
        rs.UnselectAllObjects()
        
        
        rs.Command("_Save")

sc.doc = Rhino.RhinoDoc.ActiveDoc

#FolderLocation
mydir = rs.BrowseForFolder(None,"Sel Folder (SRC / 3dm)")

result_path = rs.BrowseForFolder(None,"Sel Folder (DWG)")
print(result_path)

### Init
rs.Command("-New \"Large Objects - Millimeters.3dm\"")

### Loop
files = getRhinoFile(mydir)

open_close(files, result_path)

### Init
rs.Command("-New \"Large Objects - Millimeters.3dm\"")
print("Complete_Open_Close!!!!!!!!!!!!")