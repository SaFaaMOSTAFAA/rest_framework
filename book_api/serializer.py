# from book_api.models import Book
# from rest_framework import serializers

# class BookSerializer(serializers.Serializer) :
#     id = serializers.CharField(read_only= True)
#     title = serializers.CharField(max_length=100)
#     number_of_pages = serializers.IntegerField()
#     publish_date = serializers.DateTimeField() 
#     quantity = serializers.IntegerField() 

#     def create(request,data) :
#         return Book.objects.create(**data) 
    
#     def update(self, instance, data):
#         instance.title=data.get('title',instance.title)
#         instance.number_of_pages=data.get('number_of_pages',instance.number_of_pages)
#         instance.publish_date=data.get('publish_date',instance.publish_date)
#         instance.quantity=data.get('quantity',instance.quantity)

#         instance.save()
#         return instance


from book_api.models import Book
from rest_framework import serializers
from django.forms import ValidationError

# to inherent model class to serializer class

class BookSerializer(serializers.ModelSerializer):
    description= serializers.SerializerMethodField()
    class Meta:
        model=Book
        fields= "__all__"

    def validate_title(self, value):
        if value=="badbook" :
            raise ValidationError("No badbook")
        return value    
    
    def validate(self,data):
        if data["number_of_pages"] and data["quantity"] >200 :
            raise ValidationError("too heavy for inventory")
        return data
    
    def get_description(self,data):
        return "This book is called " +data.title +" and it is " +str(data.number_of_pages) + "pages long."