from math import sin, cos, acos, radians

earth_rad = 6378.137

def latlng_to_xyz(lat, lng):
    rlat, rlng = radians(lat), radians(lng)
    coslat = cos(rlat)
    return coslat*cos(rlng), coslat*sin(rlng), sin(rlat)

def dist_on_sphere(pos1,pos2, radious=earth_rad):
    print(str(pos1["lat"])+" : "+str(pos1["lng"]))
    xyz0, xyz1 = latlng_to_xyz(pos1["lat"],pos1["lng"]), latlng_to_xyz(pos2["lat"],pos2["lng"])
    return acos(sum(x * y for x, y in zip(xyz0, xyz1)))*radious