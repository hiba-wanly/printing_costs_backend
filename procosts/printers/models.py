from django.db import models

# Create your models here.
class Printers(models.Model):
    name = models.CharField(max_length = 250)
    # كلفة التحضير
    preparation_cost = models.FloatField()
    #كلفة بداية   
    start_up_cost = models.FloatField()
    #اهتلاك الطابعة
    printer_wear_and_tear  = models.IntegerField()
    #اهتلاكها بالساعات
    depreciation_in_hours = models.IntegerField()
    #اهتلاك ساعي
    courier_depreciation = models.FloatField()
    #اهتلاك انفرتر و بطارية
    inverter_and_battery_wear = models.IntegerField()
    #كيلوواط عمرها
    kilowatts_old = models.IntegerField()
    #سعرالكيلو الواط مع اهتلاك
    price_per_kilowatt_with_depreciation = models.FloatField()
    #كهرباء ساعي
    electricity_courier = models.FloatField()
    #تكاليف كهرباء
    electricity_costs = models.FloatField()
    #طباعة ساعية
    courier_printing = models.FloatField()
    #واحدة المواد
    single_material = models.TextField(max_length = 50)
    #تكاليف إنهاء
    termination_costs = models.FloatField()
    #تكاليف إشراف
    supervision_costs = models.FloatField()
