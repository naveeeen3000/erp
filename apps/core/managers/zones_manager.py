from apps.core.models.zones import Zones
from rest_framework.exceptions import ValidationError


class ZonesManager:

    def __init__(self):
        pass


    def get_zones_by_id(self,id=None):
        if id is None:
            raise ValidationError("id should be provided")
        zone = Zones.objects.get(id=id)
        if zone:
            return zone
        return None
    
    def get_zones_by_pincode(self,pincode=None):
        if  pincode is None:
            raise ValidationError("pincode must be provided.")
        zones = Zones.objects.filter(zone_pincode=pincode)
        if zones.exists():
            return zones
        return None
    
    def get_zones_by_pincode_and_name(self,pincode=None,name=None):
        if not pincode and not name:
            raise ValidationError("Pincode and name must be provided.")
        zones = Zones.objects.filter(zone_pincode=pincode,zone_name=name)
        if zones.exists():
            return Zones
        return None
    
    def get_zones_by_pincode_and_city_or_district(self,pincode=None,names=None):
        if pincode is None:
            raise ValidationError("pincode must be provided.")
        if type(names) != list:
            raise ValidationError("names must be a list.")
        zones = Zones.objects.filter(zone_pincode=pincode,zone_name__in=names)
        if zones.exists():
            return zones
        zones = Zones.objects.filter(zone_pincode=pincode)
        if zones.exists():
            return zones
        return None