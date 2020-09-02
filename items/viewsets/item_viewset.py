from rest_framework import viewsets, status
from rest_framework.response import Response

from branches.models import BranchUser
from items.models import BranchItem, CompanyItem, CompanyBrand
from items.serializers import ItemSerializer, CreateItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = BranchItem.objects.all()
    serializer_class = ItemSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return CreateItemSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        create_item_serializer = CreateItemSerializer(data=request.data)

        if not create_item_serializer.is_valid():
            return Response("Bad request", status.HTTP_400_BAD_REQUEST)

        user_branch = BranchUser.objects.filter(user=request.user).first()

        if not user_branch:
            return Response(
                "User doesn't belong to a company", status.HTTP_403_FORBIDDEN
            )

        cleaned_data = create_item_serializer.data
        new_company_item = CompanyItem(
            sku=cleaned_data["sku"],
            model=cleaned_data["model"],
            brand=CompanyBrand.objects.get(
                id__exact=cleaned_data["brand"], company=user_branch.branch.company
            ),
            cost=cleaned_data["cost"],
            price=cleaned_data["price"],
            category=cleaned_data["category"],
            subcategory=cleaned_data["subcategory"],
            company=user_branch.branch.company,
        )
        new_company_item.save()
        new_company_item.refresh_from_db()
        BranchItem(
            item=new_company_item,
            branch=user_branch.branch,
            cost=cleaned_data["cost"],
            price=cleaned_data["price"],
        ).save()

        return Response("OK", status.HTTP_201_CREATED)
