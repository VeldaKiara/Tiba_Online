from accounts.viewsets import ConditionsViewSets, CustomUserViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'conditions', ConditionsViewSets)
router.register(r'customuser', CustomUserViewSets)