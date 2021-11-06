from rest_framework.routers import DefaultRouter
import client.views as client
import settings.views as settings

router = DefaultRouter()

router.register(r'client', client.ClientList)
router.register(r'client-telephone', client.TelephoneList)
router.register(r'client-address', client.AddressList)
router.register(r'client-observation', client.ObservationList)
router.register(r'client-equipment', client.EquipmentList)

router.register(r'settings', settings.SettingList)
router.register(r'settings-equipment', settings.EquipmentList)
router.register(r'settings-equipment-type', settings.EquipmentTypeList)