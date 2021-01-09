from accounts.viewsets import ConditionsViewSets, CustomUserViewSets
from consultation.viewsets import ConsultationViewSets, RefferViewSets, AdmitViewSets
from drugs.viewsets import DrugsViewSets, PrescriptionViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'conditions', ConditionsViewSets)
router.register(r'customuser', CustomUserViewSets)
router.register(r'consultation', ConsultationViewSets)
router.register(r'reffer', RefferViewSets)
router.register(r'admit', AdmitViewSets)
router.register(r'drugs', DrugsViewSets)
router.register(r'prescription', PrescriptionViewSets)



