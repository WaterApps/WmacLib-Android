# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_geos', [dirname(__file__)])
        except ImportError:
            import _geos
            return _geos
        if fp is not None:
            try:
                _mod = imp.load_module('_geos', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _geos = swig_import_helper()
    del swig_import_helper
else:
    import _geos
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _geos.SwigPyIterator_value(self)
    def incr(self, n = 1): return _geos.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _geos.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _geos.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _geos.SwigPyIterator_equal(self, *args)
    def copy(self): return _geos.SwigPyIterator_copy(self)
    def next(self): return _geos.SwigPyIterator_next(self)
    def __next__(self): return _geos.SwigPyIterator___next__(self)
    def previous(self): return _geos.SwigPyIterator_previous(self)
    def advance(self, *args): return _geos.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _geos.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _geos.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _geos.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _geos.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _geos.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _geos.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _geos.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

GEOS_VERSION_MAJOR = _geos.GEOS_VERSION_MAJOR
GEOS_VERSION_MINOR = _geos.GEOS_VERSION_MINOR
GEOS_VERSION = _geos.GEOS_VERSION
GEOS_JTS_PORT = _geos.GEOS_JTS_PORT
GEOS_CAPI_VERSION_MAJOR = _geos.GEOS_CAPI_VERSION_MAJOR
GEOS_CAPI_VERSION_MINOR = _geos.GEOS_CAPI_VERSION_MINOR
GEOS_CAPI_VERSION_PATCH = _geos.GEOS_CAPI_VERSION_PATCH
GEOS_CAPI_FIRST_INTERFACE = _geos.GEOS_CAPI_FIRST_INTERFACE
GEOS_CAPI_LAST_INTERFACE = _geos.GEOS_CAPI_LAST_INTERFACE
GEOS_CAPI_VERSION = _geos.GEOS_CAPI_VERSION
GEOS_POINT = _geos.GEOS_POINT
GEOS_LINESTRING = _geos.GEOS_LINESTRING
GEOS_LINEARRING = _geos.GEOS_LINEARRING
GEOS_POLYGON = _geos.GEOS_POLYGON
GEOS_MULTIPOINT = _geos.GEOS_MULTIPOINT
GEOS_MULTILINESTRING = _geos.GEOS_MULTILINESTRING
GEOS_MULTIPOLYGON = _geos.GEOS_MULTIPOLYGON
GEOS_GEOMETRYCOLLECTION = _geos.GEOS_GEOMETRYCOLLECTION
GEOS_WKB_XDR = _geos.GEOS_WKB_XDR
GEOS_WKB_NDR = _geos.GEOS_WKB_NDR

def version():
  return _geos.version()
version = _geos.version
class CoordinateSequence(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _geos.new_CoordinateSequence(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _geos.delete_CoordinateSequence
    __del__ = lambda self : None;
    def clone(self): return _geos.CoordinateSequence_clone(self)
    def setX(self, *args): return _geos.CoordinateSequence_setX(self, *args)
    def setY(self, *args): return _geos.CoordinateSequence_setY(self, *args)
    def setZ(self, *args): return _geos.CoordinateSequence_setZ(self, *args)
    def setOrdinate(self, *args): return _geos.CoordinateSequence_setOrdinate(self, *args)
    def getX(self, *args): return _geos.CoordinateSequence_getX(self, *args)
    def getY(self, *args): return _geos.CoordinateSequence_getY(self, *args)
    def getZ(self, *args): return _geos.CoordinateSequence_getZ(self, *args)
    def getOrdinate(self, *args): return _geos.CoordinateSequence_getOrdinate(self, *args)
    def getSize(self): return _geos.CoordinateSequence_getSize(self)
    def getDimensions(self): return _geos.CoordinateSequence_getDimensions(self)
CoordinateSequence_swigregister = _geos.CoordinateSequence_swigregister
CoordinateSequence_swigregister(CoordinateSequence)

class Geometry(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_Geometry
    __del__ = lambda self : None;
    def clone(self): return _geos.Geometry_clone(self)
    def geomType(self): return _geos.Geometry_geomType(self)
    def typeId(self): return _geos.Geometry_typeId(self)
    def normalize(self): return _geos.Geometry_normalize(self)
    def getSRID(self): return _geos.Geometry_getSRID(self)
    def setSRID(self, *args): return _geos.Geometry_setSRID(self, *args)
    def getDimensions(self): return _geos.Geometry_getDimensions(self)
    def getNumGeometries(self): return _geos.Geometry_getNumGeometries(self)
    def intersection(self, *args): return _geos.Geometry_intersection(self, *args)
    def buffer(self, *args): return _geos.Geometry_buffer(self, *args)
    def convexHull(self): return _geos.Geometry_convexHull(self)
    def difference(self, *args): return _geos.Geometry_difference(self, *args)
    def symDifference(self, *args): return _geos.Geometry_symDifference(self, *args)
    def boundary(self): return _geos.Geometry_boundary(self)
    def union(self, *args): return _geos.Geometry_union(self, *args)
    def pointOnSurface(self): return _geos.Geometry_pointOnSurface(self)
    def getCentroid(self): return _geos.Geometry_getCentroid(self)
    def getEnvelope(self): return _geos.Geometry_getEnvelope(self)
    def relate(self, *args): return _geos.Geometry_relate(self, *args)
    def lineMerge(self): return _geos.Geometry_lineMerge(self)
    def simplify(self, *args): return _geos.Geometry_simplify(self, *args)
    def topologyPreserveSimplify(self, *args): return _geos.Geometry_topologyPreserveSimplify(self, *args)
    def relatePattern(self, *args): return _geos.Geometry_relatePattern(self, *args)
    def disjoint(self, *args): return _geos.Geometry_disjoint(self, *args)
    def touches(self, *args): return _geos.Geometry_touches(self, *args)
    def intersects(self, *args): return _geos.Geometry_intersects(self, *args)
    def crosses(self, *args): return _geos.Geometry_crosses(self, *args)
    def within(self, *args): return _geos.Geometry_within(self, *args)
    def contains(self, *args): return _geos.Geometry_contains(self, *args)
    def overlaps(self, *args): return _geos.Geometry_overlaps(self, *args)
    def equals(self, *args): return _geos.Geometry_equals(self, *args)
    def equalsExact(self, *args): return _geos.Geometry_equalsExact(self, *args)
    def isEmpty(self): return _geos.Geometry_isEmpty(self)
    def isValid(self): return _geos.Geometry_isValid(self)
    def isSimple(self): return _geos.Geometry_isSimple(self)
    def isRing(self): return _geos.Geometry_isRing(self)
    def hasZ(self): return _geos.Geometry_hasZ(self)
    def area(self): return _geos.Geometry_area(self)
    def length(self): return _geos.Geometry_length(self)
    def distance(self, *args): return _geos.Geometry_distance(self, *args)
Geometry_swigregister = _geos.Geometry_swigregister
Geometry_swigregister(Geometry)

class Point(Geometry):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_Point
    __del__ = lambda self : None;
    def getCoordSeq(self): return _geos.Point_getCoordSeq(self)
Point_swigregister = _geos.Point_swigregister
Point_swigregister(Point)

class LineString(Geometry):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_LineString
    __del__ = lambda self : None;
    def getCoordSeq(self): return _geos.LineString_getCoordSeq(self)
LineString_swigregister = _geos.LineString_swigregister
LineString_swigregister(LineString)

class LinearRing(Geometry):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_LinearRing
    __del__ = lambda self : None;
    def getCoordSeq(self): return _geos.LinearRing_getCoordSeq(self)
LinearRing_swigregister = _geos.LinearRing_swigregister
LinearRing_swigregister(LinearRing)

class Polygon(Geometry):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_Polygon
    __del__ = lambda self : None;
    def getExteriorRing(self): return _geos.Polygon_getExteriorRing(self)
    def getNumInteriorRings(self): return _geos.Polygon_getNumInteriorRings(self)
    def getInteriorRingN(self, *args): return _geos.Polygon_getInteriorRingN(self, *args)
Polygon_swigregister = _geos.Polygon_swigregister
Polygon_swigregister(Polygon)

class GeometryCollection(Geometry):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_GeometryCollection
    __del__ = lambda self : None;
    def getGeometryN(self, *args): return _geos.GeometryCollection_getGeometryN(self, *args)
GeometryCollection_swigregister = _geos.GeometryCollection_swigregister
GeometryCollection_swigregister(GeometryCollection)

class MultiPoint(GeometryCollection):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_MultiPoint
    __del__ = lambda self : None;
MultiPoint_swigregister = _geos.MultiPoint_swigregister
MultiPoint_swigregister(MultiPoint)

class MultiLineString(GeometryCollection):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_MultiLineString
    __del__ = lambda self : None;
MultiLineString_swigregister = _geos.MultiLineString_swigregister
MultiLineString_swigregister(MultiLineString)

class MultiLinearRing(GeometryCollection):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_MultiLinearRing
    __del__ = lambda self : None;
MultiLinearRing_swigregister = _geos.MultiLinearRing_swigregister
MultiLinearRing_swigregister(MultiLinearRing)

class MultiPolygon(GeometryCollection):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_MultiPolygon
    __del__ = lambda self : None;
MultiPolygon_swigregister = _geos.MultiPolygon_swigregister
MultiPolygon_swigregister(MultiPolygon)


def createPoint(*args):
  return _geos.createPoint(*args)
createPoint = _geos.createPoint

def createLineString(*args):
  return _geos.createLineString(*args)
createLineString = _geos.createLineString

def createLinearRing(*args):
  return _geos.createLinearRing(*args)
createLinearRing = _geos.createLinearRing

def createPolygon(*args):
  return _geos.createPolygon(*args)
createPolygon = _geos.createPolygon
class Prepared(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _geos.new_Prepared(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _geos.delete_Prepared
    __del__ = lambda self : None;
    def contains(self, *args): return _geos.Prepared_contains(self, *args)
    def containsProperly(self, *args): return _geos.Prepared_containsProperly(self, *args)
    def covers(self, *args): return _geos.Prepared_covers(self, *args)
    def intersects(self, *args): return _geos.Prepared_intersects(self, *args)
Prepared_swigregister = _geos.Prepared_swigregister
Prepared_swigregister(Prepared)

class STRtree(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _geos.new_STRtree(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _geos.delete_STRtree
    __del__ = lambda self : None;
    def insert(self, *args): return _geos.STRtree_insert(self, *args)
    def remove(self, *args): return _geos.STRtree_remove(self, *args)
    def query(self, *args): return _geos.STRtree_query(self, *args)
    def iterate(self, *args): return _geos.STRtree_iterate(self, *args)
STRtree_swigregister = _geos.STRtree_swigregister
STRtree_swigregister(STRtree)

class WktReader(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self): 
        this = _geos.new_WktReader()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _geos.delete_WktReader
    __del__ = lambda self : None;
    def read(self, *args): return _geos.WktReader_read(self, *args)
WktReader_swigregister = _geos.WktReader_swigregister
WktReader_swigregister(WktReader)

class WktWriter(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self): 
        this = _geos.new_WktWriter()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _geos.delete_WktWriter
    __del__ = lambda self : None;
    def write(self, *args): return _geos.WktWriter_write(self, *args)
WktWriter_swigregister = _geos.WktWriter_swigregister
WktWriter_swigregister(WktWriter)

class WkbReader(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self): 
        this = _geos.new_WkbReader()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _geos.delete_WkbReader
    __del__ = lambda self : None;
    def read(self, *args): return _geos.WkbReader_read(self, *args)
    def readHEX(self, *args): return _geos.WkbReader_readHEX(self, *args)
WkbReader_swigregister = _geos.WkbReader_swigregister
WkbReader_swigregister(WkbReader)

class WkbWriter(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self): 
        this = _geos.new_WkbWriter()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _geos.delete_WkbWriter
    __del__ = lambda self : None;
    def getOutputDimension(self): return _geos.WkbWriter_getOutputDimension(self)
    def setOutputDimension(self, *args): return _geos.WkbWriter_setOutputDimension(self, *args)
    def getByteOrder(self): return _geos.WkbWriter_getByteOrder(self)
    def setByteOrder(self, *args): return _geos.WkbWriter_setByteOrder(self, *args)
    def getIncludeSRID(self): return _geos.WkbWriter_getIncludeSRID(self)
    def setIncludeSRID(self, *args): return _geos.WkbWriter_setIncludeSRID(self, *args)
    def write(self, *args): return _geos.WkbWriter_write(self, *args)
    def writeHEX(self, *args): return _geos.WkbWriter_writeHEX(self, *args)
WkbWriter_swigregister = _geos.WkbWriter_swigregister
WkbWriter_swigregister(WkbWriter)



