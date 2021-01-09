from accounts.viewsets import ConditionsViewSets, CustomUserViewSets
from consultation.viewsets import ConsultationViewSets, RefferViewSets, AdmitViewSets
from drugs.viewsets import DrugsViewSets, PrescriptionViewSets
from hospital.viewsets import HospitalViewSets, User_HospitalViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'conditions', ConditionsViewSets)
router.register(r'customuser', CustomUserViewSets)
router.register(r'consultation', ConsultationViewSets)
router.register(r'reffer', RefferViewSets)
router.register(r'admit', AdmitViewSets)
router.register(r'drugs', DrugsViewSets)
router.register(r'prescription', PrescriptionViewSets)
router.register(r'hospital', HospitalViewSets)
router.register(r'userhospital', User_HospitalViewSets)



