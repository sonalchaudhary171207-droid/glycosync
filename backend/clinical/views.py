from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import GlucoseReading
from .serializers import GlucoseReadingSerializer


class GlucoseListCreateView(APIView):
    def get(self, request):
        readings = GlucoseReading.objects.all().order_by('-timestamp')[:10]
        serializer = GlucoseReadingSerializer(readings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GlucoseReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DietEngineView(APIView):
    def post(self, request):
        glucose_level = request.data.get('glucose_level', 120)
        query = request.data.get('query', '')

        recommendation = f"Based on your glucose level of {glucose_level} mg/dL, recommended meal: Grilled chicken salad with olive oil and quinoa."
        return Response({'recommendation': recommendation}, status=status.HTTP_200_OK)