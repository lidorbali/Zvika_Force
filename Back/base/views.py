from itertools import product
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Category, Product ,Order, Order_det
from django.contrib.auth import logout

 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
 
 
from .serializers import ProductSerializer ,CategorySerializer

# Create your views here.
#login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name


        # ...
 
        return token
    
     
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
 
 
# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         'api/token',
#         'api/token/refresh',
#     ]

    # return Response(routes)


#logOut
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myLogout(request):
    logout(request)
    return Response("Logout sucsses")

# register
@api_view(['POST'])
def register(request):

    User.objects.create_user(  email=request.data["email"], password=request.data["password"],last_name=request.data['last_name'],first_name=request.data['first_name'], tel=request.data['telephone']
     )
    print(request.data["username"])
    print(request.data["email"])
    print(request.data["password"])
    return JsonResponse({"DONE":"register"})





@api_view(['POST'])

def addCats(request):

    serializer = CategorySerializer(data=request.data)

    if( serializer.is_valid()):
        serializer.save()#user_id=request.user.id)
    else:
        return Response("data was not saved, error ....")

    return Response("category was create successfully")

@api_view(['GET'])
def getCats(request):
    categories= Category.objects.all()
    serializer = CategorySerializer(categories,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)

    if( serializer.is_valid()):
        serializer.save()#user_id=request.user.id)
    else:
        return Response("data was not saved, error ....")

    return Response("product was create successfully")





@api_view(['GET'])
def getProduct(request,id=0):
    
    if int(id) > 0:
        products= Product.objects.filter(cat_id=int(id))
    else:
        products= Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrder(request):
    orders=request.data
    # create a single oreder
    newOrder= Order.objects.create(user_id=request.user,total=1)

    # create new order details
    for x in orders:
        newProd=Product.objects.get(_id= x["_id"])
        total=newProd.price * x["amount"]
        Order_det.objects.create(order_id=newOrder,prod_id=newProd,amount=x["amount"],total=total)

    # print(newOrder)
    # Order_det.objects.create(order_id=newOrder,)
    return Response("product was create successfully")