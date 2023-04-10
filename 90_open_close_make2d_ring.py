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


def make2d_query(layout="CPlane", props="MaintainSourceLayers", hide_l="Yes", tangent="No", silhouette="No", clip_pl="No", rect="No", group="Yes", name="Make2D"):
    
    q = "_-Make2d L {} P {} C={} S={} R={} E={} H={} G={} A {} Enter".format(layout, props, hide_l, tangent, silhouette, clip_pl, rect, group, name)
    
    return q


def open_close(files):
    for f in files:
        f = '"' + f + '"'
        rs.Command('_-Open {}'.format(f))
        #rs.Command("_-purge _Enter")
        
        rs.UnselectAllObjects()
        
        rs.Command("SelAll")
        
        ### Make2d
        rs.Command(make2d_query())
        
        rs.UnselectAllObjects()
        
        rs.Command("_Save")


###RunScript

sc.doc = Rhino.RhinoDoc.ActiveDoc

#FolderLocation
mydir = rs.BrowseForFolder(None,"Sel Folder")

### Init
rs.Command("-New \"Large Objects - Millimeters.3dm\"")

### Loop
files = getRhinoFile(mydir)
open_close(files)

### Init
rs.Command("-New \"Large Objects - Millimeters.3dm\"")
print("Complete_Open_Close!!!!!!!!!!!!")